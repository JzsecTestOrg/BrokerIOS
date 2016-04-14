__author__ = 'xuwen1'

import globalData, Data
from PIL import Image, ImageFont, ImageDraw
import os
import math
import operator

def get_screenshot(self, i):
    moudule = globalData.MODULE
    self.driver.get_screenshot_as_file(globalData.PATH + '/TestResult/ActualScreenShot/' + moudule + '_' + str(i) + '.png')


def hanleScreenshot(image1, image2, size, box):
    image = Image.new('RGB', size)
    x, y = size
    box1 = (0, 0, x/2, y)
    box2 = (x/2, 0, x, y)
    title1 = 'Expect Result'
    title2 = 'Actual Result'
    ps1 = ImageDraw.ImageDraw(image1)
    ps1.line((box[0], box[1]) + (box[2], box[1]), fill=128, width = 5)
    ps1.line((box[0], box[1]) + (box[0], box[3]), fill=128, width = 5)
    ps1.line((box[2], box[1]) + (box[2], box[3]), fill=128, width = 5)
    ps1.line((box[0], box[3]) + (box[2], box[3]), fill=128, width = 5)
    fnt = ImageFont.truetype('Calibri', 100)
    ps1.text((300, 200), title1, fill=(255,0,0), font=fnt)
    ps2 = ImageDraw.ImageDraw(image2)
    ps2.line((box[0], box[1]) + (box[2], box[1]), fill=128, width = 5)
    ps2.line((box[0], box[1]) + (box[0], box[3]), fill=128, width = 5)
    ps2.line((box[2], box[1]) + (box[2], box[3]), fill=128, width = 5)
    ps2.line((box[0], box[3]) + (box[2], box[3]), fill=128, width = 5)
    ps2.text((300, 200), title2, fill=(255,0,0), font=fnt)
    image.paste(image1, box1)
    image.paste(image2, box2)
    return image


def endWith(s,*endstring):
        array = map(s.endswith,endstring)
        if True in array:
            return True
        else:
            return False

def compareScreenshot():
    expectdir = globalData.PATH + '/TestResult/ExpectScreenShot/'
    actualdir = globalData.PATH + '/TestResult/ActualScreenShot/'
    diffdir = globalData.PATH + '/TestResult/DifferentScreenShot/'
    for i in os.listdir(actualdir):
        if(endWith(os.path.join(actualdir, i), '.png')):
            if(isDifferent(os.path.join(actualdir, i), os.path.join(expectdir, i), globalData.BOX) != 0.0):
                expectImage = Image.open(os.path.join(expectdir, i))
                actualImage = Image.open(os.path.join(actualdir, i))
                # differentImage = ImageChops.invert(actualImage)
                # Image.blend(expectImage, differentImage, 0.5).save(os.path.join(diffdir, i))
                # differentImage = ImageChops.invert(actualImage)
                # differentImage.save(os.path.join(diffdir, i))
                differentImage = hanleScreenshot(expectImage, actualImage, globalData.SIZE, globalData.BOX)
                differentImage.save(os.path.join(diffdir, i))


def isDifferent(image1, image2, box):
    image1 = Image.open(image1)
    image2 = Image.open(image2)
    region1 = image1.crop(box)
    region2 = image2.crop(box)


    h1 = region1.histogram()
    h2 = region2.histogram()

    rms = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
    return rms

def mark_result():
    actualdir = globalData.PATH + '/TestResult/ActualScreenShot/'
    diffdir = globalData.PATH + '/TestResult/DifferentScreenShot/'
    for i in os.listdir(diffdir):
        if(endWith(os.path.join(diffdir, i), '.png')):
            moudle = i.split('_')[0]
            case = i.split('_')[1].split('.')[0]
            Data.setExecutionresult(moudle, int(case), 'Fail')
    for j in os.listdir(actualdir):
        if(endWith(os.path.join(actualdir, j), '.png')):
            if(os.path.exists(os.path.join(diffdir, j)) == False):
                moudle = j.split('_')[0]
                case = j.split('_')[1].split('.')[0]
                Data.setExecutionresult(moudle, int(case), 'Pass')


if __name__ == '__main__':
    # hanleScreenshot()
    compareScreenshot()
    # globalData.EXECUTED = [{'register': ['Pass', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed', 'Not Executed']}]
    # mark_result()
    # print globalData.EXECUTED
