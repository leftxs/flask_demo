#!/usr/bin/env bash
set -Eeo pipefail

export FLASK_APP=main.py
export FLASK_ENV=development
flask run -h 0.0.0.0 -p 8000