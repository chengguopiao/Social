#!/usr/bin/env python
from devicewrapper.android import device as d
import commands
import re
import time

MODE_LIST_BUTTON    = 'com.intel.camera22:id/mode_button'
MODE_ID             ={'single':'com.intel.camera22:id/mode_wave_photo',
                      'smile':'com.intel.camera22:id/mode_wave_smile',
                      'hdr':'com.intel.camera22:id/mode_wave_hdr',
                      'video':'com.intel.camera22:id/mode_wave_video',
                      'burst':'com.intel.camera22:id/mode_wave_burst',
                      #'burstslow':'com.intel.camera22:id/mode_wave_burst',
                      'perfectshot':'com.intel.camera22:id/mode_wave_perfectshot',
                      'panorama':'com.intel.camera22:id/mode_wave_panorama'
                      }

RESULT              = r'^>\d<$'
HORI_LIST_BUTTON    = 'com.intel.camera22:id/hori_list_button'
FLASH_SETTING       = ['off','on','auto']

##################################################
#     Settings in each mode                      #
##################################################
SINGLE_SETTING      = ['testcamera','hits','location','picturesize','scencesmode','exposure','whitebalance','iso','delay']
SMILE_SETTING       = ['location','picturesize','sencesmode','exposure','whitebalance','iso']
HDR_SETTING         = ['location','picturesize','delay']
VIDEO_SETTING       = ['testcamera','location','videosize','exposure','whitebalance']
BURST_SETTING       = ['location','picturesize','sencesmode','exposure']
PERFECTSHOT_SETTING = ['location','scencesmode','exposure']
PANORAMA_SETTING    = ['location','exposure','iso']

MODE = {'single':SINGLE_SETTING,
        'smile':SMILE_SETTING,
        'hdr':HDR_SETTING,
        'video':VIDEO_SETTING,
        'burst':BURST_SETTING,
        'perfectshot':PERFECTSHOT_SETTING,
        'panorama':PANORAMA_SETTING
        }

XML_CONFIRM_LIST = {'hits': 'pref_camera_hints_key',
                    'location': 'pref_camera_geo_location_key',
                    'picturesize': 'pref_camera_picture_size_key',
                    'scencesmode': 'pref_camera_scenemode_key',
                    'exposure': 'pref_camera_exposure_key',
                    'whitebalance': 'pref_camera_whitebalance_key',
                    'iso': 'pref_camera_iso_key',
                    'delay': 'pref_camera_delay_shooting_key',
                    'videosize': 'pref_video_quality_key'
                    }
#################################################################################################################
def switchcamera(mode):
    d(resourceId = MODE_LIST_BUTTON).click.wait()
    time.sleep(2)
    d(resourceId = MODE_ID[mode]).click.wait()

def _setFlashMode(option):
    d(resourceId = 'com.intel.camera22:id/left_menus_flash_setting').click.wait()
    d(resourceId = 'com.intel.camera22:id/hori_list_button')[FLASH_SETTING.index(option)].click.wait()

def setCameraSetting(mode,sub_mode,option):
    '''
    This method is used to set camera to one mode, sub-mode, and do any operate of this sub-mode.
    7 = Max element count in screen.
    2 = Length of settings - Max screen count

    Please input index number as sub_mode, input index number of options as option
    Such as:
    setCameraSetting('single',3,2)
    'single' means mode
    3 means the index number of Location in sub_mode list
    2 means the index number of Location off option in options list
    '''
    
    settings = MODE[mode]
    if sub_mode== 'flash':
        _setFlashMode(option)
    else:
        d(resourceId = 'com.intel.camera22:id/left_menus_camera_setting').click.wait(timeout=2000)

        if sub_mode <= 7:
            d(resourceId = HORI_LIST_BUTTON)[sub_mode-1].click.wait()
            if len(settings) >= 7:
                d(resourceId = HORI_LIST_BUTTON)[option+7-1].click.wait()
            else:
                d(resourceId = HORI_LIST_BUTTON)[option+len(settings)-1].click.wait()
        elif 7<sub_mode<=9 :
            d.swipe(680,180,100,180)
            d(resourceId = HORI_LIST_BUTTON)[sub_mode-2-1].click.wait()
            d(resourceId = HORI_LIST_BUTTON)[option+7-1].click.wait()
        else:
            raise Exception('Index is out of range!')
        return True
#        if setting == 'location':
#            result = commands.getoutput('adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep ' + XML_CONFIRM_LIST[setting])
#        else:
#            result = commands.getoutput('adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep ' + XML_CONFIRM_LIST[setting])
#        print result
#        return result

