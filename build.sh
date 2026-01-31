#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Fake the api app's initial migration if the DB has admin applied before it
python manage.py migrate api 0001 --fake --no-input 2>/dev/null || true

# Run all migrations
python manage.py migrate --no-input
