# -*- coding: utf-8 -*-
__author__ = 'xuwen'

import os
import Data
import postRequest


#Bapp测试环境
BASE_URL_PATH_BROKER = "http://t.a.jzsec.com/"

#Bweb测试环境
BASE_URL_PATH_BWEB = "http://t.b.jzsec.com/"

#Bweb登录接口
BWEB_LOGIN = "site/login"

#身份证审核接口
AFFILIATE_AUDITID = "buser/auditid"

#合同签收接口
SIGN_CONTRACT = "buser/signcontract"

#SAC账号接口
SAC_ACCOUNT = "buser/auditcer"

#执业证书编号接口
SAC_ID = "buser/auditcerid"

#SAC审核/年审
SAC_APPROVE = "buser/auditcerstatus"

#证券从业资格考试
EXAM = "buser/insertexamcondition"

#项目路径
PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

#测试数据
DATA = Data.TestData()

#模块名称
MODULE = ''

#日志信息
LOG = ''


#Bweb后台Cookies
COOKIES = postRequest.postLogin()

#个人简介审核接口
INTRODUCTION = "workorder/procorder"







