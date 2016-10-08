#! /usr/bin/env python
#-*-encoding:utf8-*-
'''
Created on 2016年10月8日

@author: wangheng
'''
import threading
from time import  sleep,ctime
loops = [4,2]


def loop(nloop,nesc):
    print 'start loop',nloop,'at:',ctime()
    sleep(nesc)
    print 'loop',nloop,'done at:',ctime()
    
    
class ThreadFunc(object):
    '''
    相当于task类的包装
    统一的函数名字，函数参数。
    需要重定义__call__函数
    '''
    def __init__(self,func,args,name=""):
        self.name=name
        self.func=func
        self.args=args
    def __call__(self):
        apply(self.func,self.args)


def main():
    print 'starting at:',ctime()
    threads=list()
    nloops = range(len(loops))
    for i in nloops:
        t=threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print 'all done at:',ctime()
if __name__ == '__main__':
    main()
        
    
    
    