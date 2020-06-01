#!/usr/bin/env python
#coding=utf-8

from Utils.adbUtils import AdbTools
from Utils.Common import Common

class InstallCase:


    def Appinstall(self):
        commands = []
        for devices in AdbTools().getOnlineDevices():
            cmd = AdbTools(devices).install(path)
            commands.append(cmd)
        return commands

if __name__ == '__main__':
    path = Common().apkPath()
    InstallCase().Appinstall()
    # print(InstallCase().mobileInstall())