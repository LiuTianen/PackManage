# coding=utf-8
from Base.PackName import APP
from Base.DevicesList import devicesList as dl
from Base.Common import Common

class UnInstall:


    def Uninstall(self):
        packName = APP().get_apk_package()

        connectDevices = dl().get_Tv_IP()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s uninstall %s" % (device,packName)
            commands.append(cmd)
        Common().loop_threads(commands)

if __name__ == '__main__':
    UnInstall().Uninstall()
