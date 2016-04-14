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
    


def passwordText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'passwordText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件passwordText未找到\n" + traceback.format_exc())
    


def cipherpasswordText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'cipherpasswordText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件cipherpasswordText未找到\n" + traceback.format_exc())


def plainpasswordText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'plainpasswordText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件plainpasswordText未找到\n" + traceback.format_exc())
    


def nicknameText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'nicknameText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件nicknameText未找到\n" + traceback.format_exc())
    


def protocolCheckbox(self, i):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'protocolCheckbox', i))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件protocolCheckbox未找到\n" + traceback.format_exc())




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
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'registerButton', 1))))
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
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'registerPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件registerPage未找到\n" + traceback.format_exc())


def loginButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'loginButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件loginButton未找到\n" + traceback.format_exc())


def protocolText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'protocolText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件protocolText未找到\n" + traceback.format_exc())


def servicephoneText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'servicephoneText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件servicephoneText未找到\n" + traceback.format_exc())


def popupText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'popupText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件popupText未找到\n" + traceback.format_exc())


def continueregisterButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'continueregisterButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件continueregisterButton未找到\n" + traceback.format_exc())


def cancelButton(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'cancelButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件cancelButton未找到\n" + traceback.format_exc())


def confirmButton(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'confirmButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件confirmButton未找到\n" + traceback.format_exc())


