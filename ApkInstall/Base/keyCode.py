import subprocess
import time
import threading
import os
import configparser

class KeyCode:
    cf = configparser.ConfigParser()
    cf.read('Config.ini', encoding="utf-8")


    def KEYCODE_HOME(self, adbDevices):
        adbs = "adb -s %s shell input keyevent KEYCODE_HOME" % (adbDevices)
        KEYCODE_HOME = os.system(adbs)
        return KEYCODE_HOME

    def KeyCode_Back(self, adbDevices):
        adbs = "adb -s %s shell input keyevent KEYCODE_BACK" % (adbDevices)
        KeyCode_Back = os.system(adbs)
        return KeyCode_Back

if __name__ == '__main__':
    adbDevices = []