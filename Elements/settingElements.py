# -*- coding: UTF-8 -*-
__author__ = 'xuwen'


from CommonMethods import Data, globalData, generateLog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback

def settingButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'mine', 'settingButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件settingButton未找到\n" + traceback.format_exc())
    


def resetpswButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'setting', 'resetpswButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件resetpswButton未找到\n" + traceback.format_exc())
    


def logoutButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'setting', 'logoutButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件logoutButton未找到\n" + traceback.format_exc())
    


def resetPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'reset', 'resetPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件resetPage未找到\n" + traceback.format_exc())
    


def phoneText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'reset', 'phoneText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件phoneText未找到\n" + traceback.format_exc())
    


def vercodeText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'reset', 'vercodeText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件vercodeText未找到\n" + traceback.format_exc())
    


def vercodeButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'reset', 'vercodeButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件vercodeButton未找到\n" + traceback.format_exc())
    


def newpasswordText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'reset', 'newpasswordText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件newpasswordText未找到\n" + traceback.format_exc())
    


def confirmButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'reset', 'confirmButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件confirmButton未找到\n" + traceback.format_exc())


def feedbackButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'setting', 'feedbackButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件feedbackButton未找到\n" + traceback.format_exc())


def feedbackPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'feedback', 'feedbackPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件feedbackPage未找到\n" + traceback.format_exc())


def feedbackText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'feedback', 'feedbackText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件feedbackText未找到\n" + traceback.format_exc())


def feedbackcountText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'feedback', 'feedbackcountText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件feedbackcountText未找到\n" + traceback.format_exc())


def feedbackcommitButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('setting', 'feedback', 'feedbackcommitButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件feedbackcommitButton未找到\n" + traceback.format_exc())



















