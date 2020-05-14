import yaml
import re
import os

class devicesList:


    def get_conn_dev(self):
        connectDeviceid = []
        p =os.popen('adb devices')
        outstr = p.read()
        connectDeviceid = re.findall(r'(.*?)\s+device\s', outstr)
        return connectDeviceid

    def openTvConfigFile(self):
        # file = open('..\\..\\Data\\TvDevices.yaml', 'r', encoding="utf-8")
        file = open('Data\\TvDevices.yaml', 'r', encoding="utf-8")
        file_data = file.read()
        file.close()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        return data

    def openMobileConfigFile(self):
        # file = open('..\\..\\Data\\MobileDevices.yaml', 'r', encoding="utf-8")
        file = open('Data\\MobileDevices.yaml', 'r', encoding="utf-8")
        file_data = file.read()
        file.close()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        return data

    def get_Tv_IP(self):
        data = str(self.openTvConfigFile())
        tvIP = re.findall("'IP': '(.*?)'", data ,re.S)
        return tvIP

    def get_MobileName(self):
        data = str(self.openMobileConfigFile())
        # Devices_name = re.findall("'name': '(.*?)'", data, re.S)
        Devices = re.findall("'DeviceID': '(.*?)'", data, re.S)
        return Devices


    def get_tvDevices(self):
        tvDevices = []
        for i in self.get_conn_dev():
            if i in self.get_Tv_IP():
                tvDevices.append(i)
        return tvDevices

    def get_mobileDevices(self):
        mobileDevices = []
        for i in self.get_conn_dev():
            if i in self.get_MobileName():
                mobileDevices.append(i)
        return mobileDevices



if __name__ == '__main__':
    # print(devicesList().get_DevicesIP())
    devicesList().get_tvDevices()
    devicesList().get_mobileDevices()

