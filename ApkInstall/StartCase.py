# coding=utf-8
from Case.MobileCase import MobileCase
from Case.TvCase import TvCase
from Base.Common import Common



class startInit:

    def Case_Select(self):
        while True:
            i = str(input("选择平台(1、手机，2、TV，3、断开无线ADB连接，4、重启ADB服务）："))
            if i == '1':
                startInit().mobileCase()
                break
            elif i == '2':
                startInit().tvCase()
                break
            elif i == '3':
                Common().adbDisconnect()
                break
            elif i == '4':
                Common().adbRestart()
                break
            else:
                print("try")
                continue

    def mobileCase(self):
        MobileCase().MobileUninstall()
        MobileCase().MobileInstall(apk_path)

    def tvCase(self):
        TvCase().tvConnect()
        TvCase().tvUninstall()
        TvCase().tvInstall(apk_path)
        TvCase().tvAppRun()

if __name__ == '__main__':
    apk_path = "C:\\Users\\YongYI\\Downloads\\com.estrongs.android.pop_10067.apk"
    startInit().Case_Select()