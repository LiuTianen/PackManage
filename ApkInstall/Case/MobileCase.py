# coding=utf-8
from Base.PackName import APP
from Base.Common import Common
from Base.DevicesList import devicesList as dl

class MobileCase:

    def MobileUninstall(self):
        packName = APP().get_apk_package()
        connectDevices = dl().get_mobileDevices()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s uninstall %s" % (device, packName)
            commands.append(cmd)
        Common().loop_threads(commands)

    def MobileInstall(self, apk_path):
        connectDevices = dl().get_mobileDevices()
        commands =[]

        for device in connectDevices:
            cmd = "adb -s %s install -r %s" % (device,apk_path)
            commands.append(cmd)
        Common().loop_threads(commands)

    def MobileAppRun(self):
        launchable_activity = APP().get_apk_activity()
        packName = APP().get_apk_package()
        pack_lauch = packName +"/"+ launchable_activity
        connectDevices = dl().get_mobileDevices()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s shell am start -n %s" % (device, pack_lauch)
            commands.append(cmd)
        Common().loop_threads(commands)

    def mobileApp_Kill(self):
        connectDevices = dl().get_mobileDevices()
        packName = APP().get_apk_package()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s shell am force-stop %s" % (device, packName)
            commands.append(cmd)
        Common().loop_threads(commands)

    def mobileAppTop(self):
        connectDevices = dl().get_mobileDevices()
        commands = []
        for device in connectDevices:
            adbTop = Common().adbTop(device)
            commands.append(adbTop)
        return commands

    def mobileAppLogcat(self):
        connectDevices = dl().get_mobileDevices()
        commands = []
        for device in connectDevices:
            adbLogcat = Common().adbLogcat(device)
            commands.append(adbLogcat)
        return commands

if __name__ == '__main__':
    apk_path = []
    MobileCase().MobileUninstall()
    MobileCase().MobileInstall(apk_path)
    MobileCase().MobileAppRun()
    MobileCase().mobileApp_Kill()
    MobileCase().mobileAppTop()