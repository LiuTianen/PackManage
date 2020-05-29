# coding=utf-8
from Base.PackName import APP
from Base.Common import Common
from Base.keyCode import KeyCode
from Base.DevicesList import devicesList as dl
from Base.ADB import Adb


class MobileCase:
    def __init__(self):
        self.packName = APP().get_apk_package()


    def MobileUninstall(self):
        connectDevices = dl().get_mobileDevices()
        commands = []
        for device in connectDevices:
            cmd = Adb().adbUninstall(device,self.packName)
            commands.append(cmd)
        Common().loop_threads(commands)

    def MobileInstall(self, apk_path):
        connectDevices = dl().get_mobileDevices()
        commands =[]
        for device in connectDevices:
            cmd = Adb().adbInstall( device,apk_path)
            commands.append(cmd)
        Common().loop_threads(commands)

    def MobileAppRun(self):
        launchable_activity = APP().get_apk_activity()
        pack_lauch = self.packName +"/"+ launchable_activity
        connectDevices = dl().get_mobileDevices()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s shell am start -n %s" % (device, pack_lauch)
            commands.append(cmd)
        Common().loop_threads(commands)

    def mobileAppQuite(self):
        connectDevices = dl().get_mobileDevices()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s shell am force-stop %s" % (device, self.packName)
            commands.append(cmd)
        Common().loop_threads(commands)

    def mobileAppTop(self):
        connectDevices = dl().get_mobileDevices()
        commands = []
        for device in connectDevices:
            adbTop = Adb().adbTop(device)
            commands.append(adbTop)
        return commands

    def mobileAppLogcat(self):
        connectDevices = dl().get_mobileDevices()
        commands = []
        for device in connectDevices:
            adbLogcat = Adb().adbLogcat(device)
            commands.append(adbLogcat)
        return commands

    def MobileAppClear(self):
        connectDevices = dl().get_mobileDevices()
        commands = []
        for device in connectDevices:
            adbClear = Adb().adbClear(device, self.packName)
            commands.append(adbClear)
        Common().loop_threads(commands)

    def mobileHome(self):
        connectDevices = dl().get_mobileDevices()
        commands = []
        for device in connectDevices:
            mobileHome = KeyCode().KEYCODE_HOME(device)
            commands.append(mobileHome)
        Common().loop_threads(commands)

    def mobileBack(self):
        connectDevices = dl().get_mobileDevices()
        commands = []
        for device in connectDevices:
            mobileBack = KeyCode().KeyCode_Back(device)
            commands.append(mobileBack)
        Common().loop_threads(commands)

if __name__ == '__main__':
    apk_path = []
    # packName = []