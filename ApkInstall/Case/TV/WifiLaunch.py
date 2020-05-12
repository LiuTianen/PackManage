import threading
import time
from Base.PackName import APP
from Base.OnlineDevices import OnelineDevices as od
from Base.DevicesList import devicesList as dl

class PackLaunch:

    def lauchApp(self):
        launchable_activity = APP().get_apk_activity()
        packName = APP().get_apk_package()
        pack_lauch = packName +"/"+ launchable_activity
        connectDevices = dl().get_DevicesIP()
        commands = []
        for device in connectDevices:
            cmd = "adb -s %s shell am start -n %s" % (device, pack_lauch)
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
    PackLaunch().lauchApp()