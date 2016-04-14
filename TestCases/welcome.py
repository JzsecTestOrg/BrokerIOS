# -*- coding: utf-8 -*-
__author__ = 'xuwen1'

from Elements import welcomeElements
from CommonMethods import globalData, generateLog, Data
import traceback

def welcome(self, action):
    #校验版本更新
    try:
        welcomeElements.versionUpdate_cancel(self).click()
        globalData.LOG += generateLog.format_log("取消版本更新")
    except Exception, e:
        globalData.LOG += generateLog.format_log("未提示版本更新,无需取消更新!")

    #校验欢迎页
    try:
        el = welcomeElements.welcomePage(self)
        for i in range(1, 5):
            if(welcomeElements.welcome_title(self).get_attribute("name")  == Data.getValue('welcome', 'welcome', 'welcome_title', i)):
                globalData.LOG += generateLog.format_log("欢迎第" + str(i) + "页显示正确")
            else:
                globalData.LOG += generateLog.format_log("欢迎第" + str(i) + "页显示错误: " + welcomeElements.welcome_title(self).get_attribute("name"))
            if(i != 4):
                self.driver.execute_script("mobile: scroll", {"direction": "right", "element": el.id})
    except:
        globalData.LOG += generateLog.format_log("欢迎页错误\n" + traceback.format_exc())

    #校验下一步操作
    try:
        if(action == 'login'):
            welcomeElements.welcome_login(self).click()
            globalData.LOG += generateLog.format_log("欢迎页面点击登录")
        elif(action == 'register'):
            welcomeElements.welcome_register(self).click()
            globalData.LOG += generateLog.format_log("欢迎页面点击注册")
    except:
        globalData.LOG += generateLog.format_log('欢迎页面下一操作错误')



