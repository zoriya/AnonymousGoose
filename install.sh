#!/usr/bin/bash

cd AnonymousGoose 2>/dev/null || git clone https://github.com/AnonymusRaccoon/AnonymousGoose
cd AnonymousGoose || (echo "Error installing." ; exit 1)
virtualenv venv
source venv/bin/activate
pip3 install pyxhook simpleaudio
./run.sh