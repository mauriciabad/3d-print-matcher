#!/bin/bash

FLASK_APP=matcher python -m flask init-db
mkdir -p "$PHOTO_UPLOAD_FOLDER" && rm -rf "$PHOTO_UPlOAD_FOLDER/*"
mkdir -p "$CROPPED_UPLOAD_FOLDER" && rm -rf "$CROPPED_UPLOAD_FOLDER/*"
FLASK_APP=matcher python -m gunicorn --timeout $TIMEOUT matcher:app
