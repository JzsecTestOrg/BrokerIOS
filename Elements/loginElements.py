# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

from CommonMethods import globalData, Data, generateLog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback


def loginPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('login', 'login', 'loginPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件loginPage未找到\n" + traceback.format_exc())
    


def usernameText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('login', 'login', 'usernameText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件usernameText未找到\n" + traceback.format_exc())
    


def passwordSecureText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('login', 'login', 'passwordSecureText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件passwordSecureText未找到\n" + traceback.format_exc())
    

def passwordText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('login', 'login', 'passwordText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件passwordText未找到\n" + traceback.format_exc())


def eyecloseButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('login', 'login', 'eyecloseButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件eyecloseButton未找到\n" + traceback.format_exc())


def eyeopenButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('login', 'login', 'eyeopenButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件eyeopenButton未找到\n" + traceback.format_exc())
    


def cantseeButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('login', 'login', 'cantseeButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件cantseeButton未找到\n" + traceback.format_exc())
    


def canseeButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('login', 'login', 'canseeButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件canseeButton未找到\n" + traceback.format_exc())
    


def forgetpawLink(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, Data.getXpath('login', 'login', 'forgetpawLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件forgetpawLink未找到\n" + traceback.format_exc())
    

def loginButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('login', 'login', 'loginButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件loginButton未找到\n" + traceback.format_exc())
    

def gothroughButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('login', 'login', 'gothroughButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件gothroughButton未找到\n" + traceback.format_exc())
    

def congratuationPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('login', 'login', 'congratuationPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件congratuationPage未找到\n" + traceback.format_exc())

def registerButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('login', 'login', 'registerButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件registerButton未找到\n" + traceback.format_exc())
    



