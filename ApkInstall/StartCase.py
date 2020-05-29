# coding=utf-8
from Case.MobileCase import MobileCase
from Case.TvCase import TvCase
from Base.ADB import Adb
from Base.Common import Common
import time
from Base.PackName import APP


class startInit:

    def Case_Select(self):
        while True:
            i = str(input("选择平台(1、手机，2、TV，3、断开无线ADB连接，4、重启ADB服务，5、结束CMD，e、退出）："))
            if i == '1':
                i = str(input("选择操作(1、卸载，2、安装，3、运行，4、结束进程，5、Top，6、Logcat）："))
                while True:
                    if i == '1':
                        MobileCase().MobileUninstall()
                        time.sleep(3)
                        break
                    elif i == '2':
                        MobileCase().MobileInstall(apk_path)
                        time.sleep(10)
                        break
                    elif i == '3':
                        MobileCase().MobileAppRun()
                        time.sleep(3)
                        break
                    elif i == '4':
                        MobileCase().mobileAppQuite()
                        time.sleep(3)
                        break
                    elif i == '5':
                        MobileCase().mobileAppTop()
                        break
                    elif i == '6':
                        MobileCase().mobileAppLogcat()
                        break
                    elif i == '7':
                        MobileCase().MobileAppClear()
                        break
                    elif i == '8':
                        MobileCase().mobileHome()
                        break
                    elif i == '9':
                        MobileCase().mobileBack()
                        break
                    else:
                        startInit().Case_Select()
            elif i == '2':
                TvCase().tvConnect()
                i = str(input("选择操作(1、卸载，2、安装，3、运行，4、结束进程，5、Top，6、Logcat）："))
                while True:
                    if i == '1':
                        TvCase().tvUninstall()
                        break
                    elif i == '2':
                        TvCase().tvInstall(apk_path)
                        break
                    elif i == '3':
                        TvCase().tvAppRun()
                        break
                    elif i == '4':
                        TvCase().tvAppQuit()
                        break
                    elif i == '5':
                        TvCase().tvAppTop()
                        break
                    elif i == '6':
                        TvCase().tvAppLogcat()
                        break
                    elif i == '7':
                        TvCase().tvAppClear()
                        break
                    elif i == '8':
                        TvCase().tvHome()
                        break
                    elif i == '9':
                        TvCase().tvBack()
                        break
                    else:
                        startInit().Case_Select()
            elif i == '3':
                Adb().adbDisconnect()
                break
            elif i == '4':
                Adb().adbRestart()
                break
            elif i == '5':
                Adb().cmdKill()
                break
            elif i == 'e':
                exit(0)
            else:
                print("try")
                continue


if __name__ == '__main__':
    apk_path = Common().apkPath()
    apk_name = APP().get_apk_package()
    startInit().Case_Select()