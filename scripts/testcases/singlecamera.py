#!/usr/bin/env python
from devicewrapper.android import device as d
import util_social_new
import time
from adb import Adb
import unittest
import random
import commands

MODE      = ('single','smile','hdr','video','burst','perfectshot','panorama')
SUB_MODE  = range(1,9)
OPTION    = range(1,2)


class MyTest(unittest.TestCase):

    def setUp(self):
        Adb().cmd('launch','com.intel.camera22/.Camera')
        super(MyTest,self).setUp()

    def tearDown(self):
        d.press.home()
        super(MyTest,self).tearDown()

    # Random choice a mode to set.
    def testSetCamera(self):
        """
        Summary:This method is used to test social_util
        """
        for count in range (0,100):
            mode     = random.choice(MODE)
            sub_mode = random.choice(SUB_MODE)
            option = random.choice(OPTION)
            util_social_new.switchcamera(mode)
            util_social_new.setCameraSetting('mode',sub_mode,option)
            print mode,sub_mode,option
            result1 = commands.getoutput('adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml ')
            result2 = commands.getoutput('adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml ')
            print result1,result2
            d.press.home()