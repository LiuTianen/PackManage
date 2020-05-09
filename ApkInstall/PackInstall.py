import os
import subprocess
import threading
import re
import time


class PackInstall:

    def excute(self, cmd):
        subprocess.Popen(cmd, shell=True)


    # 获取在线的设备
    def get_conn_dev(self):
        connectDeviceid = []
        p =os.popen('adb devices')
        outstr = p.read()
        print(outstr)
        connectDeviceid = re.findall(r'(\w+)\s+devices\s', outstr)
        return connectDeviceid

    # 推送APK，并安装
    def installApk(self, apk_path):
        connectDevices = self.get_conn_dev()
        commands =[]

        for device in connectDevices:
            cmd = "adb -s %s install -r %s" % (device,apk_path)
            commands.append(cmd)

        threads = []
        threads_count = len(commands)

        for i in range(threads_count):
            t = threading.Thread(target= self.excute, args=(commands[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()


if __name__ == '__main__':
    apk_path = "null"

