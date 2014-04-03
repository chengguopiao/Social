#!/usr/bin/env python
import unittest
import string
import os
import commands
import time
#import util_xiao
#import util_social
from devicewrapper.android import device as d

PACKAGE_NAME = 'com.intel.camera22'
ACTIVITY_NAME = PACKAGE_NAME + '/' + '.Camera'
DCIM_PATH = '/sdcard/DCIM'
MODE_LIST_BUTTON = 'Show switch camera mode list'
# MODE = {'single':'com.intel.camera22:id/mode_wave_photo',
#         'smile':'com.intel.camera22:id/mode_wave_smile',
#         'hdr':'com.intel.camera22:id/mode_wave_hdr',
#         'video':'com.intel.camera22:id/mode_wave_video',
#         'burstfast':'com.intel.camera22:id/mode_wave_burst',
#         #'burstslow':'com.intel.camera22:id/mode_wave_burst',
#         'perfectshot':'com.intel.camera22:id/mode_wave_perfectshot',
#         'panorama':'com.intel.camera22:id/mode_wave_panorama'
#         }


HITS = ['off', 'on']
LOCATION = ['off','on']
PICTURE_SIZE = ['widescreen','standard']
SENCES_MODE = ['barcode','niget-portrait','portrait','landscape','night','sport','auto']
EXPOURSE = ['-2','-1','0','1','2']
WHITEBALANCE = ['cloudy','fluorescent','daylight','incandescent','auto']
ISO = ['800','400','200','100','0']
DELAY = ['0','3','5','10']
TESTCAMERA = None

SINGLE_SETTING = ['testcamera','hits','location','picturesize','scencesmode','expourse','whitebalance','iso','delay']

OPTION = {SINGLE_SETTING[0]:TESTCAMERA,
          SINGLE_SETTING[1]:HITS,
          SINGLE_SETTING[2]:LOCATION,
          SINGLE_SETTING[3]:PICTURE_SIZE,
          SINGLE_SETTING[4]:SENCES_MODE,
          SINGLE_SETTING[5]:EXPOURSE,
          SINGLE_SETTING[6]:WHITEBALANCE,
          SINGLE_SETTING[7]:ISO,
          SINGLE_SETTING[8]:DELAY,
          }
FLASH_SETTING = ['off','on','auto']


class MyTest(unittest.TestCase):

    def setUp(self):
        super(MyTest,self).setUp()

    def tearDown(self):
        d.press.home()
        super(MyTest,self).tearDown()

    # Test case 1
    def testSetSingleCameraA(self):
        """
        Summary:This method is use to test social_util
        """
        d.start_activity(component = ACTIVITY_NAME)
        self._setSingleCameraSetting('hits','on')
        print 'test over'

    # Test case 2
    def testSetSingleCameraB(self):
        """
        Summary:This method is use to test social_util
        """
        d.start_activity(component = ACTIVITY_NAME)
        self._setSingleCameraSetting('hits','off')
        print 'test over'

    # Test case 3
    def testSetSingleCameraC(self):
        """
        Summary:This method is use to test social_util
        """
        d.start_activity(component = ACTIVITY_NAME)
        self._setSingleCameraSetting('expourse','-1')
        print 'test over'

    # Test case 4
    def testSetSingleCameraD(self):
        """
        Summary:This method is use to test social_util
        """
        d.start_activity(component = ACTIVITY_NAME)
        self._setSingleCameraSetting('delay','5')
        print 'test over'

    def _setCameraMode(self,mode):
        d(description = MODE_LIST_BUTTON).click.wait(timeout = 2000)
        d(resourceId = MODE[mode]).click.wait(timeout = 2000)

    # def _setCameraMode(self,mode):
    #     d(resourceId = MODE_LIST_BUTTON).click.wait(timeout=3000)
    #     d(resourceId = MODE[mode]).click.wait(timeout=3000)

    def _setSingleCameraSetting(self,setting,option):
        if setting == 'flash':
            d(resourceId = 'com.intel.camera22:id/left_menus_flash_setting').click.wait()
            d(resourceId = 'com.intel.camera22:id/hori_list_button')[FLASH_SETTING.index(option)].click.wait()
        else:
            d(resourceId = 'com.intel.camera22:id/left_menus_camera_setting').click.wait(timeout=2000)
            if SINGLE_SETTING.index(setting)<=6:        # 6 is the max index element in the screen
                d(resourceId = 'com.intel.camera22:id/hori_list_button')[SINGLE_SETTING.index(setting)].click.wait()
                d(resourceId = 'com.intel.camera22:id/hori_list_button')[OPTION[setting].index(option)+7].click.wait()
            else:
                d.swipe(680,180,100,180)
                d(resourceId = 'com.intel.camera22:id/hori_list_button')[SINGLE_SETTING.index(setting)-2].click.wait()
                d(resourceId = 'com.intel.camera22:id/hori_list_button')[OPTION[setting].index(option)+7].click.wait()                
