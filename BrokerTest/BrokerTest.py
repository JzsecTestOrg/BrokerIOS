# -*- coding: utf-8 -*-
__author__ = 'xuwen'

import unittest, traceback
from TestCases import welcome, register, login, logout
from CommonMethods import generateLog, globalData, checkMail, Data, driverInit, driverQuit, dataBase, generateReport, screenShot



class Register(unittest.TestCase):
    def setUp(self):
        globalData.MODULE = 'init'
        driverInit.deviceSetup(self)


    def tearDown(self):
        driverQuit.driverQuit(self)


    def test_register(self):
        module_init('register')
        globalData.MODULE = 'welcome'
        welcome.welcome(self, 'login')
        globalData.MODULE = 'register'
        try:
            for i in range(1, Data.getCasenumber('register') + 1):
                globalData.LOG += generateLog.format_log('*******现在开始执行模块【register】的第【' + str(i) + '】条用例*******')
                register.register(self, i)
            generateLog.generate_log()
            globalData.LOG = ''
        except:
            globalData.LOG += generateLog.format_log(traceback.format_exc())
            generateLog.generate_log()
            globalData.LOG = ''

class Login(unittest.TestCase):
    def setUp(self):
        globalData.MODULE = 'init'
        driverInit.deviceSetup(self)


    def tearDown(self):
        driverQuit.driverQuit(self)


    def test_login(self):
        module_init('login')
        globalData.MODULE = 'welcome'
        welcome.welcome(self, 'login')
        globalData.MODULE = 'login'
        try:
            for i in range(20, Data.getCasenumber('login') + 1):
                globalData.LOG += generateLog.format_log('*******现在开始执行模块【login】的第【' + str(i) + '】条用例*******')
                login.login(self, i)
            generateLog.generate_log()
            globalData.LOG = ''
        except:
            globalData.LOG += generateLog.format_log(traceback.format_exc())
            generateLog.generate_log()
            globalData.LOG = ''

class Logout(unittest.TestCase):
    def setUp(self):
        globalData.MODULE = 'init'
        driverInit.deviceSetup(self)


    def tearDown(self):
        driverQuit.driverQuit(self)


    def test_logout(self):
        module_init('logout')
        globalData.MODULE = 'logout'
        try:
            for i in range(1, Data.getCasenumber('logout') + 1):
                globalData.LOG += generateLog.format_log('*******现在开始执行模块【logout】的第【' + str(i) + '】条用例*******')
                logout.logout(self, i)
            generateLog.generate_log()
            globalData.LOG = ''
        except:
            globalData.LOG += generateLog.format_log(traceback.format_exc())
            generateLog.generate_log()
            globalData.LOG = ''



def suite():
    RegisterTestSuite = unittest.makeSuite(Register, 'test')
    LoginTestSuite = unittest.makeSuite(Login, 'test')
    LogoutTestSuite = unittest.makeSuite(Logout, 'test')
    return RegisterTestSuite, LoginTestSuite, LogoutTestSuite

def module_init(module):
    result = []
    for i in range(Data.getCasenumber(module)):
        result.append('Not Executed')
    result_dict = {module: result}
    globalData.EXECUTED.append(result_dict)
    for i in range(0, len(globalData.EXECUTED)):
        print globalData.EXECUTED[i].keys()
        print globalData.EXECUTED[i].values()




def log():
    generateLog.generate_log()



if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    #注册
    try:
        runner.run(suite()[2])
        # screenShot.compareScreenshot()
        # screenShot.mark_result()
        generateReport.generate_report()
    except:
        generateReport.generate_report()

