# coding=utf-8
from Base.PackName import APP
from Base.DevicesList import devicesList as dl
from Base.Common import Common

class PackLaunch:

    def lauchApp(self):
        launchable_activity = APP().get_apk_activity()
        packName = APP().get_apk_package()
        pack_lauch = packName +"/"+ launchable_activity
        connectDevices = dl().get_Tv_IP()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s shell am start -n %s" % (device, pack_lauch)
            commands.append(cmd)
        Common().loop_threads(commands)

if __name__ == '__main__':
    PackLaunch().lauchApp()