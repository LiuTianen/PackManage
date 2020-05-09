# coding=utf-8

"""
使用Python获取待测APP的相关参数信息
"""

import os
import subprocess


class APP:
    # 待测试应用路径
    apkPath = "C:\\Users\\YongYI\\Downloads\\com.estrongs.android.pop_10067.apk"

    def __init__(self):
        self.aapt = "D:\\SDK\\build-tools\\28.0.3\\aapt dump badging "


    # 获取APP的文件大小
    def get_apk_size(self):
        size = os.path.getsize(self.apkPath) / (1024 * 1000)
        return('%.2f' % size)+ "M"  #保留小数点后两位

    # 获取APP的版本信息
    def get_apk_version(self):
        cmd = self.aapt + self.apkPath
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[3].decode()[12:]
            result = result.split("'")[1]
        return result

    # 获取APP的名字
    def get_apk_name(self):
        cmd = self.aapt + self.apkPath + " | findstr application-label-zu: "
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = str(output, encoding='utf8')
        if output != "":
            result = output.split("'")[1]
        return result

    # 获取APP的包名
    def get_apk_package(self):
        cmd = self.aapt + self.apkPath + " | findstr package:"
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = str(output, encoding='utf8')
        if output != "":
            result = output.split()[1][6:-1]
        return result

    # 得到启动类
    def get_apk_activity(self):
        cmd = self.aapt + self.apkPath + " | findstr launchable-activity:"
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output != "":
            result = output.split()[1].decode()[6:-1]
        return result


if __name__ == '__main__':
    APPInfo = APP()
    # print("应用名称:", APPInfo.get_apk_name())
    # print("app文件大小:", APPInfo.get_apk_size())
    # print("app版本信息:", APPInfo.get_apk_version())
    # print("app包名:", APPInfo.get_apk_package())
    # print("app的启动类:", APPInfo.get_apk_activity())
