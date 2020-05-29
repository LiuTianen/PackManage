from Utils.adbUtils import AdbTools
from Utils.PackUtils import APP
from Utils.Common import Common

class InstallCase:


    def mobileRun(self):
        commands = []
        for devices in AdbTools().getOnlineDevices():
            cmd = AdbTools(devices).start_application(packName)
            commands.append(cmd)
        return commands

if __name__ == '__main__':
    packName = APP().get_apk_package()+ '/'+APP().get_apk_activity()
    InstallCase().mobileRun()