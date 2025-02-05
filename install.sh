#!/bin/bash
#

python -m venv .
[ -f ./bin/pip ] && ./bin/pip install --upgrade pip
[ -f ./bin/pip ] && ./bin/pip install -r requirements.txt
