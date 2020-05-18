import subprocess
import time
import threading
import os
import configparser

class Common:
    # 配置文件读取的方法
    cf = configparser.ConfigParser()
    cf.read('Config.ini', encoding="utf-8")

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

    # def apkPath(self):
    #     # 调试路径
    #     # apkPath = "..\\Apk\\com.estrongs.android.pop_10067.apk"
    #
    #     # 运行路径
    #     apkPath = "Apk\\com.estrongs.android.pop_10067.apk"
    #     return apkPath

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

    def adbDisconnect(self):
        Disc = os.popen('adb disconnect')
        return Disc

    def adbRestart(self):
        restart = os.popen('adb kill-server &&adb devices')
        return restart

    def adbTop(self,adbDevices):
        adbs = 'start cmd /k "adb -s %s shell top -m 10"' %(adbDevices)
        Top = os.system(adbs)
        return  Top


    def adbClear(self, adbDevices, packageName):
        adbClear = 'adb -s %s shell pm clear %s' %(adbDevices, packageName)
        return adbClear

    def adbLogcat(self,adbDevices):
        logTag = 'vc:V vs:V Vm:V ReportWeb:V vac:V reqm:V Em:V VPReportManager:V VpAdControl:V *:S'
        adbs = 'start cmd /k "adb -s %s logcat %s"' % (adbDevices, logTag)
        Top = os.system(adbs)
        return Top

    def cmdKill(self):
        adbs = 'start cmd /k "tskill adb && tskill cmd"'
        kill = os.system(adbs)
        return kill

if __name__ == '__main__':
    adbDevices = []
    # print(Common().apkPath())
    # Common().excute()
    # Common().loop_threads()
    # Common().apkPath()
    # Common().adbDisconnect()
    # Common().adbRestart()
    # Common().adbTop(adbDevices)
    # Common().adbLogcat(adbDevices)
    # Common().cmdKill()
