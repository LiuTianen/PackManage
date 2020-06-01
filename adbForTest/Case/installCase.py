#!/usr/bin/env python
#coding=utf-8

from Utils.adbUtils import AdbTools
from Utils.Common import Common
from Utils.OtherDevices import otherDevices

class InstallCase:

    def Appinstall(self):
        #全部在线设备的安装
        commands = []
        for devices in AdbTools().getOnlineDevices():
            cmd = AdbTools(devices).install(path)
            commands.append(cmd)
        return commands

    def mobileInstall(self):
        #只安装列表里的手机设备
        commands = []
        for devices in otherDevices().get_mobileDevices():
            cmd = AdbTools(devices).install(path)
            commands.append(cmd)
        return commands

    def tvInstall(self):
        #只安装列表里的TV设备
        commands = []
        for devices in otherDevices().get_tvDevices():
            cmd = AdbTools(devices).install(path)
            commands.append(cmd)
        return commands

if __name__ == '__main__':
    path = Common().apkPath()
    InstallCase().tvInstall()