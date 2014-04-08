#!/usr/bin/env python
#import unittest,string
#import commands
#import sys
#import time
from devicewrapper.android import device as d

# MODE_LIST_BUTTON = 'com.intel.camera22:id/mode_button'
# MODE = {'single':'com.intel.camera22:id/mode_wave_photo',
#         'smile':'com.intel.camera22:id/mode_wave_smile',
#         'hdr':'com.intel.camera22:id/mode_wave_hdr',
#         'video':'com.intel.camera22:id/mode_wave_video',
#         'burstfast':'com.intel.camera22:id/mode_wave_burst',
#         #'burstslow':'com.intel.camera22:id/mode_wave_burst',
#         'perfectshot':'com.intel.camera22:id/mode_wave_perfectshot',
#         'panorama':'com.intel.camera22:id/mode_wave_panorama'
#         }

HORI_LIST_BUTTON = 'com.intel.camera22:id/hori_list_button'
FLASH_SETTING = ['off','on','auto']

#################################################################################################################
'''
Options detail as below
'''
HITS = ['off', 'on']
LOCATION = ['off','on']
PICTURE_SIZE = ['widescreen','standard']
SENCES_MODE = ['barcode','niget-portrait','portrait','landscape','night','sport','auto']
EXPOURSE = ['-2','-1','0','1','2']
WHITEBALANCE = ['cloudy','fluorescent','daylight','incandescent','auto']
ISO = ['800','400','200','100','0']
DELAY = ['0','3','5','10']
VIDEO_SIZE = ['sd','hd','hshd','fhd','hsfhd']
TESTCAMERA = None

'''
Settings in each mode
'''
SINGLE_SETTING = ['testcamera','hits','location','picturesize','scencesmode','expourse','whitebalance','iso','delay']
SMILE_SETTING = ['location','picturesize','sencesmode','expourse','whitebalance','iso']
HDR_SETTING = ['location','picturesize','delay']
VIDEO_SETTING = ['testcamera','location','videosize','expourse','whitebalance']
BURST_SETTING = ['location','picturesize','sencesmode','expourse']
PERFECTSHOT_SETTING = ['location','scencesmode','expourse']
PANORAMA_SETTING = ['location','expourse','iso']

################################################################################################
# MODES = {
#     SINGLE: {
#         'testcamera':{
#             'index':0, 'options':['off', 'on']
#         },
#         'hits':{
#             index:1, options:['off', 'on']
#         },

#     }
#     SMILE: {

#     }
  
# }

# MODES = {
#     SINGLE: [['off', 'on'],
#         [],
#         [],
#     ],
#     SMILE: {

#     }
  
# }


#################################################################################################################
'''
Options in each setting of mode
'''
SINGLE_OPTION ={SINGLE_SETTING[0]:TESTCAMERA,
                SINGLE_SETTING[1]:HITS,
                SINGLE_SETTING[2]:LOCATION,
                SINGLE_SETTING[3]:PICTURE_SIZE,
                SINGLE_SETTING[4]:SENCES_MODE,
                SINGLE_SETTING[5]:EXPOURSE,
                SINGLE_SETTING[6]:WHITEBALANCE,
                SINGLE_SETTING[7]:ISO,
                SINGLE_SETTING[8]:DELAY
                }
SMILE_OPTION = {SMILE_SETTING[0]:LOCATION,
                SMILE_SETTING[1]:PICTURE_SIZE,
                SMILE_SETTING[2]:SENCES_MODE,
                SMILE_SETTING[3]:EXPOURSE,
                SMILE_SETTING[4]:WHITEBALANCE,
                SMILE_SETTING[5]:ISO
                }
HDR_OPTION = {HDR_SETTING[0]:LOCATION,
              HDR_SETTING[1]:PICTURE_SIZE,
              HDR_SETTING[2]:DELAY
              }
VIDEO_OPTION = {VIDEO_SETTING[0]:TESTCAMERA,
                VIDEO_SETTING[1]:LOCATION,
                VIDEO_SETTING[2]:VIDEO_SIZE,
                VIDEO_SETTING[3]:EXPOURSE,
                VIDEO_SETTING[4]:WHITEBALANCE
                }
BURST_OPTION = {BURST_SETTING[0]:LOCATION,
                BURST_SETTING[1]:PICTURE_SIZE,
                BURST_SETTING[2]:SENCES_MODE,
                BURST_SETTING[3]:WHITEBALANCE
                }
PERFECTSHOT_OPTION = {PERFECTSHOT_SETTING[0]:LOCATION,
                      PERFECTSHOT_SETTING[1]:SENCES_MODE,
                      PERFECTSHOT_SETTING[2]:EXPOURSE
                      }
PANORAMA_OPTION ={PANORAMA_SETTING[0]:LOCATION,
                  PANORAMA_SETTING[1]:EXPOURSE,
                  PANORAMA_SETTING[2]:ISO
                  }

MODE = {'single':[SINGLE_SETTING,SINGLE_OPTION],
        'smile':[SMILE_SETTING,SMILE_OPTION],
        'hdr':[HDR_SETTING,HDR_OPTION],
        'video':[VIDEO_SETTING,VIDEO_OPTION],
        'burst':[BURST_SETTING,BURST_OPTION],
        'perfectshot':[PERFECTSHOT_SETTING,PERFECTSHOT_OPTION],
        'panorama':[PANORAMA_SETTING,PANORAMA_OPTION]
        }
#################################################################################################################
# def setCameraMode(mode):
#     d(resourceId = MODE_LIST_BUTTON).click.wait(timeout=3000)
#     d(resourceId = MODE[mode]).click.wait(timeout=3000)
def _setFlashMode(option):
    d(resourceId = 'com.intel.camera22:id/left_menus_flash_setting').click.wait()
    d(resourceId = 'com.intel.camera22:id/hori_list_button')[FLASH_SETTING.index(option)].click.wait()


# def setSingleCameraSetting(mode,setting,option):
#     if setting == 'flash':
#         _setFlashMode(option)
#     else:
#         d(resourceId = 'com.intel.camera22:id/left_menus_camera_setting').click.wait(timeout=2000)
#         if SINGLE_SETTING.index(setting)<=len(SINGLE_SETTING):        # 6 is the max index element in the screen
#             d(resourceId = HORI_LIST_BUTTON)[SINGLE_SETTING.index(setting)].click.wait()
#             d(resourceId = HORI_LIST_BUTTON)[SINGLE_OPTION[setting].index(option)+len(SINGLE_SETTING)].click.wait()
#         else:
#             d.swipe(680,180,100,180)
#             d(resourceId = HORI_LIST_BUTTON)[SINGLE_SETTING.index(setting)-2].click.wait()
#             d(resourceId = HORI_LIST_BUTTON)[SINGLE_OPTION[setting].index(option)+len(SINGLE_SETTING)].click.wait()
def setCameraSetting(mode,setting,option):
    settings = MODE[mode][0]
    options = MODE[mode][1]
    if setting == 'flash':
        _setFlashMode(option)
    else:
        d(resourceId = 'com.intel.camera22:id/left_menus_camera_setting').click.wait(timeout=2000)
        if SINGLE_SETTING.index(setting)<=len(settings):        # 6 is the max index element in the screen
            d(resourceId = HORI_LIST_BUTTON)[settings.index(setting)].click.wait()
            d(resourceId = HORI_LIST_BUTTON)[options[setting].index(option)+len(settings)].click.wait()
        else:
            d.swipe(680,180,100,180)
            d(resourceId = HORI_LIST_BUTTON)[settings.index(setting)-2].click.wait()
            d(resourceId = HORI_LIST_BUTTON)[options[setting].index(option)+len(settings)].click.wait()


# def setSmileCameraSetting(setting,option):
#     if setting == 'flash':
#         _setFlashMode(option)
#     else:
#         d(resourceId = 'com.intel.camera22:id/left_menus_camera_setting').click.wait(timeout=2000)
#         d(resourceId = HORI_LIST_BUTTON)[SMILE_SETTING.index(setting)].click.wait()
#         d(resourceId = HORI_LIST_BUTTON)[SMILE_OPTION[setting].index(option)+len(SMILE_SETTING)].click.wait()

# def setHDRCameraSetting(setting,option):
#     d(resourceId = 'com.intel.camera22:id/left_menus_camera_setting').click.wait(timeout=2000)
#     d(resourceId = HORI_LIST_BUTTON)[HDR_SETTING.index(setting)].click.wait()
#     d(resourceId = HORI_LIST_BUTTON)[HDR_OPTION[setting].index(option)+len(HDR_SETTING)].click.wait()

# def setVideoCameraSetting(setting,option):
#     if setting == 'flash':
#         _setFlashMode(option)
#     else:
#         d(resourceId = 'com.intel.camera22:id/left_menus_camera_setting').click.wait(timeout=2000)
#         d(resourceId = HORI_LIST_BUTTON)[SMILE_SETTING.index(setting)].click.wait()
#         d(resourceId = HORI_LIST_BUTTON)[SMILE_OPTION[setting].index(option)+len(SMILE_SETTING)].click.wait()

# def setBurstCameraSetting(setting,option):
#     d(resourceId = 'com.intel.camera22:id/left_menus_camera_setting').click.wait(timeout=2000)
#     d(resourceId = HORI_LIST_BUTTON)[BURST_SETTING.index(setting)].click.wait()
#     d(resourceId = HORI_LIST_BUTTON)[BURST_OPTION[setting].index(option)+len(BURST_SETTING)].click.wait()

# def setPerfectshotCameraSetting(setting,option):
#     d(resourceId = 'com.intel.camera22:id/left_menus_camera_setting').click.wait(timeout=2000)
#     d(resourceId = HORI_LIST_BUTTON)[PERFECTSHOT_SETTING.index(setting)].click.wait()
#     d(resourceId = HORI_LIST_BUTTON)[PERFECTSHOT_OPTION[setting].index(option)+len(PERFECTSHOT_SETTING)].click.wait()

# def setBurstCameraSetting(setting,option):
#     d(resourceId = 'com.intel.camera22:id/left_menus_camera_setting').click.wait(timeout=2000)
#     d(resourceId = HORI_LIST_BUTTON)[PANORAMA_SETTING.index(setting)].click.wait()
#     d(resourceId = HORI_LIST_BUTTON)[PANORAMA_OPTION[setting].index(option)+len(PANORAMA_SETTING)].click.wait()