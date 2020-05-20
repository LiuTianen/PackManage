# coding=utf-8

from Base.DevicesList import devicesList as dl
from Base.Common import Common
from Base.PackName import APP

class TvCase:

    def __init__(self):
        self.packName = APP().get_apk_package()

    def tvConnect(self):
        commands = []
        data = dl().get_tvDevices()
        for IP in data:
            cmd = "adb connect %s" % (IP)
            commands.append(cmd)
        Common().loop_threads(commands)


    def tvUninstall(self):
        connectDevices = dl().get_tvDevices()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s uninstall %s" % (device, self.packName)
            commands.append(cmd)
        Common().loop_threads(commands)

    def tvInstall(self,apk_path):
        connectDevices = dl().get_tvDevices()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s install -r %s" % (device, apk_path)
            commands.append(cmd)
        Common().loop_threads(commands)

    def tvAppRun(self):
        launchable_activity = APP().get_apk_activity()
        # packName = APP().get_apk_package()
        pack_lauch = self.packName + "/" + launchable_activity
        connectDevices = dl().get_tvDevices()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s shell am start -n %s" % (device, pack_lauch)
            commands.append(cmd)
        Common().loop_threads(commands)

    def tvAppKill(self):
        connectDevices = dl().get_tvDevices()
        # packName = APP().get_apk_package()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s shell am force-stop %s" % (device, self.packName)
            commands.append(cmd)
        Common().loop_threads(commands)

    def tvAppTop(self):
        connectDevices = dl().get_tvDevices()
        commands = []
        for device in connectDevices:
            adbTop = Common().adbTop(device)
            commands.append(adbTop)
        return commands

    def tvAppLogcat(self):
        connectDevices = dl().get_tvDevices()
        commands = []
        for device in connectDevices:
            adbLogcat = Common().adbLogcat(device)
            commands.append(adbLogcat)
        return commands

    def tvAppClear(self):
        connectDevices = dl().get_tvDevices()
        commands = []
        for device in connectDevices:
            adbClear = Common().adbClear(device, self.packName)
            commands.append(adbClear)
        Common().loop_threads(commands)


if __name__ == '__main__':
    apk_path = []
