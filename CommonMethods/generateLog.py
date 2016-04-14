# -*- coding: utf-8 -*-
__author__ = 'xuwen'
import globalData, relatedTime
import sys


def generate_log():
    time = relatedTime.reporttime()
    file_name = globalData.PATH + '/TestResult/' + globalData.MODULE + '_' + time + '.txt'
    file = open(file_name, 'w')
    file.write(globalData.LOG)
    file.close

def format_log(info):
    time = relatedTime.currenttime()
    module = globalData.MODULE
    log = time + ": module-" + module + " " + info + "\n"
    print log
    return log

# if __name__ == '__main__':
#     globalData.LOG = 'ceshi'
#     generate_log()




