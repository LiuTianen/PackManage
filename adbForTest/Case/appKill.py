#!/usr/bin/env python
#coding=utf-8

from Utils.adbUtils import AdbTools
from Utils.PackUtils import APP
from Utils.Common import Common
"""
需要root权限，暂时放弃先使用force-stop + am clear 来代替杀进程
"""

class AppKill:

    def AppKill(self):
        appName = AdbTools().dump_apk_name(path)
        # pid = AdbTools().get_pid(appName)
        commands = []
        for devices in AdbTools().getOnlineDevices():
            cmd = AdbTools(devices).kill_process(appName)
            commands.append(cmd)
        return commands


if __name__ == '__main__':
    packName = APP().get_apk_package()
    path = 'C:\\Users\\YongYI\\Downloads\\CPU-Z.apk'
    AppKill().AppKill()
    # print(AppKill().AppKill())