#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python -m ipykernel install --user --name en3160 --display-name "Python (EN3160)"
python -m playwright install chromium
python scripts/verify_environment.py
