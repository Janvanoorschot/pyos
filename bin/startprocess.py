#!/usr/bin/python

import re
import subprocess
import os

# create a new process and pipe the output
print("start")
output = subprocess.check_output(["python","threadedprocess.py"])
print("end")

for line in output.split(os.linesep):
    print line

print "done"
