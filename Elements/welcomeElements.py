# -*- coding: UTF-8 -*-
__author__ = 'xuwen'


from CommonMethods import globalData, generateLog, relatedTime, Data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback




def versionUpdate_alert(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, Data.getXpath('welcome', 'welcome', 'versionUpdate_alert', '1'))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件versionUpdate_alert未找到\n" + traceback.format_exc())



def versionUpdate_cancel(self):
    try:
        el = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('welcome', 'welcome', 'versionUpdate_cancel', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件versionUpdate_cancel未找到\n" + traceback.format_exc())



def welcomePage(self):
    try:
        el = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('welcome', 'welcome', 'welcomePage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件welcomePage未找到\n" + traceback.format_exc())



def welcome_register(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('welcome', 'welcome', 'welcome_register', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件welcome_register未找到\n" + traceback.format_exc())


def welcome_login(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('welcome', 'welcome', 'welcome_login', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件welcome_login未找到\n" + traceback.format_exc())

def phone(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('welcome', 'welcome', 'phone', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件phone未找到\n" + traceback.format_exc())

def timeoutButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('welcome', 'welcome', 'timeoutButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件timeoutButton未找到\n" + traceback.format_exc())


def welcome_title(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('welcome', 'welcome', 'welcome_title', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件welcome_title未找到\n" + traceback.format_exc())


