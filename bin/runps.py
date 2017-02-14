#!/usr/bin/python
import subprocess

output = subprocess.check_output(["ps", "-e", "-T"])

print("output: " + output)