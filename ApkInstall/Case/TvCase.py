# coding=utf-8

from Base.DevicesList import devicesList as dl
from Base.Common import Common
from Base.PackName import APP

class TvCase:

    def tvConnect(self):
        commands = []
        data = dl().get_Tv_IP()
        for IP in data:
            cmd = "adb connect %s" % (IP)
            commands.append(cmd)
        Common().loop_threads(commands)


    def tvUninstall(self):
        packName = APP().get_apk_package()

        connectDevices = dl().get_Tv_IP()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s uninstall %s" % (device, packName)
            commands.append(cmd)
        Common().loop_threads(commands)

    def tvInstall(self,apk_path):
        connectDevices = dl().get_Tv_IP()
        commands = []

        for device in connectDevices:
            cmd = "adb -s %s install -r %s" % (device, apk_path)
            commands.append(cmd)
        Common().loop_threads(commands)

    def tvAppRun(self):
        launchable_activity = APP().get_apk_activity()
        packName = APP().get_apk_package()
        pack_lauch = packName + "/" + launchable_activity
        connectDevices = dl().get_Tv_IP()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s shell am start -n %s" % (device, pack_lauch)
            commands.append(cmd)
        Common().loop_threads(commands)

if __name__ == '__main__':
    apk_path = []
    TvCase().tvConnect()
    TvCase().tvUninstall()
    TvCase().tvInstall(apk_path)
    TvCase().tvAppRun()