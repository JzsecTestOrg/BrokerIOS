# -*- coding: UTF-8 -*-
__author__ = 'xuwen'


from CommonMethods import generateLog, globalData, Data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback


def phoneText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'phoneText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件phoneText未找到\n" + traceback.format_exc())
    


def vercodeButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'vercodeButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件vercodeButton未找到\n" + traceback.format_exc())
    


def vercodeText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'vercodeText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件vercodeText未找到\n" + traceback.format_exc())
    


def pswfirstText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'pswfirstText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件pswfirstText未找到\n" + traceback.format_exc())
    


def pswsecondText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'pswsecondText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件pswsecondText未找到\n" + traceback.format_exc())
    


def nicknameText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'nicknameText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件nicknameText未找到\n" + traceback.format_exc())
    


def protocolCheckbox(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'protocolCheckbox', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件protocolCheckbox未找到\n" + traceback.format_exc())
    


def protocolChecked(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'protocolChecked', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件protocolChecked未找到\n" + traceback.format_exc())
    


def protocolLink(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'protocolLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件protocolLink未找到\n" + traceback.format_exc())
    


def protocolPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'protocolPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件protocolPage未找到\n" + traceback.format_exc())


def invitecodeText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'invitecodeText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件invitecodeText未找到\n" + traceback.format_exc())
    


def backButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register_protocol', 'backButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件未找到\n" + traceback.format_exc())
    


def registerButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, Data.getXpath('register', 'register', 'registerButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件registerButton未找到\n" + traceback.format_exc())
    


def loginButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, Data.getXpath('register', 'register', 'loginButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件loginButton未找到\n" + traceback.format_exc())


def eyecloseButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'eyecloseButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件eyecloseButton未找到\n" + traceback.format_exc())


def eyeopenButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'eyeopenButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件eyeopenButton未找到\n" + traceback.format_exc())


def pswfirstSecureText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'pswfirstSecureText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件pswfirstSecureText未找到\n" + traceback.format_exc())


def registerPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'pswfirstSecureText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件pswfirstSecureText未找到\n" + traceback.format_exc())


def loginButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'loginButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件loginButton未找到\n" + traceback.format_exc())



