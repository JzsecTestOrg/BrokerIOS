# -*- coding: utf-8 -*-
__author__ = 'xuwen'

import unittest, traceback
from TestCases import welcome, register
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
                for i in range(38, Data.getCasenumber('register') + 1):
                    globalData.LOG += generateLog.format_log('*******现在开始执行模块【register】的第【' + str(i) + '】条用例*******')
                    register.register(self, i)
                generateLog.generate_log()
                globalData.LOG = ''
            except:
                globalData.LOG += generateLog.format_log(traceback.format_exc())
                generateLog.generate_log()
                globalData.LOG = ''




def suite():
    RegisterTestSuite = unittest.makeSuite(Register, 'test')
    return RegisterTestSuite

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
        # runner.run(suite())
        screenShot.compareScreenshot()
        screenShot.mark_result()
        generateReport.generate_report()
    except:
        generateReport.generate_report()

