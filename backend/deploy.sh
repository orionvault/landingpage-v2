#!/bin/bash

git pull
source venv/bin/active
pip install -r requirements.txt
cd api
python manage.py migrate
python manage.py collectstatic

echo "DONE."
