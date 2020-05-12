# coding=utf-8

from Base.DevicesList import devicesList as dl
from Base.Common import Common

class DevicesConnect:

    def deviceConnect(self):
        commands = []
        data = dl().get_Tv_IP()
        for IP in data:
            cmd = "adb connect %s" %(IP)
            commands.append(cmd)
        Common().loop_threads(commands)

if __name__ == '__main__':
    DevicesConnect().deviceConnect()
