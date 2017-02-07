#!/usr/bin/python

import re
import subprocess
import os

print("starting startprocess[" + str(os.getpid()) + "]")
# create a new process and pipe the output
print("start first")
output1 = subprocess.check_output(["python","threadedprocess.py"])
print("start second")
output2 = subprocess.check_output(["python","threadedprocess.py"])
print("after subprocess starts")
for line in output1.split(os.linesep):
    print line

print "done"
