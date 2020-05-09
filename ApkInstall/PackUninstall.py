import os
import subprocess
import threading
import re
import time
from PackName import APP

class UnInstall:

    def excute(self,cmd):
        subprocess.Popen(cmd, shell=True)

    # 获取在线的设备
    def get_conn_dev(self):
        connectDeviceid = []
        p = os.popen('adb devices')
        outstr = p.read()
        print(outstr)
        connectDeviceid = re.findall(r'(\w+)\s+device\s', outstr)
        return connectDeviceid


    def Uninstall(self):
        packName = APP().get_apk_package()

        connectDevices = self.get_conn_dev()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s uninstall %s" % (device,packName)
            commands.append(cmd)
        threads = []
        threads_count = len(commands)

        for i in range(threads_count):
            t = threading.Thread(target=self.excute, args=(commands[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)  # 防止adb连接出错
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()

if __name__ == '__main__':
    UnInstall().Uninstall()
