import os
import subprocess
import re



class OnelineDevices:

    def excute(self, cmd):
        subprocess.Popen(cmd, shell=True)


    # 获取在线的设备
    def get_conn_dev(self):
        connectDeviceid = []
        p =os.popen('adb devices')
        outstr = p.read()
        print(outstr)
        connectDeviceid = re.findall(r'(\w+)\s+device\s', outstr)
        return connectDeviceid

if __name__ == '__main__':
    OnelineDevices().get_conn_dev()