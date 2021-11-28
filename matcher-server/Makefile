.PHONY: format lint run

format:
	black matcher/
	isort matcher/

lint:
	mypy matcher/
	flake8 matcher/

run:
	DATABASE=db PIECE_TABLE=piece RENDER_TABLE=render PHOTO_UPLOAD_FOLDER="./photos" CROPPED_UPLOAD_FOLDER="./cropped" RENDERS_FOLDER="../renderer-server/out" TIMEOUT=90 ./run.sh

