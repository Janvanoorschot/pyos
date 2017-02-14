#!/usr/bin/python
import subprocess

# collect pids
pids = []
output = subprocess.check_output(["ps", "ax", "-o", "pid="])
for line in output.split('\n'):
    try:
        pid = int(line)
        pids.append(pid)
    except:
        pass

# per pid, count threads
for pid in pids:
    spids=[]
    try:
        output = subprocess.check_output(["ps", "-e", "-T", "-q", str(pid), "-o", "spid="])
        for line in output.split('\n'):
            try:
                spid = int(line)
                spids.append(spid)
            except:
                pass
        if len(spids) > 1:
            print(str(pid))
    except:
        pass
