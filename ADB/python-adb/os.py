import os

os.system('adb version')

os.system('adb shell screencap -p /sdcard/adbscreenshot/screenshot.png')
os.system('adb pull /sdcard/adbscreenshot/screenshot.png C:\Bruce\screenshotsaver\screenshot.png')
os.system('adb shell rm /sdcard/adbscreenshot/screenshot.png')
