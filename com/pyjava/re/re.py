#! /usr/bin/env python
#-*-encoding:utf8-*-
'''
Created on 2016年6月30日

@author: wangheng
'''
import re
class ReDemo(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def isMAtch(self,pattern,text):
        result=re.match(pattern, text)
        if result:
            print text
            
        else:
            print "none"
if __name__ == '__main__':
    reDemo=ReDemo()
    
    pattern="^(a)?p" #^匹配字符串开始，(子正则用小括号) ? 代表0个或1个。 .占位符
    text="python"
    reDemo.isMAtch(pattern,text)
    
    pattern="^(a)*p" #^匹配字符串开始，(子正则用小括号) ? 代表0个或多个。 .占位符
    text="python"
    reDemo.isMAtch(pattern,text)
    
    pattern="^(a)+p" #^匹配字符串开始，(子正则用小括号) ＋ 代表1个或多个。 .占位符
    text="python"
    reDemo.isMAtch(pattern,text)
    
    pattern="[1-9]{3}" ##^匹配字符串开始， [1到9] {出现3次} 然后是1这个字符
    text="1a1"
    reDemo.isMAtch(pattern,text)
    
    pattern="[1-9]{3}" #^匹配字符串开始， [1到9] {出现3次}
    text="111"
    reDemo.isMAtch(pattern,text)
    
    pattern="^[1-9]{3}1" #^匹配字符串开始， [1到9] {出现3次} 然后是1这个字符
    text="1114"
    reDemo.isMAtch(pattern,text)
    
    pattern="^[1-9]{3}1" #^匹配字符串开始， [1到9] {出现3次} 然后是1这个字符
    text="1111"
    reDemo.isMAtch(pattern,text)
    
    pattern="^[^1-9]11$" #^匹配字符串开始， 不出现[1到9]  然后是11这2个字符然后终止
    text="0111"
    reDemo.isMAtch(pattern,text)
    
    pattern="^[^1-9]11" #^匹配字符串开始， 不出现[1到9]  然后是1这个字符
    text="0111"
    reDemo.isMAtch(pattern,text)
    
    pattern="\d[.]?\d$" #
    text="0111s"
    reDemo.isMAtch(pattern,text)
    
    pattern="^\d[.]?\d$" #
    text="0111"
    reDemo.isMAtch(pattern,text)
    
    pattern="^([-+]*[\\d]+)[.]?([\\d]+)$" # 数字表达式
    text="-01113.1111"
    result= re.match(pattern, text)
    print result.group(0)
    print result.group(1)
    print result.group(2)
    reDemo.isMAtch(pattern,text)
    
    pattern="\\bwww" # 数字表达式
    text="aa www1"
    reDemo.isMAtch(pattern,text)
    
    pattern = re.compile('(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)')
    str1 = '199.130.81.191'
print(pattern.search(str1)).group(1)
    
    
    
    
    
    
        
    
        