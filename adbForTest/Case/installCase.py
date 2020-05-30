#!/usr/bin/env python
#coding=utf-8

from Utils.adbUtils import AdbTools
from Utils.PackUtils import APP
from Utils.Common import Common

class InstallCase:


    def mobileInstall(self):
        commands = []
        for devices in AdbTools().getOnlineDevices():
            cmd = AdbTools(devices).install(appPath)
            commands.append(cmd)
        return commands

if __name__ == '__main__':
    appPath = Common().apkPath()
    InstallCase().mobileInstall()
    # print(InstallCase().mobileInstall())