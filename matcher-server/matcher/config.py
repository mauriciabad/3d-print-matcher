import os


class Config:
    DATABASE = os.environ.get("DATABASE")
    PRINT_TABLE = os.environ.get("PRINT_TABLE")
    PHOTO_UPLOAD_FOLDER = os.environ.get("PHOTO_UPLOAD_FOLDER")
    CROPPED_UPLOAD_FOLDER = os.environ.get("CROPPED_UPLOAD_FOLDER")
