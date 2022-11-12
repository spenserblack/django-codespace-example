#!/bin/bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
python manage.py migrate
