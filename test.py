#!/usr/bin/env python3

from __future__ import print_function

import os

import pythondata_ip_uart16550

print("Found serv @ version", pythondata_ip_uart16550.version_str, "(with data", Uart16550_axi.data_version_str, ")")
print()
print("Data is in", pythondata_ip_uart16550.data_location)
assert os.path.exists(pythondata_ip_uart16550.data_location)
print("Data is version", pythondata_ip_uart16550.data_version_str, pythondata_ip_uart16550.data_git_hash)
print("-"*75)
print(pythondata_ip_uart16550.data_git_msg)
print("-"*75)
print()
print("It contains:")
for root, dirs, files in os.walk(pythondata_ip_uart16550.data_location):
    dirs.sort()
    for f in sorted(files):
        path = os.path.relpath(os.path.join(root, f), pythondata_ip_uart16550.data_location)
        print(" -", path)
