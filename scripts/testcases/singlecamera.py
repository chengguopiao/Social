import unittest
import commands
from uiautomator import device as d
import time
import string
import os

PACKAGE_NAME = 'com.intel.camera2'
ACTIVITY_NAME = PACKAGE_NAME + '.Camera'
DCIM_PATH = 'adb shell ls /sdcard/DCIM'
CAMERA_FOLDER = '100ANDRO'
CAMERA_ID = 'adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_camera_id_key'
Flash_STATE= 'adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_flashmode_key'
Exposure_STATE= 'adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_exposure_key'
Scene_STATE = 'adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_scenemode_key'
FDFR_STATE ='adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_fdfr_key'
PictureSize_STATE ='adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_picture_size_key'
Geolocation_STATE ='adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_camera_geo_location_key' 
Hints_STATE ='adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_hints_key'
WhiteBalance_STATE='adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_whitebalance_key'
ISO_STATE='adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_iso_key'
SelfTimer_STATE='adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_delay_shooting_key'
Delete_CMD = 'adb shell rm -r sdcard/DCIM/100ANDRO/'
CAMERA_ID_FRONT = '1'
CAMERA_ID_BACK = '0'
PICTURE_PATH = '' + os.sep + 'mnt'+os.sep+ DCIM_PATH+'/'+CAMERA_FOLDER
Switch_desceiption = 'Front and back camera switch'
Shuttor_description = 'Shutter button'
Setting_description = 'Camera settings'
Flash_description = 'Flash settings'
FDFR_description = 'Face recognition'



class SingleCamera(unittest.TestCase):
    def setUp(self):
	self.launchcamera()

    def tearDown(self):
	for i in range(3):
	    d.press.back()
	commands.getoutput(Delete_CMD)

        
    #Test case 1  Summary: Test capture picture with sence auto
    def testcapturewithsenceauto(self):
	self.confirmcamerastatus('back')	
	#step 2
	self.setsencestatus('auto')
	#step 3
	self.takesinglepicture()
 
    #Test case 2  Summary:Test capture picture with sence sports
    def testcapturewithsencesports(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setsencestatus('sports')
	#step 3
	self.takesinglepicture()


    #Test case 3  Summary:Test capture picture with sence night
    def testcapturewithsencenight(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setsencestatus('night')
	#step 3
	self.takesinglepicture()

    
    #Test case 4  Summary:Test capture picture with sence landscape
    def testcapturewithsencelandscape(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setsencestatus('landscape')
	#step 3
	self.takesinglepicture()


    #Test case 5  Summary:Test capture picture with sence portrait
    def testcapturewithsenceportrait(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setsencestatus('portrait')
	#step 3
	self.takesinglepicture()


    #Test case 6  Summary:Test capture picture with sence night-portrait
    def testcapturewithsencenightportrait(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setsencestatus('night-portrait')
	#step 3
	self.takesinglepicture()


    #Test case 7  Summary:Test capture picture with sence barcode
    def testcapturewithsencebarcode(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setsencestatus('barcode')
	#step 3
	self.takesinglepicture()


    #Test case 8  Summary:Test capture picture with sence fireworks
    def testcapturewithsencefireworks(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setsencestatus('fireworks')
	#step 3
	self.takesinglepicture()

   
    
    #Test case 9  Summary:Test capture picture with flash on
    def testcapturewithflashon(self):
        self.confirmcamerastatus('back')	
	#step 2
        state = commands.getoutput(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
	    self.setsencestatus('auto')
	    time.sleep(5)
	self.setflashstatus('on')
	#step 3
	self.takesinglepicture()

    #Test case 10  Summary:Test capture picture with flash off
    def testcapturewithflashoff(self):
        self.confirmcamerastatus('back')	
	#step 2
        state = commands.getoutput(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
	    self.setsencestatus('auto')
	    time.sleep(5)
	self.setflashstatus('off')
	#step 3
	self.takesinglepicture()

    #Test case 11  Summary:Test capture picture with flash auto
    def testcapturewithflashauto(self):
        self.confirmcamerastatus('back')	
	#step 2
        state = commands.getoutput(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
	    self.setsencestatus('auto')
	    time.sleep(5)
	self.setflashstatus('auto')
	#step 3
	self.takesinglepicture()

    
    #Test case 12  Summary:Test capture picture with FD/FR on
    def testcapturewithfdfron(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setFDFRstatus('on')
	#step 3
	self.takesinglepicture()

    #Test case 13  Summary:Test capture picture with FD/FR off
    def testcapturewithfdfroff(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setFDFRstatus('off')
	#step 3
	self.takesinglepicture()
    
    #Test case 14  Summary:Test capture picture with hints off
    def testcapturewithhintsoff(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.sethintsstatus('off')
	#step 3
	self.takesinglepicture()

    #Test case 15  Summary:Test capture picture with hints on
    def testcapturewithhintson(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.sethintsstatus('on')
	#step 3
	self.takesinglepicture()
    
    #Test case 16  Summary:Test capture picture with location on
    def testcapturewithlocationon(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setlocationstatus('on')
	#step 3
	self.takesinglepicture()

    #Test case 17  Summary:Test capture picture with location off
    def testcapturewithlocationoff(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setlocationstatus('off')
	#step 3
	self.takesinglepicture()
    
    #Test case 18  Summary:Test capture picture with pciture size wide
    def testcapturewithpicturesizewide(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setpicturesize('WideScreen')
	#step 3
	self.takesinglepicture()
    
    #Test case 19  Summary:Test capture picture with pciture size standard
    def testcapturewithpicturesizestandard(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setpicturesize('StandardScreen')
	#step 3
	self.takesinglepicture()

    #Test case 20  Summary:Test capture picture with expoure auto
    def testcapturewithexpoureauto(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setexpourestatus('0')
	#step 3
	self.takesinglepicture()

    #Test case 21  Summary:Test capture picture with expoure +1
    def testcapturewithexpoure1(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setexpourestatus('3')
	#step 3
	self.takesinglepicture()

    #Test case 22  Summary:Test capture picture with expoure +2
    def testcapturewithexpoure2(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setexpourestatus('6')
	#step 3
	self.takesinglepicture()

    #Test case 23  Summary:Test capture picture with expoure -1
    def testcapturewithexpoureend1(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setexpourestatus('-3')
	#step 3
	self.takesinglepicture()

    #Test case 24  Summary:Test capture picture with expoure -2
    def testcapturewithexpoureend2(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setexpourestatus('-6')
	#step 3
	self.takesinglepicture()

    #Test case 25  Summary:Test capture picture with wb auto
    def testcapturewithwbauto(self):
        self.confirmcamerastatus('back')	
	#step 2
        state = commands.getoutput(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
	    self.setsencestatus('auto')
	    time.sleep(5)
	self.setwbstatus('auto')
	#step 3
	self.takesinglepicture()

    #Test case 26  Summary:Test capture picture with wb incandescent
    def testcapturewithwbincandescent(self):
        self.confirmcamerastatus('back')	
	#step 2
        state = commands.getoutput(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
	    self.setsencestatus('auto')
	    time.sleep(5)
	self.setwbstatus('incandescent')
	#step 3
	self.takesinglepicture()

    #Test case 27  Summary:Test capture picture with wb daylight
    def testcapturewithwbdaylight(self):
        self.confirmcamerastatus('back')	
	#step 2
        state = commands.getoutput(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
	    self.setsencestatus('auto')
	    time.sleep(5)
	self.setwbstatus('daylight')
	#step 3
	self.takesinglepicture()
    
    #Test case 28  Summary:Test capture picture with wb fluorescent
    def testcapturewithwbfluorescent(self):
        self.confirmcamerastatus('back')	
	#step 2
        state = commands.getoutput(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
	    self.setsencestatus('auto')
	    time.sleep(5)
	self.setwbstatus('fluorescent')
	#step 3
	self.takesinglepicture()

    #Test case 29  Summary:Test capture picture with wb cloudy-daylight
    def testcapturewithwbcloudydaylight(self):
        self.confirmcamerastatus('back')	
	#step 2
        state = commands.getoutput(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
	    self.setsencestatus('auto')
	    time.sleep(5)
	self.setwbstatus('cloudy-daylight')
	#step 3
	self.takesinglepicture()
    
    #Test case 30  Summary:Test capture picture with iso-auto
    def testcapturewithisoauto(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setisostatus('iso-auto')
	#step 3
	self.takesinglepicture()

    #Test case 31  Summary:Test capture picture with iso-100
    def testcapturewithiso100(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setisostatus('iso-100')
	#step 3
	self.takesinglepicture()

    #Test case 32  Summary:Test capture picture with iso-200
    def testcapturewithiso200(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setisostatus('iso-200')
	#step 3
	self.takesinglepicture()

    #Test case 33  Summary:Test capture picture with iso-400
    def testcapturewithiso400(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setisostatus('iso-400')
	#step 3
	self.takesinglepicture()

    #Test case 34  Summary:Test capture picture with iso-800
    def testcapturewithiso800(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setisostatus('iso-800')
	#step 3
	self.takesinglepicture()
    
    #Test case 35  Summary:Test capture picture with self-timer 10
    def testcapturewithselftimer10(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setselftimerstatus('10')
	#step 3
	result = commands.getoutput('adb shell ls '+ DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
	    beforeNO = 0
        else:
	    beforeNO = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        time.sleep(3)
        d(description=Shuttor_description).click.wait()
        time.sleep(13)
        afterNO = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        assert string.atoi(beforeNO) == string.atoi(afterNO) - 1 or string.atoi(beforeNO) == string.atoi(afterNO) - 2
	self.setselftimerstatus('0')
    
    #Test case 36  Summary:Test capture picture with self-timer 5
    def testcapturewithselftimer5(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setselftimerstatus('5')
	#step 3
	result = commands.getoutput('adb shell ls '+ DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
	    beforeNO = 0
        else:
	    beforeNO = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        time.sleep(3)
        d(description=Shuttor_description).click.wait()
        time.sleep(8)
        afterNO = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        assert string.atoi(beforeNO) == string.atoi(afterNO) - 1 or string.atoi(beforeNO) == string.atoi(afterNO) - 2
	self.setselftimerstatus('0')

    #Test case 37  Summary:Test capture picture with self-timer 3
    def testcapturewithselftimer3(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setselftimerstatus('3')
	#step 3
	result = commands.getoutput('adb shell ls '+ DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
	    beforeNO = 0
        else:
	    beforeNO = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        time.sleep(3)
        d(description=Shuttor_description).click.wait()
        time.sleep(6)
        afterNO = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        assert string.atoi(beforeNO) == string.atoi(afterNO) - 1 or string.atoi(beforeNO) == string.atoi(afterNO) - 2
	self.setselftimerstatus('0')
    
    #Test case 38  Summary:Test capture picture with self-timer 0
    def testcapturewithselftimer0(self):
        self.confirmcamerastatus('back')	
	#step 2
	self.setselftimerstatus('0')
	#step 3
	result = commands.getoutput('adb shell ls '+ DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
	    beforeNO = 0
        else:
	    beforeNO = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        time.sleep(3)
        d(description=Shuttor_description).click.wait()
        time.sleep(3)
        afterNO = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        assert string.atoi(beforeNO) == string.atoi(afterNO) - 1 or string.atoi(beforeNO) == string.atoi(afterNO) - 2
    
    
    def confirmcamerastatus(self,status):
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
	    

    def takesinglepicture(self):
        result = commands.getoutput('adb shell ls '+ DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
	    beforeNO = 0
        else:
	    beforeNO = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        time.sleep(2)
        d(description=Shuttor_description).click.wait()
        time.sleep(3)
        afterNO = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        assert string.atoi(beforeNO) == string.atoi(afterNO) - 1 or string.atoi(beforeNO) == string.atoi(afterNO) - 2


    def setsencestatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
	time.sleep(1)
	d(description=Setting_description).click.wait()
	commands.getoutput('adb shell input tap 531 165')
	time.sleep(1)
	if status == 'auto':
	    commands.getoutput('adb shell input swipe 660 285 66 285')
	    commands.getoutput('adb shell input tap 657 294')
	elif status == 'sports':
	    commands.getoutput('adb shell input swipe 660 285 66 285')
	    commands.getoutput('adb shell input tap 534 290')
        elif status == 'night':
	    commands.getoutput('adb shell input tap 643 290')
        elif status == 'landscape':
	    commands.getoutput('adb shell input tap 512 290')
        elif status == 'portrait':
	    commands.getoutput('adb shell input tap 385 290')
        elif status == 'night-portrait':
	    commands.getoutput('adb shell input tap 285 290')
        elif status == 'barcode':
	    commands.getoutput('adb shell input tap 177 290')
        elif status == 'fireworks':
	    commands.getoutput('adb shell input tap 58 290')
	time.sleep(3)
        state = commands.getoutput(Scene_STATE)
        statevalue = state.find(status)
	assert statevalue != -1

    def setflashstatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
	time.sleep(1)
	d(description=Flash_description).click.wait()
	if status == 'on':
	    commands.getoutput('adb shell input tap 180 185')
	elif status == 'off':
	    commands.getoutput('adb shell input tap 66 185')
	elif status == 'auto':
	    commands.getoutput('adb shell input tap 291 185')
	time.sleep(3)
        state = commands.getoutput(Flash_STATE)
        statevalue = state.find(status)
	assert statevalue != -1



    def setFDFRstatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
	time.sleep(1)
	if status == 'on':
	    state = commands.getoutput(FDFR_STATE)
            statevalue = state.find(status)
	    if statevalue == -1:
		d(description=FDFR_description).click.wait()
		time.sleep(3)
		state = commands.getoutput(FDFR_STATE)
		statevalue = state.find(status)
		assert statevalue != -1
	if status == 'off':
	    state = commands.getoutput(FDFR_STATE)
            statevalue = state.find(status)
	    if statevalue == -1:
		d(description=FDFR_description).click.wait()
		time.sleep(3)
		state = commands.getoutput(FDFR_STATE)
		statevalue = state.find(status)
		assert statevalue != -1

    def sethintsstatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
	time.sleep(1)
	d(description=Setting_description).click.wait()
	commands.getoutput('adb shell input tap 192 173')
	time.sleep(1)
	if status == 'off':
	    commands.getoutput('adb shell input tap 57 285')
	    time.sleep(3)
	    state = commands.getoutput(Hints_STATE)
	    statevalue = state.find(status)
  	    assert statevalue != -1
	if status == 'on':
	    commands.getoutput('adb shell input tap 170 285')
	    time.sleep(3)
	    state = commands.getoutput(Hints_STATE)
	    statevalue = state.find(status)
  	    assert statevalue != -1

    def setlocationstatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
	time.sleep(1)
	d(description=Setting_description).click.wait()
	commands.getoutput('adb shell input tap 298 180')
	time.sleep(1)
	if status == 'off':
	    commands.getoutput('adb shell input tap 57 285')
	    time.sleep(3)
	    state = commands.getoutput(Geolocation_STATE)
	    statevalue = state.find(status)
  	    assert statevalue != -1
	if status == 'on':
	    commands.getoutput('adb shell input tap 173 285')
	    time.sleep(3)
	    state = commands.getoutput(Geolocation_STATE)
	    statevalue = state.find(status)
  	    assert statevalue != -1

    def setpicturesize(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
	time.sleep(1)
	d(description=Setting_description).click.wait()
	commands.getoutput('adb shell input tap 390 180')
	time.sleep(1)
	if status == 'WideScreen':
	    commands.getoutput('adb shell input tap 64 285')
	    time.sleep(3)
	    state = commands.getoutput(PictureSize_STATE)
	    statevalue = state.find(status)
  	    assert statevalue != -1
	if status == 'StandardScreen':
	    commands.getoutput('adb shell input tap 172 285')
	    time.sleep(3)
	    state = commands.getoutput(PictureSize_STATE)
	    statevalue = state.find(status)
  	    assert statevalue != -1

    def setexpourestatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
	time.sleep(1)
	d(description=Setting_description).click.wait()
	commands.getoutput('adb shell input tap 646 165')
	time.sleep(1)
	if status == '0':
	    commands.getoutput('adb shell input tap 285 290')
	elif status == '3':
	    commands.getoutput('adb shell input tap 400 290')
        elif status == '6':
	    commands.getoutput('adb shell input tap 520 290')
        elif status == '-3':
	    commands.getoutput('adb shell input tap 170 290')
        elif status == '-6':
	    commands.getoutput('adb shell input tap 60 290')
	time.sleep(3)
        state = commands.getoutput(Exposure_STATE)
        statevalue = state.find(status)
	assert statevalue != -1 

    def setwbstatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
	time.sleep(1)
	d(description=Setting_description).click.wait()
	commands.getoutput('adb shell input swipe 670 165 78 165')
	commands.getoutput('adb shell input tap 417 187')
	time.sleep(1)
        if status == 'auto':
            commands.getoutput('adb shell input tap 518 294')
        elif status == 'incandescent':
            commands.getoutput('adb shell input tap 411 294')
        elif status == 'daylight':
            commands.getoutput('adb shell input tap 293 294')
        elif status == 'fluorescent':
            commands.getoutput('adb shell input tap 187 294')
        elif status == 'cloudy-daylight':
            commands.getoutput('adb shell input tap 64 294')
	time.sleep(3)
        state = commands.getoutput(WhiteBalance_STATE)
        statevalue = state.find(status)
	assert statevalue != -1

    def setisostatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
	time.sleep(1)
	d(description=Setting_description).click.wait()
	commands.getoutput('adb shell input swipe 670 165 78 165')
	commands.getoutput('adb shell input tap 548 165')
	time.sleep(1)
        if status == 'iso-auto':
            commands.getoutput('adb shell input tap 527 294')
        elif status == 'iso-100':
            commands.getoutput('adb shell input tap 411 294')
        elif status == 'iso-200':
            commands.getoutput('adb shell input tap 293 294')
        elif status == 'iso-400':
            commands.getoutput('adb shell input tap 187 294')
        elif status == 'iso-800':
            commands.getoutput('adb shell input tap 64 294')
	time.sleep(3)
        state = commands.getoutput(ISO_STATE)
        statevalue = state.find(status)
	assert statevalue != -1

    def setselftimerstatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
	time.sleep(1)
	d(description=Setting_description).click.wait()
	commands.getoutput('adb shell input swipe 670 165 78 165')
	commands.getoutput('adb shell input tap 679 182')
	time.sleep(1)
        if status == '10':
            commands.getoutput('adb shell input tap 414 294')
        elif status == '5':
            commands.getoutput('adb shell input tap 295 294')
        elif status == '3':
            commands.getoutput('adb shell input tap 181 294')
        elif status == '0':
            commands.getoutput('adb shell input tap 54 294')
	time.sleep(3)
        state = commands.getoutput(SelfTimer_STATE)
        statevalue = state.find(status)
	assert statevalue != -1	

    def launchcamera(self):
	d(description='Apps').click.wait()
        while not d.exists(text='Camera'):
	    d().swipe.right()
            time.sleep(3)
        d(text='Camera').click.wait()
        d(description="Shutter button").wait.exists(timeout=3000)
        time.sleep(5)
