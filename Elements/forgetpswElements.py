# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

import sys
from appium import webdriver
from CommonMethods import Data, globalData, generateLog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback


def fetchpasswordPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('forgetpassword', 'forgetpassword', 'fetchpasswordPage', 1))))        
        return el
    except:
        globalData.LOG += generateLog.format_log("控件fetchpasswordPage未找到\n" + traceback.format_exc())
        

def phoneText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('forgetpassword', 'forgetpassword', 'phoneText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件phoneText未找到\n" + traceback.format_exc())
    

def vercodeButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('forgetpassword', 'forgetpassword', 'vercodeButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件vercodeButton未找到\n" + traceback.format_exc())
    

def vercodeText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('forgetpassword', 'forgetpassword', 'vercodeText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件vercodeText未找到\n" + traceback.format_exc())
    

def cipherpasswordText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('forgetpassword', 'forgetpassword', 'cipherpasswordText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件cipherpasswordText未找到\n" + traceback.format_exc())
    


def confirmButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('forgetpassword', 'forgetpassword', 'confirmButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件confirmButton未找到\n" + traceback.format_exc())
    


def backButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('forgetpassword', 'forgetpassword', 'backButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件backButton未找到\n" + traceback.format_exc())


def popupText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('forgetpassword', 'forgetpassword', 'popupText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件popupText未找到\n" + traceback.format_exc())

def findButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('forgetpassword', 'forgetpassword', 'findButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件findButton未找到\n" + traceback.format_exc())

def plainpasswordText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('forgetpassword', 'forgetpassword', 'plainpasswordText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件plainpasswordText未找到\n" + traceback.format_exc())

def eyecloseButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('forgetpassword', 'forgetpassword', 'eyecloseButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件eyecloseButton未找到\n" + traceback.format_exc())

def eyeopenButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('forgetpassword', 'forgetpassword', 'eyeopenButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件eyeopenButton未找到\n" + traceback.format_exc())




