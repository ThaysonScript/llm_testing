#!/usr/bin/env bash

python3 -m venv venv

source env/bin/activate

pip install -r requirements.txt

python -m ipykernel install --user --name=env --display-name "virtual_env_personalizado"
