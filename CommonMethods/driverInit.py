# -*- coding: utf-8 -*-
__author__ = 'xuwen'

from selenium import webdriver
import globalData, generateLog
import traceback
import os

def deviceSetup(self):
    try:
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': 'com.jzsec.kingbroker',
                'platformName': 'iOS',
                'platformVersion': '8.4',
                'deviceName': 'iPhone 6 Plus'
            })
        globalData.LOG += generateLog.format_log("真机启动成功")
    except Exception, e:
        globalData.LOG += generateLog.format_log("真机启动失败\n" + traceback.format_exc())


def simulatorSetup(self):
    app = os.path.join(os.path.dirname(__file__),
                           '/Users/xuwen1/Library/Developer/Xcode/DerivedData/Broker-ayelcthmulepmvdjzbhmvncvqjmz/Build/Products/Debug-iphoneos',
                           'Broker.app')
    app = os.path.abspath(app)
    try:
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '8.1',
                'deviceName': 'iPhone 6'
            })
        globalData.LOG += generateLog.format_log("模拟器启动成功")
    except Exception, e:
        globalData.LOG += generateLog.format_log("模拟器启动失败\n" + traceback.format_exc())









