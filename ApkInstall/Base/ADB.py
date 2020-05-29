import subprocess
import time
import re
import os
import configparser
import platform

cf = configparser.ConfigParser()
cf.read('Config.ini', encoding="utf-8")
system = platform.system()

if system is "Windows":
    find_util = "findstr"
else:
    find_util = "grep"

class Adb:

    def adbInstall(self,device, apk_path):
        adbInstall  = "adb -s %s install -r %s" % (device, apk_path)
        return adbInstall

    def adbUninstall(self,device, packName):
        adbUninstall = "adb -s %s uninstall %s" % (device, packName)
        return adbUninstall

    def adbDisconnect(self):
        Disc = os.popen('adb disconnect')
        return Disc

    def adbRestart(self):
        restart = os.popen('adb kill-server &&adb devices')
        return restart

    def adbTop(self,adbDevices):
        adbs = 'start cmd /k "adb -s %s shell top -m 10"' %(adbDevices)
        Top = os.system(adbs)
        return Top

    def adbClear(self, adbDevices, packageName):
        adbClear = 'adb -s %s shell pm clear %s' %(adbDevices, packageName)
        return adbClear

    def adbLogcat(self,adbDevices):
        logTag = cf.get("Common", "logTag")
        adbs = 'start cmd /k "adb -s %s logcat %s"' % (adbDevices, logTag)
        adbLogcat = os.system(adbs)
        return adbLogcat

    def cmdKill(self):
        adbs = 'start cmd /k "tskill adb && tskill cmd"'
        kill = os.system(adbs)
        return kill

if __name__ == '__main__':
    pass
