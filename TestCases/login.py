# -*- coding: utf-8 -*-
__author__ = 'xuwen'


import time, sys, traceback
from Elements import registerElements, loginElements, tabElements, mineElements, settingElements, welcomeElements
from CommonMethods import redis, globalData, generateLog, Data, userStatus, dataBase, screenShot
import logout



def login_smoking(self, phone, password):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    #登录页面手机号验证
    try:
        loginElements.usernameText(self).clear()
        loginElements.usernameText(self).send_keys(str(phone))
        globalData.LOG += generateLog.format_log("输入登录手机号: " + str(phone))
    except Exception, e:
        globalData.LOG += generateLog.format_log("登录页面手机号输入框错误\n" + traceback.format_exc())
    #登录页面密码验证
    try:
        loginElements.cipherpasswordText(self).send_keys(str(password))
        globalData.LOG += generateLog.format_log("输入登录密码: " + str(password))
    except Exception, e:
        globalData.LOG += generateLog.format_log("登录页面密码输入框错误\n" + traceback.format_exc())

    #登陆页面登录按钮验证
    try:
        loginElements.loginButton(self).click()
        globalData.LOG += generateLog.format_log("登录中...")
        time.sleep(2)
        el = tabElements.mineTab(self)
        globalData.LOG += generateLog.format_log("登录成功")
    except Exception, e:
        globalData.LOG += generateLog.format_log("登录页面登录按钮错误\n" + traceback.format_exc())

def login(self, i):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    #构造前置条件：已注册或者未注册
    if(Data.getPrecondition('login', i) == '手机号未注册'):
        if(userStatus.isRegisterSuccess(Data.getTestdata('login', i, 2)) == True):
            dataBase.del_buser(Data.getTestdata('login', i, 2))
    else:
        if(userStatus.isRegisterSuccess(Data.getTestdata('register', i, 2)) == False):
            dataBase.insert_buser(Data.getTestdata('login', i, 2))
        redis.clear_vercode(Data.getTestdata('login', i, 2))
        redis.uncheckexamstatus(Data.getTestdata('login', i, 2))
        redis.uncheckfacesignin(Data.getTestdata('login', i, 2))
        redis.uncheckdailymsg_complaint(Data.getTestdata('login', i, 2))
        dataBase.uncheckmugshot(Data.getTestdata('login', i, 2))
        dataBase.uncheckdailymsg_id(Data.getTestdata('login', i, 2))
    if(userStatus.isLoginSuccess(self) == True):
        logout.logout_smoking(self)



    #进入登录页面校验
    try:
        if(loginElements.loginPage(self)):
            globalData.LOG += generateLog.format_log('登录页面正确显示')
    except:
        globalData.LOG += generateLog.format_log('登录页面显示错误')

    #处理登录手机号逻辑
    try:
        loginElements.usernameText(self).clear()
        loginElements.usernameText(self).send_keys(Data.getTestdata('login', i, 2))
        globalData.LOG += generateLog.format_log('输入手机号：' + Data.getTestdata('login', i, 2))
    except:
        globalData.LOG += generateLog.format_log('手机号输入错误\n' + traceback.format_exc())

    #处理登录密码逻辑
    try:
        loginElements.cipherpasswordText(self).clear()
        loginElements.cipherpasswordText(self).send_keys(Data.getTestdata('login', i, 3))
        globalData.LOG += generateLog.format_log('输入密码：' + Data.getTestdata('login', i, 3))
    except:
        globalData.LOG += generateLog.format_log('密码输入错误\n' + traceback.format_exc())

    #处理登录密码明暗文逻辑
    try:
        if(Data.getTestdata('login', i, 4) == 'None'):
            globalData.LOG += generateLog.format_log('不对密码明暗文进行校验')
        elif(Data.getTestdata('login', i, 4) == 'Y'):
            if('•' in loginElements.cipherpasswordText(self).get_attribute('value')):
                globalData.LOG += generateLog.format_log('密码显示正确：暗文')
            else:
                globalData.LOG += generateLog.format_log('密码显示错误：明文')
            loginElements.eyecloseButton(self).click()
            globalData.LOG += generateLog.format_log("切换密码为明文")
            if('•'  not in loginElements.plainpasswordText(self).get_attribute('value')):
                globalData.LOG += generateLog.format_log('密码显示正确：明文')
            else:
                globalData.LOG += generateLog.format_log('密码显示错误：暗文')
            loginElements.eyeopenButton(self).click()
            globalData.LOG += generateLog.format_log("切换密码为暗文")
            if('•' in loginElements.cipherpasswordText(self).get_attribute('value')):
                globalData.LOG += generateLog.format_log('密码显示正确：暗文')
            else:
                globalData.LOG += generateLog.format_log('密码显示错误：明文')
    except:
        globalData.LOG += generateLog.format_log('明暗文逻辑错误\n' + traceback.format_exc())


    #处理登录页面客服电话逻辑
    try:
        if(Data.getTestdata('login', i, 5) == 'None'):
            globalData.LOG += generateLog.format_log('不对客服电话校验')
        else:
            if(loginElements.servicephoneText(self)):
                globalData.LOG += generateLog.format_log('客服电话显示正确')
    except:
        globalData.LOG += generateLog.format_log('客服电话显示错误\n' + traceback.format_exc())


    #登录按钮点击逻辑校验
    try:
        if(Data.getTestdata('login', i, 6) == 'Y'):
            loginElements.loginButton(self).click()
            globalData.LOG += generateLog.format_log('点击登录按钮')
            if(Data.getTestdata('login', i, 8) == '2'):
                if(Data.getTestdata('login', i, 10) == '账号锁定'):
                    for j in range(0, 4):
                        loginElements.confirmButton(self).click()
                        globalData.LOG + generateLog.format_log('点击确定按钮')
                        loginElements.loginButton(self).click()
                        globalData.LOG += generateLog.format_log('点击登录按钮')
                try:
                    if(loginElements.popupText(self).get_attribute('name') == Data.getTestdata('login', i, 9)):
                        globalData.LOG += generateLog.format_log('弹框提示正确：' + Data.getTestdata('login', i, 9))
                        loginElements.confirmButton(self).click()
                        globalData.LOG += generateLog.format_log('点击确定')
                        Data.setExecutionresult(globalData.MODULE, i, 'Pass')
                    else:
                        globalData.LOG += generateLog.format_log('弹框提示错误: ' + loginElements.popupText(self).get_attribute('name') )
                        Data.setExecutionresult(globalData.MODULE, i, 'Fail')
                except:
                    globalData.LOG += generateLog.format_log('弹框提示错误')
    except:
        globalData.LOG += generateLog.format_log('登录错误\n' + traceback.format_exc())

    #登录成功逻辑校验
    try:
        if(Data.getTestdata('login', i, 7) == 'Y'):
            if(tabElements.mineTab(self)):
                globalData.LOG += generateLog.format_log('登录成功')
                tabElements.mineTab(self).click()
                globalData.LOG += generateLog.format_log("点击'我的'选项卡")
                settingElements.settingButton(self).click()
                globalData.LOG += generateLog.format_log("点击设置按钮")
                settingElements.logoutButton(self).click()
                globalData.LOG += generateLog.format_log("点击退出登录")
                el = loginElements.loginPage(self)
                globalData.LOG += generateLog.format_log("成功退出")
                Data.setExecutionresult(globalData.MODULE, i, 'Pass')
            else:
                globalData.LOG += generateLog.format_log('注册成功页面显示错误')
                Data.setExecutionresult(globalData.MODULE, i, 'Fail')
        elif(Data.getTestdata('login', i, 7) == 'None'):
            globalData.LOG += generateLog.format_log('不对注册成功逻辑进行校验')
    except:
        globalData.LOG += generateLog.format_log('登录失败')
        Data.setExecutionresult(globalData.MODULE, i, 'Fail')

