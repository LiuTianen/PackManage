from Base.DevicesList import devicesList as dl
import time
import threading
from Base.OnlineDevices import OnelineDevices as od

class WifiInstall:

    def wifiInstall(self, apk_path):
        connecetDevices = dl().get_DevicesIP()
        commands = []

        for device in connecetDevices:
            cmd = "adb -s %s install -r %s" %(device, apk_path)
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
    WifiInstall().wifiInstall(apk_path)