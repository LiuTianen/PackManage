# coding=utf-8
from Base.PackName import APP
from Base.Common import Common
from Base.OnlineDevices import OnelineDevices as od

class UnInstall:


    def Uninstall(self):
        packName = APP().get_apk_package()

        connectDevices = od().get_conn_dev()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s uninstall %s" % (device,packName)
            commands.append(cmd)
        Common().loop_threads(commands)


if __name__ == '__main__':
    UnInstall().Uninstall()
