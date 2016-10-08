#! /usr/bin/env python
#-*-encoding:utf8-*-
'''
Created on 2016年10月8日

@author: wangheng
'''
import threading
from time import ctime,sleep
from Queue import Queue
from random import randint

class MyThread(threading.Thread):
    '''
    classdocs
    '''
    def __init__(self,func,args,name=""):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
        
    def getResult(self):
        return self.res
    
    def run(self):
        print 'starting',self.name,'at:',ctime()
        self.res = apply(self.func,self.args)
        print self.name,'finished at:',ctime()
        
def writeQ(queue):
    print 'producing object for Q...'
    queue.put('xxx',1)
    print 'size now',queue.qsize()
    
def readQ(queue):
    val=queue.get(1)
    print 'consumed object from Q... size now',queue.qsize(),val

def writer(queue,loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))
        
def reader(queue,loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2,5))

funcs =[writer,reader]
nfuncs = range(len(funcs))
def main():
    nloops=randint(10,10)
    print nloops
    q=Queue(32)
    threads=list()
    for i in nfuncs:
        t=MyThread(funcs[i],(q,nloops),funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
if __name__ == '__main__':
    main()
    
        


    
        