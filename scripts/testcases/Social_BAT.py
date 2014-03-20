#/usr/bin/python 

from devicewrapper.android import device as d
#from uiautomator import device as d
import unittest
import time
import os
import sys
import commands
import string

CAMERA_ACTIVITY = 'adb shell am start -n com.intel.camera22/.Camera'
CAMERA_ID = 'adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_camera_id_key'
PictureSize_STATE ='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_picture_size_key'
DCIM_PATH = '/sdcard/DCIM'
CAMERA_FOLDER = '100ANDRO'

class MyTest(unittest.TestCase):

    def setUp(self):
		d.press.home()
		self._launchcamera()
		super(MyTest,self).setUp()

    def testCaptureWithBackAndFrontCamera(self):
		# set camera status to back
		self._confirmcamerastatus('back')
		# take 10 picture
		for i in range (0,10):	
			self._takePicture()
		self._confirmcamerastatus('front')
		for i in range (0,10):
			self._takePicture()

    def testCaptureWith6MPPortraitFlashOn(self):
        # Set picture size
        self._setPictureSizeStatus('WideScreen')
        # Set flash status
        self._setFlashStatus('on')
        self._takePicture()

    def testCaptureWithFrontCamera(self):
		self._confirmcamerastatus('front')
		self._takePicture()

    def _launchcamera(self):
        commands.getoutput(CAMERA_ACTIVITY)

    def _confirmcamerastatus(self,status):
		#check back/front camera
        if status == 'front':
            camera = commands.getoutput(CAMERA_ID)
            cameravalue = camera.find('1')
            if cameravalue == -1:
	        commands.getoutput('adb shell input swipe 530 6 523 22')
	        d(description = 'Front and back camera switch').click.wait()
	        time.sleep(2)
	        camera = commands.getoutput(CAMERA_ID)
	        cameravalue = camera.find('1')
	        assert cameravalue != -1
        if status == 'back':
            camera = commands.getoutput(CAMERA_ID)
            cameravalue = camera.find('0')
            if cameravalue == -1:
	        commands.getoutput('adb shell input swipe 530 6 523 22')
	        d(description = 'Front and back camera switch').click.wait()
	        time.sleep(2)
	        camera = commands.getoutput(CAMERA_ID)
	        cameravalue = camera.find('0')
	        assert cameravalue != -1

    def _takePicture(self):
        result = commands.getoutput('adb shell ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
            time.sleep(3)
        d(description = 'Shutter button').click.wait()
        after = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        time.sleep(3)
        if string.atoi(before) == string.atoi(after) - 1 or string.atoi(before) == string.atoi(after) - 2:
            print('take picture success!')
        else:
            self.fail('take picture fail!')

    def _setPictureSizeStatus(self,status):
        #commands.getoutput('adb shell input swipe 530 6 523 22')
        d.swipe(530,6,523,22)
        d(description = 'Camera settings').click.wait()
        #.d()
        if status == 'WideScreen':
            d.click(60,292)
        elif status == 'StandardScreen':
            d.click(180,292)
        state = commands.getoutput()
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera picture size to' + status +'fail!')

    def _setFlashStatus(self,status):
        #commands.getoutput('adb shell input swipe 530 6 523 22')
        # Touch flash setting
        d.swipe(530,6,523,22)
        d(description = 'Camera settings').click.wait()
        if status == 'on':
            d.click(176,176)
        elif status == 'off':
            d.click(59,178)
        else:
            self.touch((296,176))
        state = commands.getoutput(PictureSize_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera flash status to' + status + 'fail!') 

    def tearDown(self):
		d.press.back()
		super(MyTest,self).tearDown()

if __name__ =='__main__':  
    unittest.main()  
