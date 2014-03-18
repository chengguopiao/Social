#/usr/bin/python 

from devicewrapper.android import device as d
#from uiautomator import device as d
import unittest
import time
import os
import sys

class MyTest(unittest.TestCase):

    def setUp(self):
	d.press.home()
	self._launchcamera()
	super(MyTest,self).setUp()


    def testCaptureWithBackAndFrontCamera(self):
	#find 'Camera' app in main screen and launch it.
	d.press.back()
	self._confirmcamerastatus('back')


    def _launchcamera(self):
	#find 'Camera' app in main screen and launch it.
		while not d(text = 'Camera').wait.exists(timeout=2000):
	    		d().swipe.right()
		d(text = 'Camera').click()
		#Verify that Camera is launched.
		assert d(className = 'android.view.View', packageName = 'com.sec.android.app.camera'), 'Camera unable to be launched.'
		d.click(1203,656)
		time.sleep(3)

    def _confirmcamerastatus(self,status):
	#check back/front camera
        if status == 'back':
            camera = commands.getoutput(CAMERA_ID)
            cameravalue = camera.find(CAMERA_ID_BACK)
            if cameravalue == -1:
	        commands.getoutput('adb shell input swipe 530 6 523 22')
	        d(description=Switch_desceiption).click.wait()
	        time.sleep(2)
	        camera = commands.getoutput(CAMERA_ID)
	        cameravalue = camera.find(CAMERA_ID_BACK)
	        assert cameravalue != -1
        if status == 'front':
            camera = commands.getoutput(CAMERA_ID)
            cameravalue = camera.find(CAMERA_ID_FRONT)
            if cameravalue == -1:
	        commands.getoutput('adb shell input swipe 530 6 523 22')
	        d(description=Switch_desceiption).click.wait()
	        time.sleep(2)
	        camera = commands.getoutput(CAMERA_ID)
	        cameravalue = camera.find(CAMERA_ID_FRONT)
	        assert cameravalue != -1

    def tearDown(self):
	d.press.home()
	super(MyTest,self).tearDown()

if __name__ =='__main__':  
    unittest.main()  
