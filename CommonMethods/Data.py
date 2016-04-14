# -*- coding: utf-8 -*-
__author__ = 'xuwen'

import xlrd
from pyexcel_xls import XLBook
import sys
import os
import globalData


def TestData():
    file_path = globalData.PATH + '/TestData/BappData.xlsx'
    workbook = XLBook(file_path)
    test_data = dict(workbook.sheets())
    return test_data

def getXpath(tab, page, element, index):
    worksheet = globalData.DATA.get(tab)
    nrows = len(worksheet)
    for i in range(1, nrows):
        if(worksheet[i][0] == unicode(page,'utf-8')):
            if(worksheet[i][1] == unicode(element,'utf-8')):
                if(int(worksheet[i][2]) == index):
                    return worksheet[i][3]
                    break


def getValue(tab, page, element, index):
    module = globalData.MODULE
    worksheet = globalData.DATA.get(tab)
    nrows = len(worksheet)
    for i in range(0, nrows):
        if(worksheet[i][0] == unicode(page,'utf-8')):
            if(worksheet[i][1] == unicode(element,'utf-8')):
                if(int(worksheet[i][2]) == index):
                    return str(worksheet[i][4]).split('.')[0]
                    break


def getNumber(tab, page, element, index):
    module = globalData.MODULE
    worksheet = globalData.DATA.get(tab)
    nrows = len(worksheet)
    for i in range(0, nrows):
        if(worksheet[i][0] == unicode(page,'utf-8')):
            if(worksheet[i][1] == unicode(element,'utf-8')):
                if(int(worksheet[i][2]) == index):
                    return str(worksheet[i][4]).split('.')[0]
                    break


def getPrecondition(tab, case):
    worksheet = globalData.TESTDATA.get(tab)
    return worksheet[case][1]


def getTestdata(tab, case, index):
    worksheet = globalData.TESTDATA.get(tab)
    if('.' in str(worksheet[case][index])):
        return  str(worksheet[case][index]).split('.')[0]
    else:
        return worksheet[case][index]

def getCasenumber(module):
    worksheet = globalData.TESTDATA.get(module)
    nrows = len(worksheet)
    return nrows - 1

def setExecutionresult(module, i, result):
    for j in range(0, len(globalData.EXECUTED)):
        if(globalData.EXECUTED[j].keys()[0] == module):
            globalData.EXECUTED[j].values()[0][i - 1] = result





# if __name__ == '__main__':
    # print Data()
    # print sys.path
    # print os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    # print getXpath('welcome', 'versionUpdate_cancel', 1)
    # print getXpath('login', 'phoneText', '1')
    # print getXpath('welcome', 'versionUpdate_cancel', 1)
    # globalData.MODULE = 'register'
    # print unicode("输入昵称: ", 'utf-8') + getValue('register', 'nicknameText', 1)


