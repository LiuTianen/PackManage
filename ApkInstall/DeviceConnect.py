from Base.DevicesList import devicesList as dl
import time
import threading
from Base.OnlineDevices import OnelineDevices as od
class DevicesConnect:

    def deviceConnect(self):
        commands = []
        data = dl().get_DevicesIP()
        for IP in data:
            cmd = "adb connect %s" %(IP)
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
    DevicesConnect().deviceConnect()
