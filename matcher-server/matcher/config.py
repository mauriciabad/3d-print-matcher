import os


class Config:
    DATABASE = os.environ.get("DATABASE")
    PRINT_TABLE = os.environ.get("PIECE_TABLE")
    PRINT_TABLE = os.environ.get("RENDER_TABLE")
    PHOTO_UPLOAD_FOLDER = os.environ.get("PHOTO_UPLOAD_FOLDER")
    CROPPED_UPLOAD_FOLDER = os.environ.get("CROPPED_UPLOAD_FOLDER")
