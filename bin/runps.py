#!/usr/bin/python
import subprocess

output = subprocess.check_output(["ps", "-e", "-T"])

for line in output:
    print("line: " + line)