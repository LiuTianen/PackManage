# coding=utf-8
from Base.Common import Common
from Base.DevicesList import devicesList as dl


class PackInstall:

    # 推送APK，并安装
    def installApk(self, apk_path):
        connectDevices = dl().get_MobileName()
        commands =[]

        for device in connectDevices:
            cmd = "adb -s %s install -r %s" % (device,apk_path)
            commands.append(cmd)
        Common().loop_threads(commands)


if __name__ == '__main__':
    apk_path = "C:\\Users\\YongYI\\Downloads\\com.estrongs.android.pop_10067.apk"
    PackInstall().installApk(apk_path)

