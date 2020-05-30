#!/usr/bin/env python
#coding=utf-8

from Utils.adbUtils import AdbTools
from Utils.PackUtils import APP
from Utils.Common import Common

class UninstallCase:


    def mobileUninstall(self):
        commands = []
        for devices in AdbTools().getOnlineDevices():
            cmd = AdbTools(devices).uninstall(packName)
            commands.append(cmd)
        return commands

if __name__ == '__main__':
    packName = APP().get_apk_package()
    UninstallCase().mobileUninstall()