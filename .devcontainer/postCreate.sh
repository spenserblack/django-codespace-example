#!/bin/bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
pre-commit install
python manage.py migrate
