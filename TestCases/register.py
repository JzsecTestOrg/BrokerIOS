# -*- coding: utf-8 -*-
__author__ = 'xuwen'


import time, sys, traceback
from Elements import registerElements, loginElements, tabElements, mineElements, settingElements, welcomeElements
from CommonMethods import redis, globalData, generateLog, Data, userStatus, dataBase, screenShot



def register_smoking(self, phone, password, nickname):
    reload(sys)
    sys.setdefaultencoding('utf-8')

    #注册页面手机号验证
    try:
        registerElements.phoneText(self).send_keys(str(phone))
        globalData.LOG += generateLog.format_log("输入注册手机号: " + str(phone))
    except Exception, e:
        globalData.LOG += generateLog.format_log("注册页面手机号输入框错误\n" + traceback.format_exc())

    #注册页面发送验证码验证
    try:
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
    except Exception, e:
        globalData.LOG += generateLog.format_log("按钮发送验证码识别错误\n" + traceback.format_exc())
    time.sleep(5)
    code = redis.registerVercode(str(phone))

    try:
        registerElements.vercodeText(self).send_keys(code)
        globalData.LOG += generateLog.format_log("输入验证码: " + code)
    except Exception, e:
        globalData.LOG += generateLog.format_log("注册页面验证码输入框错误\n" + traceback.format_exc())

    try:
        registerElements.pswfirstSecureText(self).send_keys(str(password))
        globalData.LOG += generateLog.format_log("输入注册密码: " + str(password))
    except Exception, e:
        globalData.LOG += generateLog.format_log("注册页面密码输入框错误\n" + traceback.format_exc())

    #注册昵称验证
    try:
        registerElements.nicknameText(self).send_keys(unicode(str(nickname), 'utf-8'))
        globalData.LOG += generateLog.format_log("输入昵称: " + Data.getValue('register', 'register', 'nicknameText', 1))
    except Exception, e:
        globalData.LOG += generateLog.format_log("注册页面昵称输入框错误\n" + traceback.format_exc())

    #注册页面注册按钮验证
    try:
        registerElements.registerButton(self).click()
        globalData.LOG += generateLog.format_log("点击注册按钮")
    except Exception, e:
        globalData.LOG += generateLog.format_log("注册页面注册按钮错误\n" + traceback.format_exc())

    #验证注册成功
    try:
        el = tabElements.customerTab(self)
        globalData.LOG += generateLog.format_log("注册完成页面正确显示")
    except Exception, e:
        globalData.LOG += generateLog.format_log("注册完成页面未显示\n" + traceback.format_exc())


def register(self, i):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    #构造前置条件：注册过的手机号，未注册过的手机号
    if(Data.getPrecondition('register', i) == '注册过的手机号'):
        if(userStatus.isRegisterSuccess(Data.getTestdata('register', i, 2)) == False):
            dataBase.insert_buser(Data.getTestdata('register', i, 2))
    else:
        if(userStatus.isRegisterSuccess(Data.getTestdata('register', i, 2)) == True):
            dataBase.del_buser(Data.getTestdata('register', i, 2))
    redis.clear_vercode(Data.getTestdata('register', i, 2))


    #进入注册页面校验
    try:
        if(loginElements.loginPage(self)):
            globalData.LOG += generateLog.format_log('登录页面正确显示')
            loginElements.registerButton(self).click()
            globalData.LOG += generateLog.format_log('点击注册按钮')
            if(registerElements.registerPage(self)):
                globalData.LOG += generateLog.format_log('注册页面正确显示')
    except:
        if(registerElements.registerPage(self)):
            globalData.LOG += generateLog.format_log('注册页面正确显示')

    #处理注册手机号逻辑
    registerElements.phoneText(self).clear()
    if(len(Data.getTestdata('register', i, 2)) > 11):
        registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2)[0:11])
        registerElements.phoneText(self).click()
        registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2)[11:len(Data.getTestdata('register', i, 2))])
    else:
        registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
    globalData.LOG += generateLog.format_log('输入手机号：' + Data.getTestdata('register', i, 2))

    #处理验证码逻辑
    if(Data.getTestdata('register', i, 3) == 'None'):
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log('点击发送验证码')
        if(Data.getTestdata('register', i, 13) == '1'):
            screenShot.get_screenshot(self, i)
        elif(Data.getTestdata('register', i, 13) == '2'):
            try:
                if(registerElements.popupText(self).get_attribute('name') == Data.getTestdata('register', i, 14)):
                    globalData.LOG += generateLog.format_log('提示正确：' + Data.getTestdata('register', i, 14))
                    registerElements.confirmButton(self).click()
                    globalData.LOG += generateLog.format_log('点击确定')
                    Data.setExecutionresult(globalData.MODULE, i, 'Pass')
                else:
                    globalData.LOG += generateLog.format_log('提示错误:' + registerElements.popupText(self).get_attribute('name'))
                    registerElements.confirmButton(self).click()
                    globalData.LOG += generateLog.format_log('点击确定')
                    Data.setExecutionresult(globalData.MODULE, i, 'Fail')
            except:
                    globalData.LOG += generateLog.format_log('手机号提示错误')
        globalData.LOG += generateLog.format_log('不对验证码进行校验')
    elif(Data.getTestdata('register', i, 3) == 'Y'):
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        time.sleep(10)
        globalData.LOG += generateLog.format_log('验证码发送成功！')
        code = redis.registerVercode(Data.getTestdata('register', i, 2))
        registerElements.vercodeText(self).send_keys(code)
        globalData.LOG += generateLog.format_log("输入验证码: " + code)
    elif(Data.getTestdata('register', i, 15) == '6位错误的验证码'):
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        time.sleep(10)
        globalData.LOG += generateLog.format_log('验证码发送成功！')
        code = '111111'
        registerElements.vercodeText(self).send_keys(code)
        globalData.LOG += generateLog.format_log("输入错误验证码: " + code)
    elif(Data.getTestdata('register', i, 15) == '6位过期的验证码'):
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        time.sleep(10)
        globalData.LOG += generateLog.format_log('验证码发送成功！')
        code = redis.registerVercode(Data.getTestdata('register', i, 2))
        redis.expireregisterVercode(Data.getTestdata('register', i, 2))
        registerElements.vercodeText(self).send_keys(code)
        globalData.LOG += generateLog.format_log("输入验证码: " + code)
    elif(Data.getTestdata('register', i, 15) == '使用过的验证码'):
        registerElements.phoneText(self).clear()
        registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
        globalData.LOG += generateLog.format_log('输入手机号：' + Data.getTestdata('register', i, 2))
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        time.sleep(10)
        globalData.LOG += generateLog.format_log('验证码发送成功！')
        code = redis.registerVercode(Data.getTestdata('register', i, 2))
        registerElements.vercodeText(self).send_keys(code)
        globalData.LOG += generateLog.format_log("输入验证码: " + code)
        registerElements.cipherpasswordText(self).send_keys(Data.getTestdata('register', i, 4))
        globalData.LOG += generateLog.format_log('输入密码：' + Data.getTestdata('register', i, 4))
        registerElements.nicknameText(self).send_keys(Data.getTestdata('register', i, 6))
        globalData.LOG += generateLog.format_log('输入昵称：' + Data.getTestdata('register', i, 6))
        registerElements.registerButton(self).click()
        globalData.LOG += generateLog.format_log('点击‘立即注册’')
        tabElements.mineTab(self).click()
        globalData.LOG += generateLog.format_log("点击'我的'选项卡")
        settingElements.settingButton(self).click()
        globalData.LOG += generateLog.format_log("点击设置按钮")
        settingElements.logoutButton(self).click()
        globalData.LOG += generateLog.format_log("点击退出登录")
        if(loginElements.loginPage(self)):
            globalData.LOG += generateLog.format_log("成功退出")
        dataBase.del_buser(Data.getTestdata('register', i, 2))
        loginElements.registerButton(self).click()
        globalData.LOG += generateLog.format_log('登录页面点击注册按钮')
        registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
        globalData.LOG += generateLog.format_log('输入手机号：' + Data.getTestdata('register', i, 2))
        redis.expireregisterVercode(Data.getTestdata('register', i, 2))
        registerElements.vercodeText(self).send_keys(code)
        globalData.LOG += generateLog.format_log('输入已经用过的验证码：' + code)
    elif(Data.getTestdata('register', i, 15) == '超过60s重新触发发送验证码'):
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        if(registerElements.vercodeButton(self).get_attribute('name') != '发送验证码'):
            globalData.LOG += generateLog.format_log('验证码发送过程发送验证码按钮文案显示正确')
        else:
            globalData.LOG += generateLog.format_log('验证码发送过程发送验证码按钮文案显示错误:' + registerElements.vercodeButton(self).get_attribute('text'))
        time.sleep(60)
        globalData.LOG += generateLog.format_log('等待60s')
        if(registerElements.vercodeButton(self).get_attribute('name') == '重新发送'):
            globalData.LOG += generateLog.format_log('验证码发送完成60s后发送验证码按钮文案显示正确：重新发送')
        else:
            globalData.LOG += generateLog.format_log('验证码发送完成60s后发送验证码按钮文案显示错误：' + registerElements.vercodeButton(self).get_attribute('name'))
        redis.clear_vercode(Data.getNumber('register', 'register', 'phoneText', i))
        globalData.LOG += generateLog.format_log('清除redis验证码缓存')
        registerElements.vercodeButton(self).click()
        globalData.LOG += generateLog.format_log("验证码发送中...")
        time.sleep(10)
        globalData.LOG += generateLog.format_log('验证码发送成功！')
    else:
        registerElements.vercodeText(self).clear()
        registerElements.vercodeText(self).send_keys(Data.getTestdata('register', i, 3))
        globalData.LOG += generateLog.format_log("输入验证码: " + Data.getTestdata('register', i, 3))

    #处理注册密码逻辑
    if(Data.getTestdata('register', i, 4) == 'None'):
        globalData.LOG += generateLog.format_log('不对密码进行校验')
    else:
        registerElements.passwordText(self).send_keys(Data.getTestdata('register', i, 4))
        globalData.LOG += generateLog.format_log('输入密码：' + Data.getTestdata('register', i, 4))


    #处理密码明暗文逻辑
    if(Data.getTestdata('register', i, 5) == 'None'):
        globalData.LOG += generateLog.format_log('不对密码明暗文进行校验')
    elif(Data.getTestdata('register', i, 5) == 'Y'):
        if('•' in registerElements.cipherpasswordText(self).get_attribute('value')):
            globalData.LOG += generateLog.format_log('密码显示正确：暗文')
        else:
            globalData.LOG += generateLog.format_log('密码显示错误：明文')
        registerElements.eyecloseButton(self).click()
        globalData.LOG += generateLog.format_log("切换密码为明文")
        if('•'  not in registerElements.plainpasswordText(self).get_attribute('value')):
            globalData.LOG += generateLog.format_log('密码显示正确：明文')
        else:
            globalData.LOG += generateLog.format_log('密码显示错误：暗文')
        registerElements.eyeopenButton(self).click()
        globalData.LOG += generateLog.format_log("切换密码为暗文")
        if('•' in registerElements.cipherpasswordText(self).get_attribute('value')):
            globalData.LOG += generateLog.format_log('密码显示正确：暗文')
        else:
            globalData.LOG += generateLog.format_log('密码显示错误：明文')

    #处理昵称逻辑
    try:
        if(Data.getTestdata('register', i, 6) == 'None'):
            globalData.LOG += generateLog.format_log('不对昵称进行校验')
        else:
            registerElements.nicknameText(self).clear()
            registerElements.nicknameText(self).send_keys(Data.getTestdata('register', i, 6))
            globalData.LOG += generateLog.format_log("输入昵称: " + Data.getTestdata('register', i, 6))
    except:
        screenShot.get_screenshot(self, i)
        globalData.LOG += generateLog.format_log('输入的昵称报错')

    #处理邀请码逻辑
    if(Data.getTestdata('register', i, 7) == 'None'):
        globalData.LOG += generateLog.format_log('不对邀请码进行校验')
    elif(Data.getTestdata('register', i, 7) == 'Y'):
        if(Data.getTestdata('register', i, 15) == '邀请码为空'):
            registerElements.invitecodeText(self).clear()
            globalData.LOG += generateLog.format_log('清空邀请码')
        elif(Data.getTestdata('register', i, 15) == '默认个人邀请码'):
            invite_code = dataBase.invite_code('12300000000', Data.getTestdata('register', i, 2), 1)
            registerElements.phoneText(self).clear()
            registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
            if(registerElements.invitecodeText(self).get_attribute('value') == invite_code):
                globalData.LOG += generateLog.format_log('个人邀请码预填正确：' + invite_code)
            else:
                globalData.LOG += generateLog.format_log('个人邀请码预填错误：' + registerElements.invitecodeText(self).get_attribute('value'))
        elif(Data.getTestdata('register', i, 15) == '默认机构邀请码'):
            invite_code = dataBase.invite_code('12300000001', Data.getTestdata('register', i, 2), 2)
            registerElements.phoneText(self).clear()
            registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
            if(registerElements.invitecodeText(self).get_attribute('value') == invite_code):
                globalData.LOG += generateLog.format_log('机构邀请码预填正确：' + invite_code)
            else:
                globalData.LOG += generateLog.format_log('机构邀请码预填错误：' + registerElements.invitecodeText(self).get_attribute('value'))
        elif(Data.getTestdata('register', i, 15) == '个人改成其他个人邀请码'):
            invite_code1 = dataBase.invite_code('12300000002', Data.getTestdata('register', i, 2), 1)
            invite_code2 = dataBase.invite_code('12300000003', Data.getTestdata('register', i, 2), 1)
            registerElements.phoneText(self).clear()
            registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
            if(registerElements.invitecodeText(self).get_attribute('value') == invite_code1):
                globalData.LOG += generateLog.format_log('个人邀请码预填正确：' + invite_code1)
            else:
                globalData.LOG += generateLog.format_log('个人邀请码预填错误：' + registerElements.invitecodeText(self).get_attribute('value'))
            registerElements.invitecodeText(self).clear()
            globalData.LOG += generateLog.format_log('清除邀请码')
            registerElements.invitecodeText(self).send_keys(invite_code2)
            globalData.LOG += generateLog.format_log('输入新的个人邀请码：' + invite_code2)
        elif(Data.getTestdata('register', i, 15) == '机构改成其他机构邀请码'):
            invite_code1 = dataBase.invite_code('12300000004', Data.getTestdata('register', i, 2), 2)
            invite_code2 = dataBase.invite_code('12300000005', Data.getTestdata('register', i, 2), 3)
            registerElements.phoneText(self).clear()
            registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
            if(registerElements.invitecodeText(self).get_attribute('value') == invite_code1):
                globalData.LOG += generateLog.format_log('机构邀请码预填正确：' + invite_code1)
            else:
                globalData.LOG += generateLog.format_log('机构邀请码预填错误：' + registerElements.invitecodeText(self).get_attribute('value'))
            registerElements.invitecodeText(self).clear()
            globalData.LOG += generateLog.format_log('清除邀请码')
            registerElements.invitecodeText(self).send_keys(invite_code2)
            globalData.LOG += generateLog.format_log('输入新的机构邀请码：' + invite_code2)
        elif(Data.getTestdata('register', i, 15) == '清除邀请码注册'):
            invite_code = dataBase.invite_code('12300000006', Data.getTestdata('register', i, 2), 1)
            registerElements.phoneText(self).clear()
            registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
            if(registerElements.invitecodeText(self).get_attribute('value') == invite_code):
                globalData.LOG += generateLog.format_log('个人邀请码预填正确：' + invite_code)
            else:
                globalData.LOG += generateLog.format_log('个人邀请码预填错误：' + registerElements.invitecodeText(self).get_attribute('value'))
            registerElements.invitecodeText(self).clear()
            globalData.LOG += generateLog.format_log('清除预填的邀请码')
    elif(Data.getTestdata('register', i, 7) == 'N'):
        if(Data.getTestdata('register', i, 15) == '邀请码不存在'):
            invite_code = '1111'
            registerElements.invitecodeText(self).clear()
            registerElements.invitecodeText(self).send_keys(invite_code)
            globalData.LOG += generateLog.format_log('输入不存在的邀请码：' + invite_code)
        elif(Data.getTestdata('register', i, 15) == 'Capp邀请码'):
            invite_code = dataBase.invite_code('12300000007', Data.getTestdata('register', i, 2), 4)
            registerElements.invitecodeText(self).clear()
            registerElements.invitecodeText(self).send_keys(invite_code)
            globalData.LOG += generateLog.format_log('输入Capp邀请码：' + invite_code)
        elif(Data.getTestdata('register', i, 15) == '个人邀请码改成Capp邀请码'):
            invite_code1 = dataBase.invite_code('12300000008', Data.getTestdata('register', i, 2), 1)
            invite_code2 = dataBase.invite_code('12300000009', Data.getTestdata('register', i, 2), 4)
            registerElements.phoneText(self).clear()
            registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
            if(registerElements.invitecodeText(self).get_attribute('value') == invite_code1):
                globalData.LOG += generateLog.format_log('个人邀请码预填正确：' + invite_code1)
            else:
                globalData.LOG += generateLog.format_log('个人邀请码预填错误：' + registerElements.invitecodeText(self).get_attribute('value'))
            registerElements.invitecodeText(self).clear()
            globalData.LOG += generateLog.format_log('清除邀请码')
            registerElements.invitecodeText(self).send_keys(invite_code2)
            globalData.LOG += generateLog.format_log('输入Capp邀请码：' + invite_code2)
        elif(Data.getTestdata('register', i, 15) == '个人邀请码改成不存在的邀请码'):
            invite_code1 = dataBase.invite_code('12300000010', Data.getTestdata('register', i, 2), 1)
            invite_code2 = '1111'
            registerElements.phoneText(self).clear()
            registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
            if(registerElements.invitecodeText(self).get_attribute('value') == invite_code1):
                globalData.LOG += generateLog.format_log('个人邀请码预填正确：' + invite_code1)
            else:
                globalData.LOG += generateLog.format_log('个人邀请码预填错误：' + registerElements.invitecodeText(self).get_attribute('value'))
            registerElements.invitecodeText(self).clear()
            globalData.LOG += generateLog.format_log('清除邀请码')
            registerElements.invitecodeText(self).send_keys(invite_code2)
            globalData.LOG += generateLog.format_log('输入不存在的邀请码：' + invite_code2)
        elif(Data.getTestdata('register', i, 15) == '个人邀请码改成机构邀请码'):
            invite_code1 = dataBase.invite_code('12300000011', Data.getTestdata('register', i, 2), 1)
            invite_code2 = dataBase.invite_code('12300000012', Data.getTestdata('register', i, 2), 2)
            registerElements.phoneText(self).clear()
            registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
            if(registerElements.invitecodeText(self).get_attribute('value') == invite_code1):
                globalData.LOG += generateLog.format_log('个人邀请码预填正确：' + invite_code1)
            else:
                globalData.LOG += generateLog.format_log('个人邀请码预填错误：' + registerElements.invitecodeText(self).get_attribute('value'))
            registerElements.invitecodeText(self).clear()
            globalData.LOG += generateLog.format_log('清除邀请码')
            registerElements.invitecodeText(self).send_keys(invite_code2)
            globalData.LOG += generateLog.format_log('输入机构邀请码：' + invite_code2)
        elif(Data.getTestdata('register', i, 15) == '机构邀请码改成Capp邀请码'):
            invite_code1 = dataBase.invite_code('12300000013', Data.getTestdata('register', i, 2), 2)
            invite_code2 = dataBase.invite_code('12300000014', Data.getTestdata('register', i, 2), 4)
            registerElements.phoneText(self).clear()
            registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
            if(registerElements.invitecodeText(self).get_attribute('value') == invite_code1):
                globalData.LOG += generateLog.format_log('机构邀请码预填正确：' + invite_code1)
            else:
                globalData.LOG += generateLog.format_log('机构邀请码预填错误：' + registerElements.invitecodeText(self).get_attribute('value'))
            registerElements.invitecodeText(self).clear()
            globalData.LOG += generateLog.format_log('清除邀请码')
            registerElements.invitecodeText(self).send_keys(invite_code2)
            globalData.LOG += generateLog.format_log('输入Capp邀请码：' + invite_code2)
        elif(Data.getTestdata('register', i, 15) == '机构邀请码改成不存在的邀请码'):
            invite_code1 = dataBase.invite_code('12300000015', Data.getTestdata('register', i, 2), 3)
            invite_code2 = '1111'
            registerElements.phoneText(self).clear()
            registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
            if(registerElements.invitecodeText(self).get_attribute('value') == invite_code1):
                globalData.LOG += generateLog.format_log('机构邀请码预填正确：' + invite_code1)
            else:
                globalData.LOG += generateLog.format_log('机构邀请码预填错误：' + registerElements.invitecodeText(self).get_attribute('value'))
            registerElements.invitecodeText(self).clear()
            globalData.LOG += generateLog.format_log('清除邀请码')
            registerElements.invitecodeText(self).send_keys(invite_code2)
            globalData.LOG += generateLog.format_log('输入不存在的邀请码：' + invite_code2)
        elif(Data.getTestdata('register', i, 15) == '机构邀请码改成个人邀请码'):
            invite_code1 = dataBase.invite_code('12300000016', Data.getTestdata('register', i, 2), 2)
            invite_code2 = dataBase.invite_code('12300000017', Data.getTestdata('register', i, 2), 1)
            registerElements.phoneText(self).clear()
            registerElements.phoneText(self).send_keys(Data.getTestdata('register', i, 2))
            if(registerElements.invitecodeText(self).get_attribute('value') == invite_code1):
                globalData.LOG += generateLog.format_log('机构邀请码预填正确：' + invite_code1)
            else:
                globalData.LOG += generateLog.format_log('机构邀请码预填错误：' + registerElements.invitecodeText(self).get_attribute('value'))
            registerElements.invitecodeText(self).clear()
            globalData.LOG += generateLog.format_log('清除邀请码')
            registerElements.invitecodeText(self).send_keys(invite_code2)
            globalData.LOG += generateLog.format_log('输入个人邀请码：' + invite_code2)


    #处理经纪宝注册协议勾选逻辑
    if(Data.getTestdata('register', i, 8) == 'None'):
        globalData.LOG += generateLog.format_log('不对经纪宝注册协议勾选进行校验')
    elif(Data.getTestdata('register', i, 8) == 'Y'):
        if(registerElements.protocolCheckbox(self, 1)):
            globalData.LOG += generateLog.format_log('《经纪宝注册协议》默认勾选')
        else:
            globalData.LOG += generateLog.format_log('《经纪宝注册协议》默认未勾选错误')
        registerElements.protocolCheckbox(self, 1).click()
        globalData.LOG += generateLog.format_log("不勾选《经纪宝注册协议》")
        registerElements.protocolCheckbox(self, 2).click()
        globalData.LOG += generateLog.format_log("勾选《经纪宝注册协议》")
        if(registerElements.protocolCheckbox(self, 1)):
            globalData.LOG += generateLog.format_log('《经纪宝注册协议》已勾选')
        else:
            globalData.LOG += generateLog.format_log('《经纪宝注册协议》未勾选错误')
    else:
        if(registerElements.protocolCheckbox(self, 1)):
            globalData.LOG += generateLog.format_log('《经纪宝注册协议》默认勾选')
        else:
            globalData.LOG += generateLog.format_log('《经纪宝注册协议》默认未勾选错误')
        registerElements.protocolCheckbox(self, 1).click()
        globalData.LOG += generateLog.format_log('不勾选《经纪宝注册协议》')


    #处理经纪宝注册协议内容逻辑
    if(Data.getTestdata('register', i, 8) == 'None'):
        globalData.LOG += generateLog.format_log('不对经纪宝注册协议内容校验')
    elif(Data.getTestdata('register', i, 8) == 'Y'):
        registerElements.protocolLink(self).click()
        globalData.LOG += generateLog.format_log('点击《经纪宝注册协议》')
        if(registerElements.protocolPage(self)):
            globalData.LOG += generateLog.format_log('《经纪宝注册协议》页面显示正确')
        else:
            globalData.LOG += generateLog.format_log('《经纪宝注册协议》页面显示错误')
        if(registerElements.protocolText(self)):
            globalData.LOG += generateLog.format_log('《经纪宝注册协议》内容显示正确')
        else:
            globalData.LOG += generateLog.format_log('《经纪宝注册协议》内容显示错误')
        registerElements.backButton(self).click()
        globalData.LOG += generateLog.format_log('返回注册页面')

    #校验客服电话
    if(Data.getTestdata('register', i, 11) == 'None'):
        globalData.LOG += generateLog.format_log('不对注册页面的客服电话校验')
    elif(Data.getTestdata('register', i, 11) == 'Y'):
        try:
            el = registerElements.servicephoneText(self)
            globalData.LOG += generateLog.format_log('注册页面的客服电话显示正确')
        except:
            generateLog.format_log('注册页面的客服电话错误\n' + traceback.format_exc())

    #处理点击注册按钮逻辑
    if(Data.getTestdata('register', i, 10) == 'None'):
        globalData.LOG += generateLog.format_log('不对点击注册进行校验')
        registerElements.loginButton(self).click()
        globalData.LOG += generateLog.format_log('注册页面点击登录按钮')
    elif(Data.getTestdata('register', i, 10) == 'Y'):
        registerElements.registerButton(self).click()
        globalData.LOG += generateLog.format_log("点击注册按钮")
        if(Data.getTestdata('register', i, 13) == '1'):
            screenShot.get_screenshot(self, i)
            registerElements.loginButton(self).click()
            globalData.LOG += generateLog.format_log('注册页面点击登录按钮')
        elif(Data.getTestdata('register', i, 13) == '2'):
            try:
                if(registerElements.popupText(self).get_attribute('name') == Data.getTestdata('register', i, 14)):
                    globalData.LOG += generateLog.format_log('弹框提示正确：' + Data.getTestdata('register', i, 14))
                    try:
                        registerElements.cancelButton(self).click()
                        globalData.LOG += generateLog.format_log('点击取消')
                    except:
                        registerElements.confirmButton(self).click()
                        globalData.LOG += generateLog.format_log('点击确定')
                    Data.setExecutionresult(globalData.MODULE, i, 'Pass')
                else:
                    globalData.LOG += generateLog.format_log('弹框提示错误')
                    Data.setExecutionresult(globalData.MODULE, i, 'Fail')
                registerElements.loginButton(self).click()
                globalData.LOG += generateLog.format_log('注册页面点击登录按钮')
            except:
                globalData.LOG += generateLog.format_log('弹框提示错误')


    #处理注册成功校验逻辑
    if(Data.getTestdata('register', i, 12) == 'Y'):
        try:
            if(tabElements.mineTab(self)):
                globalData.LOG += generateLog.format_log('注册成功')
                tabElements.mineTab(self).click()
                globalData.LOG += generateLog.format_log("点击'我的'选项卡")
                if(Data.getTestdata('register', i, 13) == '3'):
                    mineElements.invitecodeLink(self).click()
                    globalData.LOG += generateLog.format_log('进入活动邀请码页面')
                    el = mineElements.invitecodeText(self)
                    globalData.LOG += generateLog.format_log('错误邀请码未显示')
                    mineElements.backButton(self).click()
                    globalData.LOG += generateLog.format_log('回到我的页面')
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
        except:
            globalData.LOG += generateLog.format_log('注册失败')
            Data.setExecutionresult(globalData.MODULE, i, 'Fail')
    elif(Data.getTestdata('register', i, 12) == 'None'):
        globalData.LOG += generateLog.format_log('不对注册成功逻辑进行校验')

