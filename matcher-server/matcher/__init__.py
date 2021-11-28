import os
import uuid

from flask import Flask, request
from flask.json import jsonify
from werkzeug.utils import secure_filename

from matcher.database import init_app, query_db
from background.main import process

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

        # TODO: Compute similarity

        return "Success", 200

    return "File error", 400



@app.route("/pieces", methods=["POST"])
def create_piece():
        model_path = request.json["modelPath"]
        render_paths = request.json["renderPaths"]

        query_db(f"INSERT INTO {app.config['PIECE_TABLE']} (model_path) VALUES(?)", [model_path])

        for render_path in render_paths:
            query_db(f"INSERT INTO {app.config['RENDER_TABLE']} (render_path) VALUES(?)", [render_path])

        return "Success", 200
