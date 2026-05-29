#!/usr/bin/env bash
set -euo pipefail

VEV_DIR=".venv"
python3 -m venv "$VEV_DIR"
echo "Created virtualenv at $VEV_DIR"
source "$VEV_DIR/bin/activate"
pip install --upgrade pip
if [ -f requirements.txt ]; then
	pip install -r requirements.txt
else
	echo "No requirements.txt found. Edit requirements.txt to add dependencies."
fi

# Install package in editable mode so tests can import it
if [ -f pyproject.toml ]; then
	pip install -e .
fi

echo "Done. To activate the environment: source $VEV_DIR/bin/activate"
