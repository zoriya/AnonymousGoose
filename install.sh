#!/usr/bin/bash

cd AnonymousGoose || (git clone https://github.com/AnonymusRaccoon/AnonymousGoose && cd AnonymousGoose) || (echo "Error installing." ; exit 1)
virtualenv venv
source venv/bin/activate
pip3 install pyxhook simpleaudio
./main.py