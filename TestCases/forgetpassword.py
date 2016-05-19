# -*- coding: utf-8 -*-
__author__ = 'xuwen'

import sys, traceback, time
from CommonMethods import Data, dataBase, userStatus, globalData, generateLog, screenShot, redis
import logout
from Elements import loginElements, forgetpswElements

def forgetpassword(self, i):
    reload(sys)
    sys.setdefaultencoding('utf-8')

    #构造前置条件：注册
    if(Data.getPrecondition('forgetpassword', i) != '未注册的手机号'):
        dataBase.insert_buser(Data.getTestdata('forgetpassword', i, 2))
        session = dataBase.db_session()
        session.execute("update b_user set password = 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb' where mobilephone = '" + Data.getTestdata('forgetpassword', i, 2) + "'")
        session.commit()
        oldpassword = dataBase.get_buser_password(Data.getTestdata('forgetpassword', i, 2))
    if(userStatus.isLoginSuccess(self) == True):
        logout.logout_smoking(self)
    redis.clear_vercode(Data.getTestdata('forgetpassword', i, 2))

    #进入忘记密码校验
    try:
        loginElements.forgetpswLink(self).click()
        if(forgetpswElements.fetchpasswordPage(self)):
            globalData.LOG += generateLog.format_log('忘记密码页面显示正确')
    except:
        globalData.LOG += generateLog.format_log('忘记密码页面显示错误\n' + traceback.format_exc())

    #处理手机号逻辑
    try:
        forgetpswElements.phoneText(self).clear()
        forgetpswElements.phoneText(self).send_keys(Data.getTestdata('forgetpassword', i, 2))
        globalData.LOG += generateLog.format_log('输入手机号：' + Data.getTestdata('forgetpassword', i, 2))
    except:
        globalData.LOG += generateLog.format_log('手机号错误\n' + traceback.format_exc())

    #处理验证码逻辑
    try:
        if(Data.getTestdata('forgetpassword', i, 3) == 'None'):
            forgetpswElements.vercodeButton(self).click()
            globalData.LOG += generateLog.format_log('点击发送验证码')
            if(Data.getTestdata('forgetpassword', i, 8) == '1'):
                screenShot.get_screenshot(self, i)
            elif(Data.getTestdata('forgetpassword', i, 8) == '2'):
                if(forgetpswElements.popupText(self).get_attribute('name') == Data.getTestdata('forgetpassword', i, 9)):
                    globalData.LOG += generateLog.format_log('提示正确：' + Data.getTestdata('forgetpassword', i, 9))
                    forgetpswElements.confirmButton(self).click()
                    globalData.LOG += generateLog.format_log('点击确定')
                    Data.setExecutionresult(globalData.MODULE, i, 'Pass')
                else:
                    globalData.LOG += generateLog.format_log('提示错误：' + forgetpswElements.popupText(self).get_attribute('name'))
                    forgetpswElements.confirmButton(self).click()
                    globalData.LOG += generateLog.format_log('点击确定')
                    Data.setExecutionresult(globalData.MODULE, i, 'Fail')
            globalData.LOG += generateLog.format_log('不对验证码进行校验')
        elif(Data.getTestdata('forgetpassword', i, 3) == 'Y'):
            forgetpswElements.vercodeButton(self).click()
            globalData.LOG += generateLog.format_log('验证码发送中...')
            time.sleep(3)
            globalData.LOG += generateLog.format_log('验证码发送成功！')
            code = redis.registerVercode(Data.getTestdata('forgetpassword', i, 2))
            forgetpswElements.vercodeText(self).send_keys(code)
            globalData.LOG += generateLog.format_log('输入验证码：' + code)
        elif(Data.getTestdata('forgetpassword', i, 10) == '6位错误的验证码'):
            forgetpswElements.vercodeButton(self).click()
            globalData.LOG += generateLog.format_log('验证码发送中...')
            time.sleep(3)
            globalData.LOG += generateLog.format_log('验证码发送成功！')
            code = '111111'
            forgetpswElements.vercodeText(self).send_keys(code)
            globalData.LOG += generateLog.format_log('输入错误验证码：' + code)
        elif(Data.getTestdata('forgetpassword', i, 10) == '6位过期的验证码'):
            forgetpswElements.vercodeButton(self).click()
            globalData.LOG += generateLog.format_log('验证码发送中...')
            time.sleep(3)
            globalData.LOG += generateLog.format_log('验证码发送成功！')
            code = redis.registerVercode(Data.getTestdata('forgetpassword', i, 2))
            redis.expireregisterVercode(Data.getTestdata('forgetpassword', i, 2))
            forgetpswElements.vercodeText(self).send_keys(code)
            globalData.LOG += generateLog.format_log('输入过期验证码：' + code)
        elif(Data.getTestdata('forgetpassword', i, 10) == '使用过的验证码'):
            forgetpswElements.vercodeButton(self).click()
            globalData.LOG += generateLog.format_log('验证码发送中...')
            time.sleep(3)
            globalData.LOG += generateLog.format_log('验证码发送成功！')
            code = redis.registerVercode(Data.getTestdata('forgetpassword', i, 2))
            forgetpswElements.vercodeText(self).send_keys(code)
            globalData.LOG += generateLog.format_log('输入验证码：' + code)
            forgetpswElements.cipherpasswordText(self).send_keys(Data.getTestdata('forgetpassword', i, 4))
            globalData.LOG += generateLog.format_log('输入密码：' + Data.getTestdata('forgetpassword', i, 4))
            forgetpswElements.findButton(self).click()
            globalData.LOG += generateLog.format_log('点击确定按钮，回到登录页面')
            loginElements.forgetpswLink(self).click()
            globalData.LOG += generateLog.format_log('点击忘记密码链接')
            forgetpswElements.phoneText(self).send_keys(Data.getTestdata('forgetpassword', i, 2))
            globalData.LOG += generateLog.format_log('输入手机号：' + Data.getTestdata('forgetpassword', i, 2))
            redis.expireregisterVercode(Data.getTestdata('forgetpassword', i, 2))
            forgetpswElements.vercodeText(self).send_keys(code)
            globalData.LOG += generateLog.format_log('输入使用过的验证码：' + code)
        elif(Data.getTestdata('forgetpassword', i, 10) == '超过60s重新触发发送验证码'):
            forgetpswElements.vercodeButton(self).click()
            globalData.LOG += generateLog.format_log('验证码发送中...')
            time.sleep(3)
            globalData.LOG += generateLog.format_log('验证码发送成功！')
            if(forgetpswElements.vercodeButton(self).get_attribute('name') != '发送验证码'):
                globalData.LOG += generateLog.format_log('验证码发送过程发送验证码按钮文案显示正确')
            else:
                globalData.LOG += generateLog.format_log('验证码发送过程发送验证码按钮文案显示错误:' + forgetpswElements.vercodeButton(self).get_attribute('text'))
            time.sleep(60)
            globalData.LOG += generateLog.format_log('等待60s')
            if(forgetpswElements.vercodeButton(self).get_attribute('name') == '重新发送'):
                globalData.LOG += generateLog.format_log('验证码发送过程发送验证码按钮文案显示正确')
                Data.setExecutionresult(globalData.MODULE, i, 'Pass')
            else:
                globalData.LOG += generateLog.format_log('验证码发送过程发送验证码按钮文案显示错误:' + forgetpswElements.vercodeButton(self).get_attribute('text'))
                Data.setExecutionresult(globalData.MODULE, i, 'Fail')
            redis.clear_vercode(Data.getNumber('register', 'register', 'phoneText', i))
            globalData.LOG += generateLog.format_log('清除redis验证码缓存')
            forgetpswElements.vercodeButton(self).click()
            globalData.LOG += generateLog.format_log("验证码发送中...")
            time.sleep(3)
            globalData.LOG += generateLog.format_log('验证码发送成功！')
        else:
            forgetpswElements.vercodeText(self).clear()
            forgetpswElements.vercodeText(self).send_keys(Data.getTestdata('forgetpassword', i, 3))
            globalData.LOG += generateLog.format_log('输入验证码：' + Data.getTestdata('forgetpassword', i, 3))
    except:
        globalData.LOG += generateLog.format_log('验证码错误\n' + traceback.format_exc())

    #处理密码逻辑
    try:
        if(Data.getTestdata('forgetpassword', i, 4) == 'None'):
            globalData.LOG += generateLog.format_log('不对密码进行校验')
        else:
            forgetpswElements.cipherpasswordText(self).send_keys(Data.getTestdata('forgetpassword', i, 4))
            globalData.LOG += generateLog.format_log('输入密码：' + Data.getTestdata('forgetpassword', i, 4))
    except:
        globalData.LOG += generateLog.format_log('密码错误\n' + traceback.format_exc())

    #处理密码明暗文逻辑
    try:
        if(Data.getTestdata('forgetpassword', i, 5) == 'None'):
            globalData.LOG += generateLog.format_log('不对密码明暗文进行校验')
        elif(Data.getTestdata('forgetpassword', i, 5) == 'Y'):
            if('•' in forgetpswElements.cipherpasswordText(self).get_attribute('value')):
                globalData.LOG += generateLog.format_log('密码显示正确：暗文')
            else:
                globalData.LOG += generateLog.format_log('密码显示错误：明文')
            forgetpswElements.eyecloseButton(self).click()
            globalData.LOG += generateLog.format_log("切换密码为明文")
            if('•'  not in forgetpswElements.plainpasswordText(self).get_attribute('value')):
                globalData.LOG += generateLog.format_log('密码显示正确：明文')
            else:
                globalData.LOG += generateLog.format_log('密码显示错误：暗文')
            forgetpswElements.eyeopenButton(self).click()
            globalData.LOG += generateLog.format_log("切换密码为暗文")
            if('•' in forgetpswElements.cipherpasswordText(self).get_attribute('value')):
                globalData.LOG += generateLog.format_log('密码显示正确：暗文')
            else:
                globalData.LOG += generateLog.format_log('密码显示错误：明文')
    except:
        globalData.LOG += generateLog.format_log('明暗文逻辑错误\n' + traceback.format_exc())


    #处理点击确定按钮逻辑
    try:
        if(Data.getTestdata('forgetpassword', i, 6) == 'None'):
            globalData.LOG += generateLog.format_log('不对点击确定进行校验')
            forgetpswElements.backButton(self).click()
            globalData.LOG += generateLog.format_log('忘记密码页面点击返回按钮')
        elif(Data.getTestdata('forgetpassword', i, 6) == 'Y'):
            forgetpswElements.findButton(self).click()
            globalData.LOG += generateLog.format_log("点击确定按钮")
            if(Data.getTestdata('forgetpassword', i, 8) == '1'):
                screenShot.get_screenshot(self, i)
                forgetpswElements.backButton(self).click()
                globalData.LOG += generateLog.format_log('忘记密码页面点击返回按钮')
            elif(Data.getTestdata('forgetpassword', i, 8) == '2'):
                    if(forgetpswElements.popupText(self).get_attribute('name') == Data.getTestdata('forgetpassword', i, 9)):
                        globalData.LOG += generateLog.format_log('弹框提示正确：' + Data.getTestdata('forgetpassword', i, 9))
                        forgetpswElements.confirmButton(self).click()
                        globalData.LOG += generateLog.format_log('点击确定')
                        Data.setExecutionresult(globalData.MODULE, i, 'Pass')
                    else:
                        globalData.LOG += generateLog.format_log('弹框提示错误')
                        Data.setExecutionresult(globalData.MODULE, i, 'Fail')
                    forgetpswElements.backButton(self).click()
                    globalData.LOG += generateLog.format_log('忘记密码页面点击返回按钮')
    except:
        globalData.LOG += generateLog.format_log('忘记密码\n' + traceback.format_exc())


    #处理忘记密码成功校验逻辑
    try:
        if(Data.getTestdata('forgetpassword', i, 7) == 'Y'):
            newpassword = dataBase.get_buser_password(Data.getTestdata('forgetpassword', i, 2))
            if(loginElements.loginPage(self) and oldpassword != newpassword):
                globalData.LOG += generateLog.format_log('忘记密码成功')
                Data.setExecutionresult(globalData.MODULE, i, 'Pass')
            else:
                globalData.LOG += generateLog.format_log('登录页面显示错误')
                Data.setExecutionresult(globalData.MODULE, i, 'Fail')
        elif(Data.getTestdata('forgetpassword', i, 7) == 'None'):
            globalData.LOG += generateLog.format_log('不对忘记密码成功逻辑进行校验')
    except:
            globalData.LOG += generateLog.format_log('忘记密码失败')
            Data.setExecutionresult(globalData.MODULE, i, 'Fail')
