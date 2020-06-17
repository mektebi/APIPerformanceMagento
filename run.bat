#!/usr/bin/env bash

PATH=${PATH}:/usr/local/bin

pip3.8 install -r requirements.txt

PYTHONPATH=. python3.8 -m locust -f load_category_list.py  -c 2 -r 1 --no-web --csv=report -t 1m