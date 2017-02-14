#!/usr/bin/python
import subprocess

output = subprocess.check_output(["ps", "ax", "-o", "pid="])

for line in output.split('\n'):
    pid = int(line)
    if pid:
        print("pid: " + str(pid))
    else:
        print("invalid line: " + line)