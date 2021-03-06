#!/usr/bin/env python3

from __future__ import print_function
import os
from binascii import hexlify
import cantools


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
MOTOHAWK_PATH = os.path.join(SCRIPT_DIR,
                             '..',
                             'tests',
                             'files',
                             'motohawk.dbc')

database = cantools.db.load_file('tests/files/motohawk.dbc')

message = {
    'Temperature': 250.1,
    'AverageRadius': 3.2,
    'Enable': 'Enabled'
}

encoded = database.encode_message('ExampleMessage', message)
decoded = database.decode_message('ExampleMessage', encoded)

print('Message:', message)
print('Encoded:', hexlify(encoded).decode('ascii'))
print('Decoded:', decoded)
