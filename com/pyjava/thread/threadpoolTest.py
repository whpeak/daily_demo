#! /usr/bin/env python
#-*-encoding:utf8-*-
'''
Created on 2016年9月12日

@author: wangheng
'''
import threading
from threadpool import ThreadPool
from threadpool import makeRequests
import time
import random
def hello(sayStr):
    print sayStr
    return "hello";

def print_result(request, result):
    print "the result is %s %r"%(request.requestID, result)

data = [ random.randint(1, 10) for i in range(200) ]
print data
pool = ThreadPool(200)
requests = makeRequests(hello, ("122222"))
for req in requests:
    pool.putRequest(req) 
pool.wait()
# pool.joinAllDismissedWorkers()
print "aaaaaaa"
while 1:
    pass
