#!/usr/bin/env bash

if [[ ! -d "venv" ]]; then
    python3 -m venv env

    python -m ipykernel install --user --name=env --display-name "virtual_env_personalizado"

fi

source env/bin/activate

pip install --upgrade pip

pip install -r requirements.txt
