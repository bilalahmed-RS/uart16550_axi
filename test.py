#!/usr/bin/env python3

from __future__ import print_function

import os

import uart16550_axi

print("Found serv @ version", uart16550_axi.version_str, "(with data", uart16550_axi.data_version_str, ")")
print()
print("Data is in", uart16550_axi.data_location)
assert os.path.exists(uart16550_axi.data_location)
print("Data is version", uart16550_axi.data_version_str, uart16550_axi.data_git_hash)
print("-"*75)
print(uart16550_axi.data_git_msg)
print("-"*75)
print()
print("It contains:")
for root, dirs, files in os.walk(uart16550_axi.data_location):
    dirs.sort()
    for f in sorted(files):
        path = os.path.relpath(os.path.join(root, f), uart16550_axi.data_location)
        print(" -", path)
