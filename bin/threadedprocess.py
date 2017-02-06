#!/usr/bin/python

import thread
import time

# Define a function for the thread
def print_time( threadName, delay, maxi):
    count = 0
    while count < maxi:
        time.sleep(delay)
        count += 1
        print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try:
    thread.start_new_thread( print_time, ("Thread-1", 2, 20) )
    thread.start_new_thread( print_time, ("Thread-2", 4, 10) )
except:
    print "Error: unable to start thread"

counter = 0
while counter<40:
    counter = counter + 1
    time.sleep(1)

