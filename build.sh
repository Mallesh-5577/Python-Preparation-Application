#!/usr/bin/env bash
set -o errexit

python -m pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py seed_data

if [ -f "README.md" ]; then
	python manage.py import_guide README.md
fi