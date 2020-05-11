import threading
import time
from PackName import APP
from Base.OnlineDevices import OnelineDevices as od

class UnInstall:


    def Uninstall(self):
        packName = APP().get_apk_package()

        connectDevices = od().get_conn_dev()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s uninstall %s" % (device,packName)
            commands.append(cmd)
        threads = []
        threads_count = len(commands)

        for i in range(threads_count):
            t = threading.Thread(target=od().excute, args=(commands[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)  # 防止adb连接出错
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()

if __name__ == '__main__':
    UnInstall().Uninstall()
