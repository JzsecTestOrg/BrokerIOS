# -*- coding: utf-8 -*-
__author__ = 'xuwen1'

from Elements import tabElements, settingElements, welcomeElements, loginElements
from CommonMethods import generateLog, globalData, userStatus, Data, dataBase
import login, welcome
import traceback, sys

def logout_smoking(self):
    try:
        tabElements.mineTab(self).click()
        globalData.LOG += generateLog.format_log("点击'我的'选项卡")
        settingElements.settingButton(self).click()
        globalData.LOG += generateLog.format_log("点击设置按钮")
        settingElements.logoutButton(self).click()
        globalData.LOG += generateLog.format_log("点击退出登录")
        el = loginElements.loginPage(self)
        globalData.LOG += generateLog.format_log("成功退出")
    except:
        globalData.LOG += generateLog.format_log("退出登录失败\n" + traceback.format_exc())

def logout(self, i):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    #构造前置条件
    if(userStatus.isLoginSuccess(self) == False):
        if(userStatus.isRegisterSuccess(Data.getTestdata('register', 1, 2)) == False):
            dataBase.insert_buser(Data.getTestdata('register', 1, 2))
        welcome.welcome(self, 'login')
        login.login_smoking(self, Data.getTestdata('login', 1, 2), Data.getTestdata('login', 1, 3))

    #处理退出逻辑
    try:
        tabElements.mineTab(self).click()
        globalData.LOG += generateLog.format_log("点击'我的'选项卡")
        settingElements.settingButton(self).click()
        globalData.LOG += generateLog.format_log("点击设置按钮")
        settingElements.logoutButton(self).click()
        globalData.LOG += generateLog.format_log("点击退出登录")
        el = loginElements.loginPage(self)
        globalData.LOG += generateLog.format_log("成功退出")
        Data.setExecutionresult(globalData.MODULE, i, 'Pass')
    except:
        globalData.LOG += generateLog.format_log("退出登录失败\n" + traceback.format_exc())
        Data.setExecutionresult(globalData.MODULE, i, 'Fail')

