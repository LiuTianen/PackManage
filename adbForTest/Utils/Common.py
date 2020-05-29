#!/usr/bin/env python
#coding=utf-8

import subprocess
import time
import threading
import configparser

class Common:
    # 配置文件读取的方法
    cf = configparser.ConfigParser()
    cf.read('../Data/Config.ini', encoding="utf-8")

    # apk路径读取的方法
    def apkPath(self):
        apkPath = self.cf.get("Common", "apkPath")
        return apkPath

    # aapt路径的读取方法
    def aapt(self):
        appt = self.cf.get("Common", "aapt")
        return appt

    def aaPath(self):
        aaPath = Common().aapt() + ' ' + Common().apkPath()
        return aaPath

    def excute(self, cmd):
        subprocess.Popen(cmd, shell=True)

    def loop_threads(self,commands):
        threads = []
        threads_count = len(commands)

        for i in range(threads_count):
            t = threading.Thread(target=self.excute, args=(commands[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()


if __name__ == '__main__':
    adbDevices = []

