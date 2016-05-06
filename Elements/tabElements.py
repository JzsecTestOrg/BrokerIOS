# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

from CommonMethods import Data, globalData, generateLog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback

def customerTab(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('tab', 'customer', 'customerTab', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件customerTab未找到\n" + traceback.format_exc())
    

def followTab(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('tab', 'follow', 'followTab', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件followTab未找到\n" + traceback.format_exc())
    

def recommendTab(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('tab', 'recommend', 'recommendTab', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件recommendTab未找到\n" + traceback.format_exc())
    

def mineTab(self):
    try:
        el = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('tab', 'mine', 'mineTab', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件mineTab未找到\n" + traceback.format_exc())
    


