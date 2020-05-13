"""
运行逻辑（暂定）
版本控制功能，区分TV和手机设备
1为手机
2为TV
整体逻辑是：选择版本后，先进行卸载操作，然后安装
等待2分钟，或者隐式等待（APP列表出现指定包名）
启动APP，启动top，启动logcat
然后等待一段时间后，重启APP
然后卸载，重装，再运行
"""
from Case.MobileCase import MobileCase
from Case.TvCase import TvCase
from Base.Common import Common



class startInit:

    def Case_Select(self):
        while True:
            i = str(input("选择平台(1、手机，2、TV，3、断开无线ADB连接，4、重启ADB服务）："))
            if i == '1':
                startInit().mobileCase()
                # print("1")
                break
            elif i == '2':
                startInit().tvCase()
                # print("2")
                break
            elif i == '3':
                Common().adbDisconnect()
                # print("3")
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