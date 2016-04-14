__author__ = 'xuwen1'

import os
import urllib



def resetVercode(phone):
    redis_command = 'redis-cli -a CRM_jzzq_Redis get sms_verify_code_' + str(phone)
    p = os.popen("ssh -o StrictHostKeyChecking=no root@10.10.13.39 " + redis_command)
    return p.read()[0:6]


def registerVercode(phone):
    redis_command = 'redis-cli -a CRM_jzzq_Redis get sms_verify_code_' + str(phone)
    p = os.popen("ssh -o StrictHostKeyChecking=no root@10.10.13.39 " + redis_command)
    return p.read()[0:6]

def clear_vercode(phone):
    redis_command = 'redis-cli -a CRM_jzzq_Redis del sms_verify_code_limit_' + str(phone)
    os.popen("ssh -o StrictHostKeyChecking=no root@10.10.13.39 " + redis_command)
    redis_command = 'redis-cli -a CRM_jzzq_Redis del sms_verify_code_first_' + str(phone)
    os.popen("ssh -o StrictHostKeyChecking=no root@10.10.13.39 " + redis_command)
    redis_command = 'redis-cli -a CRM_jzzq_Redis del sms_verify_code_' + str(phone)
    os.popen("ssh -o StrictHostKeyChecking=no root@10.10.13.39 " + redis_command)
    redis_command = 'redis-cli -a CRM_jzzq_Redis del sms_verify_code_count_' + str(phone)
    os.popen("ssh -o StrictHostKeyChecking=no root@10.10.13.39 " + redis_command)
    # redis_command = 'redis-cli -a CRM_jzzq_Redis del bapp_login_token_' + str(phone)
    # os.popen("ssh -o StrictHostKeyChecking=no root@10.10.13.39 " + redis_command)
    redis_command = 'redis-cli -a CRM_jzzq_Redis del sms_verify_code_time_' + str(phone)
    os.popen("ssh -o StrictHostKeyChecking=no root@10.10.13.39 " + redis_command)



def registersendVercode(mobilephone):
    params = urllib.urlencode({'mobilephone': mobilephone})
    response = urllib.urlopen("http://t.a.jzsec.com/system/sendauthcode",params).read()
    return response[8:9]


def resetpswsendVercode(mobilephone):
    params = urllib.urlencode({'mobilephone': mobilephone})
    response = urllib.urlopen("http://t.a.jzsec.com/system/sendresetpasscode",params).read()
    return response[8:9]


def expireregisterVercode(phone):
    redis_command = 'redis-cli -a CRM_jzzq_Redis expire sms_verify_code_' + str(phone) + ' 0'
    p = os.popen("ssh -o StrictHostKeyChecking=no root@10.10.13.39 " + redis_command)
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

