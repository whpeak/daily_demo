#! /usr/bin/env python
#-*-encoding:utf8-*-
'''
Created on 2016年9月27日

@author: wangheng
'''
import thread
from time import sleep,ctime
#thread 模块，仅仅是为了学习，不推荐使用该模块
loops = [2,4] #每一个线程的睡眠时间
def loop (nloop,nesc,lock):
    print "start loop",nloop,"at:",ctime()
    sleep(nesc)
    print 'loop',nloop,'done at:',ctime()
    lock.release()#任务完成后，需要释放该锁
def main():
    print 'starting at:',ctime()
    locks = []
    nloops=range(len(loops))
    for i in nloops:
        lock = thread.allocate_lock()#分配一个锁对象
        lock.acquire()#获取锁对象
        locks.append(lock)#保存该锁
    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i], locks[i]))
    
    for i in nloops:
        while locks[i].locked():#如果该锁locked住，那么就继续执行while语句
            print "wait for ",str(i),"to relase"
            pass
        print 'all done at:',ctime()
if __name__ == '__main__':
        main()