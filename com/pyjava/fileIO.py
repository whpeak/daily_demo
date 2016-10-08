#! /usr/bin/env python
#-*-encoding:utf8-*-
'''
Created on 2016年7月29日

@author: wangheng
'''
class FileIO(object):
    def __init__(self):
        pass
    def fileIO(self):       
        filePath="/Users/wangheng/Documents/fileIO/input/48ca0c8e58383b64c34fd48baa7f8943.imda"
        a=list()
        with open(filePath,"r") as files:
            for line in files:
                a.append(line)
            files.close()
        print len(a)

if __name__ == '__main__':
    FileIO().fileIO()