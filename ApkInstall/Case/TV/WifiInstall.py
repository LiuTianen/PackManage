# coding=utf-8
from Base.DevicesList import devicesList as dl
from Base.Common import Common

class WifiInstall:

    def wifiInstall(self, apk_path):
        connectDevices = dl().get_Tv_IP()
        commands = []

        for device in connectDevices:
            cmd = "adb -s %s install -r %s" %(device, apk_path)
            commands.append(cmd)
        Common().loop_threads(commands)

if __name__ == '__main__':
    apk_path = "C:\\Users\\YongYI\\Downloads\\com.estrongs.android.pop_10067.apk"
    WifiInstall().wifiInstall(apk_path)