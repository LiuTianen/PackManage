from Utils.adbUtils import AdbTools
from Utils.PackUtils import APP
from Utils.Common import Common

class InstallCase:


    def mobileQuit(self):
        commands = []
        for devices in AdbTools().getOnlineDevices():
            cmd = AdbTools(devices).quit_app(packName)
            commands.append(cmd)
        return commands

if __name__ == '__main__':
    packName = APP().get_apk_package()
    InstallCase().mobileQuit()