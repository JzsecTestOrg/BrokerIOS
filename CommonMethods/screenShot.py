__author__ = 'xuwen1'

import globalData
from PIL import Image, ImageChops
import os
import math
import operator

def get_screenshot(self, i):
    moudule = globalData.MODULE
    self.driver.get_screenshot_as_file(globalData.PATH + '/TestResult/ActualScreenShot/' + moudule + '_' + str(i) + '.png')


def hanleScreenshot():
    root = globalData.PATH + '/TestResult/ActualScreenShot/'
    box=(0,75,1080,1800)
    for i in os.listdir(root):
        if(endWith(os.path.join(root, i), '.png')):
            f = Image.open(os.path.join(root, i))
            f.crop(box).save(os.path.join(root, i))


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
            if(isDifferent(os.path.join(actualdir, i), os.path.join(expectdir, i)) != 0.0):
                expectImage = Image.open(os.path.join(expectdir, i))
                actualImage = Image.open(os.path.join(actualdir, i))
                # differentImage = ImageChops.invert(actualImage)
                # Image.blend(expectImage, differentImage, 0.5).save(os.path.join(diffdir, i))
                differentImage = ImageChops.darker(expectImage, actualImage)
                differentImage.save(os.path.join(diffdir, i))


def isDifferent(image1, image2):
    image1 = Image.open(image1)
    image2 = Image.open(image2)


    h1 = image1.histogram()
    h2 = image2.histogram()

    rms = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return rms


if __name__ == '__main__':
    # hanleScreenshot()
    compareScreenshot()
