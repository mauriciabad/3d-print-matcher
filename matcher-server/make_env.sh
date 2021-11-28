#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements_background.txt
pip install -r requirements_matching.txt
