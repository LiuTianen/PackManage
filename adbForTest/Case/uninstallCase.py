#!/usr/bin/env python
#coding=utf-8

from Utils.adbUtils import AdbTools
from Utils.Common import Common

class UninstallCase:


    def AppUninstall(self):
        commands = []
        for devices in AdbTools().getOnlineDevices():
            cmd = AdbTools(devices).uninstall(packName)
            commands.append(cmd)
        return commands

if __name__ == '__main__':
    path = Common().apkPath()
    packName = AdbTools().dump_apk_name(path)
    UninstallCase().AppUninstall()