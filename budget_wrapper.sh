#!/bin/bash
if [[ -x "$(command -v python3)" ]]
then 
    python3 --version
    python_version="$(python3 -V 2>&1)"
    if [[ $python_version == "Python 3"* ]]
        then
            pip3 install virtualenv
            python3 -m virtualenv .venv
            source .venv/bin/activate
            pip install Pyfiglet
            pip install Clearing
            pip install simple_term_menu
            pip install prettytable
            pip install pytest
            python3 src/main.py
        else
            echo "Python $python_version is out of date! This program needs the latest version. You can get it here - https://www.python.org/downloads/" >&2
        fi
    else
        echo "Looks like you dont have Python installed, install the latest version here: https://www.python.org/downloads/">&2
    fi
    