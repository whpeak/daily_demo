#! /usr/bin/env python
#-*-encoding:utf8-*-
'''
Created on 2017年1月20日

@author: wangheng
'''
import commands
from datetime import datetime
from time import sleep
class HbaseMonitor(object):
    
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.host_dict={"nslave01":"10.130.81.40","nslave02":"10.130.81.41","nslave06":"10.130.81.26","nslave07":"10.130.81.27","nslave08":"10.130.81.28"}
        
    
    def __currentTime(self):
        return str(datetime.now())
    def __create_monitor_cmd(self,ip):
        monitor_cmd="ssh "+ip+ " 'jps | grep HRegionServer'" 
        return  monitor_cmd
    def __create_start_cmd(self,ip):
        start_cmd="ssh "+ip+ " 'cd /opt/hadoop/hbase/bin; sh hbase-daemon.sh start regionserver'"  
        return  start_cmd
    def __excute_cmd(self,cmd):
        cmd_result=dict()
        (status, output) = commands.getstatusoutput(cmd)
        cmd_result['status']=status #正常执行为0
        cmd_result['output']=output
        return cmd_result
    def __isRestart(self,cmd_result):
        status=cmd_result['status']
        cmd_result=cmd_result['output']
        if 0==status or 256==status:
            print "检测命令顺利执行，分析检测结果。。。。。"
            if  "HRegionServer"  not in cmd_result :
                return  True #正常执行没有结果，说明进程不存在
            else:
                return False
        else:
            return False 
    def __doReStart(self,host,ip,try_num=3):
        print "开始重启目标主机【"+host+"】重启时间:"+self.__currentTime()
        temp=0
        flag=True
        while flag and temp<=try_num:
            start_cmd=self.__create_start_cmd(ip)
            cmd_result=self.__excute_cmd(start_cmd)
            print "目标主机【"+host+"】重启命令执行："+str(cmd_result)
            temp+=1
            monitor_cmd=self.__create_monitor_cmd(ip)
            monitor_result=self.__excute_cmd(monitor_cmd)
            isRestart=self.__isRestart(monitor_result)
            if isRestart:
                print "目标主机【"+host+"】rs 重启失败 ,重启次数:"+str(temp)+"次.10s中后尝试，重启时间:"+self.__currentTime()
                sleep(10)
            else:
                print "目标主机【"+host+"】rs 进程重启完成，重启时间:"+self.__currentTime()
                flag=False 
        if temp==(try_num+1):
            print "目标主机【"+host+"】rs 重启完成"+str(temp)+"次重启。停止重启。停止时间："+self.__currentTime()
    
    def run(self,host,ip):
        print "******************************************************************************"
        print "开始检测目标主机【"+host+"】检测时间:"+self.__currentTime()
        monitor_cmd=self.__create_monitor_cmd(ip)
        cmd_result=self.__excute_cmd(monitor_cmd)
        print "目标主机【"+host+"】检测命令执行："+str(cmd_result)
        isRestart=self.__isRestart(cmd_result)
        if isRestart:
            print "目标主机【"+host+"】rs 进程消失，检测时间:"+self.__currentTime()
            self.__doReStart(host,ip)
        else:
            print "目标主机【"+host+"】rs 进程存在，检测时间:"+self.__currentTime()
        
if __name__ == '__main__':
    hm=HbaseMonitor()
    host_dict=hm.host_dict
#     host="nslave06"
#     ip="10.130.81.26"
    for host,ip in host_dict.items(): 
        hm.run(host, ip)