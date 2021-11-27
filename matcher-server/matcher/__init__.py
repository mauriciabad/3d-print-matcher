import os
import uuid

from flask import Flask, request
from flask.json import jsonify
from werkzeug.utils import secure_filename

from matcher.database import init_app, query_db

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
        file.save(os.path.join(app.config["PHOTO_UPLOAD_FOLDER"], filename))

        # TODO: Crop photo
        cropped_filename = filename

        file.save(os.path.join(app.config["CROPPED_UPLOAD_FOLDER"], cropped_filename))

        # query_db(f"INSERT INTO {app.config['PRINT_TABLE']} (picture_path) VALUES(?)", [filename])
        return "Success", 200

    return "File error", 400
