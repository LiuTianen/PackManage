import threading
import time
from OnlineDevices import OnelineDevices as od


class PackInstall:

    # 推送APK，并安装
    def installApk(self, apk_path):
        connectDevices = od().get_conn_dev()
        commands =[]

        for device in connectDevices:
            cmd = "adb -s %s install -r %s" % (device,apk_path)
            commands.append(cmd)

        threads = []
        threads_count = len(commands)

        for i in range(threads_count):
            t = threading.Thread(target=od().excute, args=(commands[i],))
            threads.append(t)

        for i in range(threads_count):
            time.sleep(1)
            threads[i].start()

        for i in range(threads_count):
            threads[i].join()


if __name__ == '__main__':
    apk_path = "C:\\Users\\YongYI\\Downloads\\com.estrongs.android.pop_10067.apk"
    PackInstall().installApk(apk_path)

