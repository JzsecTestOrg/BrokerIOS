# -*- coding: utf-8 -*-
__author__ = 'xuwen'
import dataBase
from Elements import welcomeElements, tabElements
import generateLog, globalData, Data

def isRegisterSuccess(phone):
    count = len(dataBase.broker_info(phone))
    if(count == 0):
        globalData.LOG += generateLog.format_log("手机号 " + str(phone) + " 未注册")
        return False
    else:
        globalData.LOG += generateLog.format_log("手机号 " + str(phone) + " 已注册")
        return True


def isLoginSuccess(self):
    try:
        el = tabElements.mineTab(self)
        if(el != None):
            globalData.LOG += generateLog.format_log("已登录")
            return True
        else:
            globalData.LOG += generateLog.format_log("未登录")
            return False
    except:
        globalData.LOG += generateLog.format_log("已登录")
        return True


def isUploadidFinished(phone):
    status = dataBase.uploadid_status(phone)
    if(status == 2):
        globalData.LOG += generateLog.format_log("已上传身份证")
        return True
    else:
        globalData.LOG += generateLog.format_log("未上传身份证")
        return False


def isUploadidSuccess(phone):
    status = dataBase.uploadid_status(phone)
    if(status == 0):
        globalData.LOG += generateLog.format_log("未上传身份证")
        return False
    else:
        globalData.LOG += generateLog.format_log("已上传身份证")
        return True

def isTrainFinished(phone):
    status = dataBase.train_status(phone)
    if(status == 1):
        globalData.LOG += generateLog.format_log("培训已完成")
        return True
    else:
        globalData.LOG += generateLog.format_log("培训未完成")
        return False


# def isTrainSuccess(phone):
#     status = dataBase.train_status(phone)
#     if(status == 1):
#         globalData.LOG += generateLog.format_log("培训已完成")
#         return True
#     else:
#         globalData.LOG += generateLog.format_log("培训未完成")
#         return False



def isContractFinished(phone):
    status = dataBase.contract_status(phone)
    if(status == 0):
        globalData.LOG += generateLog.format_log("合同未签收")
        return False
    elif(status == 4):
        globalData.LOG += generateLog.format_log("合同已签收")
        return True


def isSACFinished(phone):
    status = dataBase.sac_status(phone)
    if(status == 2):
        globalData.LOG += generateLog.format_log("SAC已完成")
        return True
    else:
        globalData.LOG += generateLog.format_log("SAC未完成")
        return False


def isExamFinished(phone):
    status = dataBase.exam_status(phone)
    if(status == 2):
        globalData.LOG += generateLog.format_log("证券从业资格考试已完成")
        return True
    else:
        globalData.LOG += generateLog.format_log("证券从业资格考试已解锁")
        return False



if __name__ == '__main__':
    if(isRegisterSuccess(Data.getNumber('commen', 'commen', 'phone', 1)) == True):
        print 'ok'
#             dataBase.del_buser(Data.getNumber('commen', 'commen', 'phone', 1))








