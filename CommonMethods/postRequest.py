# -*- coding: utf-8 -*-
__author__ = 'xuwen'


import urllib
import dataBase, generateLog
import globalData
import requests



def auditId(mobilephone):
    session = dataBase.db_session()
    url = globalData.BASE_URL_PATH_BWEB + globalData.AFFILIATE_AUDITID
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(mobilephone)).first().bid
    params = urllib.urlencode({'id': bid, 'audit_reason': '', 'audit_status': 2})
    cookies = globalData.COOKIES
    response = requests.get(url, data = params, cookies = cookies)
    return response._content[8:9]


def signContract(mobilephone, startdate, enddate):
    session = dataBase.db_session()
    url = globalData.BASE_URL_PATH_BWEB + globalData.SIGN_CONTRACT
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(mobilephone)).first().bid
    params = urllib.urlencode({'id': bid, 'contract_start': startdate, 'contract_end': enddate})
    cookies = globalData.COOKIES
    response = requests.get(url, data = params, cookies = cookies)
    session.close()
    return response._content[8:9]


def sacAccount(mobilephone, username, password):
    session = dataBase.db_session()
    url = globalData.BASE_URL_PATH_BWEB + globalData.SAC_ACCOUNT
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(mobilephone)).first().bid
    params = urllib.urlencode({'id': bid, 'sac_apply_count': username, 'sac_apply_password': password})
    cookies = globalData.COOKIES
    response = requests.get(url, data = params, cookies = cookies)
    session.close()
    return response._content[8:9]


def sacID(mobilephone, id):
    session = dataBase.db_session()
    url = globalData.BASE_URL_PATH_BWEB + globalData.SAC_ID
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(mobilephone)).first().bid
    params = urllib.urlencode({'id': bid, 'sac_id': str(id)})
    cookies = globalData.COOKIES
    response = requests.get(url, data = params, cookies = cookies)
    session.close()
    return response._content[8:9]


def sacApprove(mobilephone):
    session = dataBase.db_session()
    url = globalData.BASE_URL_PATH_BWEB + globalData.SAC_APPROVE
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(mobilephone)).first().bid
    params = urllib.urlencode({'id': bid, 'sac_status': '2'})
    cookies = globalData.COOKIES
    response = requests.get(url, data = params, cookies = cookies)
    session.close()
    return response._content[8:9]

def examPass(mobilephone):
    session = dataBase.db_session()
    url = globalData.BASE_URL_PATH_BWEB + globalData.EXAM
    bid = session.execute("select * from b_user WHERE mobilephone = " + str(mobilephone)).first().bid
    params = urllib.urlencode({'id': bid, 'select': '2'})
    cookies = globalData.COOKIES
    response = requests.get(url, data = params, cookies = cookies)
    session.close()
    return response._content[8:9]

def introductionPass(mobilephone):
    id = dataBase.get_work_order(mobilephone)
    url = globalData.BASE_URL_PATH_BWEB + globalData.INTRODUCTION
    params = urllib.urlencode({'id': id, 'status': '1', 'comment': '审核通过'})
    cookies = globalData.COOKIES
    response = requests.get(url, data = params, cookies = cookies)
    return response._content[8:9]



def postLogin():
    params = urllib.urlencode({'LoginForm[name]': 'admin', 'LoginForm[password]': '123456', 'login-button': ''})
    session = requests.session()
    session.get("http://t.b.jzsec.com/site/login", data = params)
    PHPSESSID = str(session.cookies).split("PHPSESSID=")[1].split(" ")[0]
    _csrf = str(session.cookies).split("_csrf=")[1].split(" ")[0]
    cookies = {'PHPSESSID': PHPSESSID, '_csrf': _csrf}
    return cookies


if __name__ == '__main__':
    # print dataBase.uploadid_status(15210262168)
    # if(dataBase.uploadid_status(Data.getNumber('register', 'register', 'phoneText', 1)) != 2):
    #     print 'ok'
        # if(auditId(Data.getNumber('register', 'register', 'phoneText', 1)) == '0'):
        #     globalData.LOG += generateLog.format_log("后台身份证审核通过")
        # else:
        #     globalData.LOG += generateLog.format_log("后台身份证审核错误")
    # else:
    #     globalData.LOG += generateLog.format_log("后台身份证已审核")
    # print auditId(15210262168)
    # print sacID(15210262168, 546758)
    # print sacApprove(15210262168)
    print introductionPass(15210262168)







