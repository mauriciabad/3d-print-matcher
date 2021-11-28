import os


class Config:
    DATABASE = os.environ.get("DATABASE")
    PIECE_TABLE = os.environ.get("PIECE_TABLE")
    RENDER_TABLE = os.environ.get("RENDER_TABLE")
    PHOTO_UPLOAD_FOLDER = os.environ.get("PHOTO_UPLOAD_FOLDER")
    CROPPED_UPLOAD_FOLDER = os.environ.get("CROPPED_UPLOAD_FOLDER")
    RENDERS_FOLDER = os.environ.get("RENDERS_FOLDER")
