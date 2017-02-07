#!/usr/bin/python
import argparse
import os
import threading
import subprocess
import time
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="name of the process", default="main")
parser.add_argument("--children", help="number of child processes", type=int, default=3)
parser.add_argument("--threads", help="number of threads", type=int, default=2)
parser.add_argument("--memory", help="memory count in bytes", type=int, default=2000)
args=parser.parse_args()

def start_childprocess(cname):
    child = {}
    child['name'] = cname
    child['handle'] = subprocess.Popen(['python', 'runit.py', '--children=0', '--name=%s' % (cname)])
    return child

def start_thread(tname):
    thrd = {}
    thrd['name'] = tname
    thrd['handle'] = threading.Thread(target=waste_time_and_space, args=(thrd, 10, 1024))
    thrd['handle'].start()
    return thrd

def waste_time_and_space(thrd, count, size):
    # print("start %s:%d:%d" % (thrd['name'],count,size))
    with tempfile.NamedTemporaryFile() as fn:
        ix = 0
        blocks = []
        while ix < count:
            blocks.append(' ' * size * 1024)
            time.sleep(4)
            ix+=1
    # print("end %s:%d:%d" % (thrd['name'],count,size))

# start yourself
print("strt %s[%d]:%d:%d:%d" % (args.name, os.getpid(), args.children, args.threads, args.memory))
# create children and threads
children = []
threads = []
for x in range(0,args.children):
    children.append(start_childprocess("child_%d" % (x)))
for y in range(0,args.threads):
    threads.append(start_thread("thread_%s_%d" % (args.name,y)))
# wait for children and threads to finish
ready = False
while not ready:
    alldone = True
    for child in children:
        if child['handle'].poll() == None:
            alldone = False
    for thrd in threads:
        if thrd['handle'].isAlive():
            alldone = False
    if alldone:
        ready = True
    else:
        time.sleep(1)
# finish yourself
print("stop %s[%d]:%d:%d:%d" % (args.name, os.getpid(), args.children, args.threads, args.memory))

