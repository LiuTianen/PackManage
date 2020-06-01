#!/usr/bin/env python
#coding=utf-8

from Utils.adbUtils import AdbTools
from Utils.Common import Common
from Utils.OtherDevices import otherDevices

class appClear:


    def appClear(self):
        commands = []
        for devices in AdbTools().getOnlineDevices():
            cmd = AdbTools(devices).clear_app_data(packName)
            commands.append(cmd)
        return commands

    def mobileClear(self):
        commands = []
        for devices in otherDevices().get_mobileDevices():
            cmd = AdbTools(devices).clear_app_data(packName)
            commands.append(cmd)
        return commands

    def tvClear(self):
        commands = []
        for devices in otherDevices().get_tvDevices():
            cmd = AdbTools(devices).clear_app_data(packName)
            commands.append(cmd)
        return commands

if __name__ == '__main__':
    path = Common().apkPath()
    packName = AdbTools().dump_apk_name(path)
    appClear().appClear()