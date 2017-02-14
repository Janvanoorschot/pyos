#!/usr/bin/python
import subprocess

output = subprocess.check_output(["ps", "ax", "-o", "pid="])

for line in output.split('\n'):
    try:
        pid = int(line)
        print("pid: " + str(pid))
    except:
        print("invalid line: " + line)