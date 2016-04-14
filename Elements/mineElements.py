# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

from CommonMethods import Data, generateLog, globalData
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback

def affiliateLink(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'affiliateLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件affiliateLink未找到\n" + traceback.format_exc())



def minePage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'minePage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件minePage未找到\n" + traceback.format_exc())


def nicknameInfo(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'nicknameInfo', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件nicknameInfo未找到\n" + traceback.format_exc())


def departmentInfo(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'departmentInfo', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件departmentInfo未找到\n" + traceback.format_exc())


def cashInfo(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'cashInfo', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件cashInfo未找到\n" + traceback.format_exc())


def personalinfoLink(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'personalinfoLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件personalinfoLink未找到\n" + traceback.format_exc())


def personalinfoPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'personalinfoPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件personalinfoPage未找到\n" + traceback.format_exc())


def profileButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'profileButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件profileButton未找到\n" + traceback.format_exc())

def cameraButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'cameraButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件cameraButton未找到\n" + traceback.format_exc())
    


def imageButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'imageButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件imageButton未找到\n" + traceback.format_exc())
    


def cameralimitButton(self):
    try:
        el = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'cameralimitButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件cameralimitButton未找到\n" + traceback.format_exc())
    



def photocaptureButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'photocaptureButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件photocaptureButton未找到\n" + traceback.format_exc())
    


def imagelimitButton(self):
    try:
        el = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'imagelimitButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件imagelimitButton未找到\n" + traceback.format_exc())
    


def timephotoButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'timephotoButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件timephotoButton未找到\n" + traceback.format_exc())
    


def imagecancelButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'imagecancelButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件imagecancelButton未找到\n" + traceback.format_exc())
    


def usephotoButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'usephotoButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件usephotoButton未找到\n" + traceback.format_exc())


def profileImage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'profileImage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件profileImage未找到\n" + traceback.format_exc())


def profileselectButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'profileselectButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件profileselectButton未找到\n" + traceback.format_exc())


def nicknameText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'nicknameText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件nicknameText未找到\n" + traceback.format_exc())


def nicknameItem(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'nicknameItem', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件nicknameItem未找到\n" + traceback.format_exc())


def changenicknamePage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'changenicknamePage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件changenicknamePage未找到\n" + traceback.format_exc())


def nicknameFiled(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'nicknameFiled', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件nicknameFiled未找到\n" + traceback.format_exc())


def nicknamedeleteButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'nicknamedeleteButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件nicknamedeleteButton未找到\n" + traceback.format_exc())


def nicknamecountText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'nicknamecountText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件nicknamecountText未找到\n" + traceback.format_exc())


def nicknamesaveButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'nicknamesaveButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件nicknamesaveButton未找到\n" + traceback.format_exc())


def backButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'backButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件backButton未找到\n" + traceback.format_exc())


def introductionButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'introductionButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件introductionButton未找到\n" + traceback.format_exc())


def phoneText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'phoneText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件phoneText未找到\n" + traceback.format_exc())


def nameText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'nameText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件nameText未找到\n" + traceback.format_exc())


def departmentText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'departmentText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件departmentText未找到\n" + traceback.format_exc())


def contractText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'contractText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件contractText未找到\n" + traceback.format_exc())


def sacidText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'sacidText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件sacidText未找到\n" + traceback.format_exc())


def addressItem(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'addressItem', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件addressItem未找到\n" + traceback.format_exc())


def addressText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'addressText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件addressText未找到\n" + traceback.format_exc())


def changeaddressPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'changeaddressPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件changeaddressPage未找到\n" + traceback.format_exc())


def addressField(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'addressField', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件addressField未找到\n" + traceback.format_exc())


def addresscountText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'addresscountText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件addresscountText未找到\n" + traceback.format_exc())


def addresssaveButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'addresssaveButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件addresssaveButton未找到\n" + traceback.format_exc())


def emailItem(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'emailItem', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件emailItem未找到\n" + traceback.format_exc())


def emailText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'emailText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件emailText未找到\n" + traceback.format_exc())


def changeemailPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'changeemailPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件changeemailPage未找到\n" + traceback.format_exc())


def emailField(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'emailField', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件emailField未找到\n" + traceback.format_exc())


def emaildeleteButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'emaildeleteButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件emaildeleteButton未找到\n" + traceback.format_exc())


def emailsaveButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'emailsaveButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件emailsaveButton未找到\n" + traceback.format_exc())


def aboutbrokerLink(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'aboutbrokerLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件aboutbrokerLink未找到\n" + traceback.format_exc())


def aboutbrokerPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'aboutbrokerPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件aboutbrokerPage未找到\n" + traceback.format_exc())


def brokerintroductionLink(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'brokerintroductionLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件brokerintroductionLink未找到\n" + traceback.format_exc())


def brokerintroductionPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'brokerintroductionPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件brokerintroductionPage未找到\n" + traceback.format_exc())


def brokerintroductionContent(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'brokerintroductionContent', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件brokerintroductionContent未找到\n" + traceback.format_exc())


def fullbrokerageLink(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'fullbrokerageLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件fullbrokerageLink未找到\n" + traceback.format_exc())


def fullbrokeragePage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'fullbrokeragePage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件fullbrokeragePage未找到\n" + traceback.format_exc())


def relatedruleContent(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'relatedruleContent', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件relatedruleContent未找到\n" + traceback.format_exc())


def fullbrokerageContent(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'fullbrokerageContent', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件fullbrokerageContent未找到\n" + traceback.format_exc())


def brokerseviceLink(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'brokerseviceLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件brokerseviceLink未找到\n" + traceback.format_exc())


def brokersevicePage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'brokersevicePage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件brokersevicePage未找到\n" + traceback.format_exc())


def brokerseviceContent(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'brokerseviceContent', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件brokerseviceContent未找到\n" + traceback.format_exc())


def relatedruleLink(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'relatedruleLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件relatedruleLink未找到\n" + traceback.format_exc())


def relatedrulePage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'aboutbroker', 'relatedrulePage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件relatedrulePage未找到\n" + traceback.format_exc())


def historyrecordButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'historyrecordButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件historyrecordButton未找到\n" + traceback.format_exc())


def historyrecordPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'historyrecordPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件historyrecordPage未找到\n" + traceback.format_exc())


def kpiItem(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpiItem未找到\n" + traceback.format_exc())


def kpitimeText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[2]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpitimeText未找到\n" + traceback.format_exc())


def kpidescText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[1]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpidescText未找到\n" + traceback.format_exc())


def kpipointText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[3]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpipointText未找到\n" + traceback.format_exc())


def kpidetailPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'kpidetailPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpidetailPage未找到\n" + traceback.format_exc())


def kpidetailtimeText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'kpidetailtimeText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpidetailtimeText未找到\n" + traceback.format_exc())


def kpidetaildescText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'kpidetaildescText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpidetaildescText未找到\n" + traceback.format_exc())


def kpidetailpointText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'kpidetailpointText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpidetailpointText未找到\n" + traceback.format_exc())


def kpiruleLink(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'kpiruleLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpiruleLink未找到\n" + traceback.format_exc())


def kpirulePage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'kpirulePage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpirulePage未找到\n" + traceback.format_exc())


def kpiruleContent(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'kpiruleContent', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpiruleContent未找到\n" + traceback.format_exc())


def kpisubText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'kpisubText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpisubText未找到\n" + traceback.format_exc())


def kpichangetimeText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[" + str(i) + "]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpichangetimeText未找到\n" + traceback.format_exc())


def kpichangdescText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[2]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpichangdescText未找到\n" + traceback.format_exc())


def kpichangepointText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[3]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件kpichangepointText未找到\n" + traceback.format_exc())


def recordScrollview(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'recordScrollview', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件recordScrollview未找到\n" + traceback.format_exc())


def incomedetailcustrecommandText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[3]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomedetailcustrecommandText未找到\n" + traceback.format_exc())


def tradetotalamountText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'tradetotalamountText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件tradetotalamountText未找到\n" + traceback.format_exc())


def trademonthText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[2]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件trademonthText未找到\n" + traceback.format_exc())


def trademonthamountText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[3]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件trademonthamountText未找到\n" + traceback.format_exc())


def tradedetailtotalamountText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'tradedetailtotalamountText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件tradedetailtotalamountText未找到\n" + traceback.format_exc())


def tradedetailcustamountText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[2]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件tradedetailcustamountText未找到\n" + traceback.format_exc())


def incometotalText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'incometotalText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incometotalText未找到\n" + traceback.format_exc())


def securitytotalText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'securitytotalText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件securitytotalText未找到\n" + traceback.format_exc())


def securityguardPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'securityguardPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件securityguardPage未找到\n" + traceback.format_exc())


def securitydetailtotalText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'securitydetailtotalText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件securitydetailtotalText未找到\n" + traceback.format_exc())

def securitymonthText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[" + str(2 * i - 1) + "]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件securitymonthText未找到\n" + traceback.format_exc())


def securitydetailamountText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[" + str(i * 2) + "]/UIAStaticText[2]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件securitydetailamountText未找到\n" + traceback.format_exc())


def incomedetailPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'incomedetailPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomedetailPage未找到\n" + traceback.format_exc())


def incomemonthText(self, i):
    try:
        self.driver.execute_script("mobile: scrollTo", {"element": self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]").id})
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[1]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomemonthText未找到\n" + traceback.format_exc())


def incomecommssionText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[3]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomecommssionText未找到\n" + traceback.format_exc())


def incomerecommandText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[4]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomerecommandText未找到\n" + traceback.format_exc())


def incometaxText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[5]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incometaxText未找到\n" + traceback.format_exc())


def incomemonthtotalText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[6]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomemonthtotalText未找到\n" + traceback.format_exc())


def incomemonthItem(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomemonthItem未找到\n" + traceback.format_exc())


def incomedetailmonthText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'incomedetailmonthText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomedetailmonthText未找到\n" + traceback.format_exc())


def incomedetailtotalText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'incomedetailtotalText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomedetailtotalText未找到\n" + traceback.format_exc())


def incomedetailsecurityText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'incomedetailsecurityText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomedetailsecurityText未找到\n" + traceback.format_exc())


def securitytipButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'securitytipButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件securitytipButton未找到\n" + traceback.format_exc())


def securitydescContent(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'securitydescContent', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件securitydescContent未找到\n" + traceback.format_exc())


def securitydescPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'securitydescPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件securitydescPage未找到\n" + traceback.format_exc())


def incomedetailcommissiontaxText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'incomedetailcommissiontaxText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomedetailcommissiontaxText未找到\n" + traceback.format_exc())


def incomedetailrecommandtaxText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'incomedetailrecommandtaxText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomedetailrecommandtaxText未找到\n" + traceback.format_exc())


def incomedetailcommissionText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'incomedetailcommissionText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomedetailcommissionText未找到\n" + traceback.format_exc())


def incomedetailrecommandText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'historyrecord', 'incomedetailrecommandText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件incomedetailrecommandText未找到\n" + traceback.format_exc())


def currentkpiItem(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'currentkpiItem', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentkpiItem未找到\n" + traceback.format_exc())


def currentkpiText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'currentkpiText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentkpiText未找到\n" + traceback.format_exc())


def currentcommissionText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'currentcommissionText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentcommissionText未找到\n" + traceback.format_exc())


def currentrecommendText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'currentrecommendText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件thisrecommendText未找到\n" + traceback.format_exc())


def currentkpidetailPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'currentrecord', 'currentkpidetailPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentkpidetailPage未找到\n" + traceback.format_exc())


def currentkpidetailtimeText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'currentrecord', 'currentkpidetailtimeText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentkpidetailtimeText未找到\n" + traceback.format_exc())


def currentkpidetaildescText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'currentrecord', 'currentkpidetaildescText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentkpidetaildescText未找到\n" + traceback.format_exc())


def currentkpidetailpointText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'currentrecord', 'currentkpidetailpointText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentkpidetailpointText未找到\n" + traceback.format_exc())


def currentkpiruleLink(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'currentrecord', 'currentkpiruleLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentkpiruleLink未找到\n" + traceback.format_exc())


def currentkpisubText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'currentrecord', 'currentkpisubText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentkpisubText未找到\n" + traceback.format_exc())


def currentkpichangetimeText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell[" + str(i) + "]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentkpichangetimeText未找到\n" + traceback.format_exc())


def currentkpichangdescText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[2]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentkpichangdescText未找到\n" + traceback.format_exc())


def currentkpichangepointText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[3]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentkpichangepointText未找到\n" + traceback.format_exc())


def currenttradetotalamountText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'currentrecord', 'currenttradetotalamountText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currenttradetotalamountText未找到\n" + traceback.format_exc())


def currenttradelcustamountText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[2]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currenttradelcustamountText未找到\n" + traceback.format_exc())


def currentcontinuouscommissionText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'currentrecord', 'currentcontinuouscommissionText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentcontinuouscommissionText未找到\n" + traceback.format_exc())


def currentcustrecommandText(self, i):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[3]/UIATableView[1]/UIATableCell[" + str(i) + "]/UIAStaticText[3]")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件currentcustrecommandText\n" + traceback.format_exc())


def withdrawcashButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'withdrawcashButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件withdrawcashButton未找到\n" + traceback.format_exc())


def authorizecancelButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'authorizecancelButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件authorizecancelButton未找到\n" + traceback.format_exc())


def adjustbrokerageLink(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'adjustbrokerageLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件adjustbrokerageLink未找到\n" + traceback.format_exc())


def adjustbrokeragePage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'adjustbrokerage', 'adjustbrokeragePage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件adjustbrokeragePage未找到\n" + traceback.format_exc())


def searchadjustText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'adjustbrokerage', 'searchadjustText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件searchadjustText未找到\n" + traceback.format_exc())


def adjustbrokerageItem(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'adjustbrokerage', 'adjustbrokerageItem', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件adjustbrokerageItem未找到\n" + traceback.format_exc())


def adjuststatusText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'adjustbrokerage', 'adjuststatusText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件adjuststatusText未找到\n" + traceback.format_exc())


def adjustbrokeragedetailPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'adjustbrokerage', 'adjustbrokeragedetailPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件adjustbrokeragedetailPage未找到\n" + traceback.format_exc())


def adjuststatusdetailText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'adjustbrokerage', 'adjuststatusdetailText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件adjuststatusdetailText未找到\n" + traceback.format_exc())

def adjustcancelButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'adjustbrokerage', 'adjustcancelButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件adjustcancelButton未找到\n" + traceback.format_exc())


def introductionPage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'introduction', 'introductionPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件introductionPage未找到\n" + traceback.format_exc())


def introductionText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'introduction', 'introductionText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件introductionText未找到\n" + traceback.format_exc())


def tipText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'introduction', 'tipText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件tipText未找到\n" + traceback.format_exc())


def introductioncountText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'introduction', 'introductioncountText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件introductioncountText未找到\n" + traceback.format_exc())


def introductioncommitButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'introduction', 'introductioncommitButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件introductioncommitButton未找到\n" + traceback.format_exc())


def profileconfirmButton(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'personalinfo', 'profileconfirmButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件profileconfirmButton未找到\n" + traceback.format_exc())


def invitecodeLink(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'invitecodeLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件invitecodeLink未找到\n" + traceback.format_exc())


def invitecodePage(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'invitecode', 'invitecodePage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件invitecodePage未找到\n" + traceback.format_exc())


def invitecodeText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'invitecode', 'invitecodeText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件invitecodeText未找到\n" + traceback.format_exc())


def brokeractivityText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'invitecode', 'brokeractivityText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件brokeractivityText未找到\n" + traceback.format_exc())


def examactivityText(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'invitecode', 'examactivityText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件examactivityText未找到\n" + traceback.format_exc())


def invitecodevalueText(self, code):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//UIAStaticText[@name = '您当前填写的邀请码：" + code +"\']")))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件invitecodevalueText未找到\n" + traceback.format_exc())
