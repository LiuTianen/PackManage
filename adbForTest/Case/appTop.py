#!/usr/bin/env python
#coding=utf-8


from Utils.adbUtils import AdbTools
from Utils.Common import Common


class adbTop:

    def appTop(self):
        #全部在线设备的安装
        commands = []
        for devices in AdbTools().getOnlineDevices():
            cmd = Common().adbTop(devices)
            commands.append(cmd)
        return commands

if __name__ == '__main__':
    # path = Common().logTag()
    adbTop().appTop()