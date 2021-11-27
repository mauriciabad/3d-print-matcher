#!/bin/bash

PHOTOS="./photos"
CROPPED="./cropped"

FLASK_APP=matcher flask init-db
rm -rf "$PHOTOS" && mkdir "$PHOTOS"
rm -rf "$CROPPED" && mkdir "$CROPPED"
FLASK_APP=matcher flask run
