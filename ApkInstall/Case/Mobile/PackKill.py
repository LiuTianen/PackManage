# coding=utf-8
from Base.DevicesList import devicesList as dl
from Base.PackName import APP
from Base.Common import Common

class AppStop:

    def mobileApp(self):
        connectDevices = dl().get_MobileName()
        packName = APP().get_apk_package()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s shell am force-stop %s" % (device, packName)
            commands.append(cmd)
        Common().loop_threads(commands)

if __name__ == '__main__':
    AppStop().mobileApp()