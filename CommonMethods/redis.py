# -*- coding: UTF-8 -*-
__author__ = 'xuwen1'

import os
import urllib
import globalData, dataBase, relatedTime



def resetVercode(phone):
    redis_command = globalData.REDIS + 'get sms_verify_code_' + str(phone)
    p = os.popen(globalData.SSH + redis_command)
    return p.read()[0:6]


def registerVercode(phone):
    redis_command = globalData.REDIS + 'get sms_verify_code_' + str(phone)
    p = os.popen(globalData.SSH + redis_command)
    return p.read()[0:6]

def clear_vercode(phone):
    redis_command = globalData.REDIS + 'del sms_verify_code_limit_' + str(phone)
    os.popen(globalData.SSH + redis_command)
    redis_command = globalData.REDIS + 'del sms_verify_code_first_' + str(phone)
    os.popen(globalData.SSH + redis_command)
    redis_command = globalData.REDIS + 'del sms_verify_code_' + str(phone)
    os.popen(globalData.SSH + redis_command)
    redis_command = globalData.REDIS + 'del sms_verify_code_count_' + str(phone)
    os.popen(globalData.SSH + redis_command)
    redis_command = globalData.REDIS + 'del bapp_login_fail_times' + str(phone)
    os.popen(globalData.SSH + redis_command)
    redis_command = globalData.REDIS + 'del sms_verify_code_time_' + str(phone)
    os.popen(globalData.SSH + redis_command)



def registersendVercode(mobilephone):
    params = urllib.urlencode({'mobilephone': mobilephone})
    response = urllib.urlopen("http://t.a.jzsec.com/system/sendauthcode",params).read()
    return response[8:9]


def resetpswsendVercode(mobilephone):
    params = urllib.urlencode({'mobilephone': mobilephone})
    response = urllib.urlopen("http://t.a.jzsec.com/system/sendresetpasscode",params).read()
    return response[8:9]


def expireregisterVercode(phone):
    redis_command = globalData.REDIS + 'expire sms_verify_code_' + str(phone) + ' 0'
    p = os.popen(globalData.SSH + redis_command)
    return p.read()

#禁用答题
def uncheckexamstatus(phone):
    session = dataBase.db_session()
    time = relatedTime.redistime()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    redis_command = globalData.REDIS + "HSET king_broker_" + str(bid)  + " last_finish_time " + str(time)
    p = os.popen(globalData.SSH + redis_command)
    session.close()
    return p.read()

#禁用刷脸
def uncheckfacesignin(phone):
    session = dataBase.db_session()
    time = relatedTime.loadtime()
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(phone)).first().bid
    redis_command = globalData.REDIS + "HSET king_broker_face_" + str(bid) + " last_face_sign_time '" + str(time)[0:10] + "\ " + str(time)[11:19] + "'"
    p = os.popen(globalData.SSH + redis_command)
    session.close()
    return p.read()

#禁用有奖投诉弹窗
def uncheckdailymsg_complaint(phone):
    redis_command = globalData.REDIS + 'HDEL bapp_user_complaint_notice ' + str(phone)
    p = os.popen(globalData.SSH + redis_command)
    return p.read()









if __name__ == '__main__':
    # print resetpswsendVercode(13500000001)
    # print resetVercode(15500000000)
    # print registerVercode(17500000001)
    # print registersendVercode(15500000000)
    # print auditid(15210262168)
    # getcookie()
    # globalData.MODULE = 'register'
    # print Data.getNumber('register', 'phoneText', 1)
    # print registersendVercode(15000000001)
    clear_vercode(15210262168)
    # print uncheckexamstatus(15210262168)
    # print uncheckfacesignin(15210262168)
    # print uncheckdailymsg_complaint(15210262168)

