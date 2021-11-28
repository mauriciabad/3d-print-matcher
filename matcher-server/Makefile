.PHONY: format lint run

format:
	black matcher/
	isort matcher/

lint:
	mypy matcher/
	flake8 matcher/

install:
	python3 -m venv venv
	source /venv/bin/activate
	pip install -r requirements.txt
	pip install -r requirements_background.txt
	pip install -r requirements_matching.txt

run:
	DATABASE=db PIECE_TABLE=piece RENDER_TABLE=render PHOTO_UPLOAD_FOLDER="./photos" CROPPED_UPLOAD_FOLDER="./cropped" RENDERS_FOLDER="../renderer-server/out" TIMEOUT=90 ./run.sh

