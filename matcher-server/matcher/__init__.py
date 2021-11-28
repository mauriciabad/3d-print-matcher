import logging
import os
import uuid
from os import listdir
from os.path import isfile

from flask import Flask, request, send_file
from flask.json import jsonify
from werkzeug.utils import secure_filename

from background.main import process
from matcher.database import init_app, query_db
from matcher.matching import get_similarity

app = Flask(__name__)
app.config.from_object("matcher.config.Config")
init_app(app)


def get_ext(filename):
    return filename.rsplit(".", 1)[1].lower()


def allowed_file(filename):
    return "." in filename and get_ext(filename) in ["jpg", "jpeg", "png"]


@app.route("/prints", methods=["POST"])
def create_print():
    if "file" not in request.files:
        return "Missing file", 400
    file = request.files["file"]
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == "":
        return "Missing file or empty filename", 400

    if file and allowed_file(file.filename):
        filename = f"{secure_filename(str(uuid.uuid4()))}.{get_ext(file.filename)}"
        file_path = os.path.join(app.config["PHOTO_UPLOAD_FOLDER"], filename)
        file.save(file_path)

        cropped_file_path = os.path.join(app.config["CROPPED_UPLOAD_FOLDER"], filename)
        process(str(file_path), str(cropped_file_path))

        render_files = [
            f
            for f in listdir(app.config["RENDERS_FOLDER"])
            if isfile(os.path.join(app.config["RENDERS_FOLDER"], f))
        ]
        diffs = [
            (
                get_similarity(
                    os.path.join(app.config["RENDERS_FOLDER"], file), cropped_file_path
                ),
                file,
            )
            for file in render_files
        ]
        max_dist, _ = max(diffs)
        min_dist, most_sim_render = min(diffs)

        return jsonify(
            image_uri=f"/renders/{most_sim_render}",
            name=most_sim_render.split("_")[0],
            customer="Jaimito",
            confidence=min_dist / max_dist,
        )

    return "File error", 400


@app.route("/pieces", methods=["POST"])
def create_piece():
    model_path = request.json["modelPath"]
    name = request.json["name"]
    customer = request.json["customer"]
    render_paths = request.json["renderPaths"]

    query_db(
        f"INSERT INTO {app.config['PIECE_TABLE']} (name, customer, model_path) VALUES(?, ?, ?)",
        [name, customer, model_path],
    )
    logging.info(f"New piece: {name}")

    for render_path in render_paths:
        query_db(
            f"INSERT INTO {app.config['RENDER_TABLE']} (model_path, render_path) VALUES(?, ?)",
            [model_path, render_path],
        )
        logging.info(f"New render: {render_path}")
    return "Success", 200


@app.route("/renders/<path:path>")
def get_render_file(path):
    p = os.path.join("..", app.config["RENDERS_FOLDER"], path)
    print(p, isfile(p))
    return send_file(p, as_attachment=True)
