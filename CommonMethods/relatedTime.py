# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

import time, sys
import datetime
reload(sys)
sys.setdefaultencoding('utf8')


NOWTIMEFORMAT = '%Y-%m-%d %X'
LOADTIMEFORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULTFOLLOWFORMAT = "%Y-%m-%d %H:%M"
KPITIMEFORMAT = "%Y%m"
TRADETIMEFORMAT = "%Y%m%d"
REPORTTIMEFORMAT = '%Y%m%d'


def currenttime():
    now = time.strftime(NOWTIMEFORMAT, time.localtime(time.time()))
    return now


def loadtime():
    time = (datetime.datetime.now() + datetime.timedelta(seconds = 1)).strftime(LOADTIMEFORMAT)
    return time


def statustime(time):
    return unicode(time[5:16], "utf-8")


def defaultfollowtime():
    now = time.strftime(DEFAULTFOLLOWFORMAT, time.localtime(time.time()))
    return now


def followtime():
    followtime = (datetime.datetime.now() + datetime.timedelta(minutes = 67)).strftime(DEFAULTFOLLOWFORMAT)
    month = followtime[5:7]
    day = followtime[8:10]
    date = month + '月' + day + '日'
    hour = followtime[11:13]
    minute = followtime[14:16]
    return date, hour, minute, followtime

def kpitime():
    month = ""
    if(len(str(datetime.datetime.now().month - 1)) == 1):
        month = "0" + str(datetime.datetime.now().month - 1)
    else:
        month = str(datetime.datetime.now().month - 1)
    lastmonth = str(datetime.datetime.now().year) + month
    thismonth = datetime.datetime.now().strftime(KPITIMEFORMAT)
    return lastmonth, thismonth

def tradetime():
    tradetime1 = datetime.datetime.now().strftime(TRADETIMEFORMAT)
    recommandtime1 = datetime.datetime.now().strftime(LOADTIMEFORMAT)
    month1 = tradetime1[0:6]
    peroid1 = int(tradetime1[6:8]) + 1
    tradetime2 = (datetime.datetime.now() - datetime.timedelta(peroid1)).strftime(TRADETIMEFORMAT)
    recommandtime2 = (datetime.datetime.now() - datetime.timedelta(peroid1)).strftime(LOADTIMEFORMAT)
    month2 = tradetime2[0:6]
    peroid2 = peroid1 + int(tradetime2[6:8])
    tradetime3 = (datetime.datetime.now() - datetime.timedelta(peroid2)).strftime(TRADETIMEFORMAT)
    recommandtime3 = (datetime.datetime.now() - datetime.timedelta(peroid2)).strftime(LOADTIMEFORMAT)
    month3 = tradetime3[0:6]
    peroid3 = peroid2 + int(tradetime3[6:8])
    tradetime4 = (datetime.datetime.now() - datetime.timedelta(peroid3)).strftime(TRADETIMEFORMAT)
    recommandtime4 = (datetime.datetime.now() - datetime.timedelta(peroid3)).strftime(LOADTIMEFORMAT)
    month4 = tradetime4[0:6]
    return tradetime1, tradetime2, tradetime3, tradetime4, recommandtime1, recommandtime2, recommandtime3, recommandtime4, month1, month2, month3, month4


def reporttime():
    now = time.strftime(REPORTTIMEFORMAT, time.localtime(time.time()))
    return now



if __name__ == '__main__':
    # print currenttime()
#     print loadtime()
#     print defaultfollowtime()
#     print followtime()
#     print tradetime()
    print reporttime()

