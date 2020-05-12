import yaml
import re

class devicesList:


    def openTvConfigFile(self):
        file = open('..\\..\\Data\\TvDevices.yaml', 'r', encoding="utf-8")
        file_data = file.read()
        file.close()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        return data

    def openMobileConfigFile(self):
        file = open('..\\..\\Data\\MobileDevices.yaml', 'r', encoding="utf-8")
        file_data = file.read()
        file.close()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        return data

    def get_Tv_IP(self):
        data = str(self.openTvConfigFile())
        IP = re.findall("'IP': '(.*?)'", data ,re.S)
        return IP

    def get_MobileName(self):
        data = str(self.openMobileConfigFile())
        # Devices_name = re.findall("'name': '(.*?)'", data, re.S)
        Devices = re.findall("'DeviceID': '(.*?)'", data, re.S)

        return Devices



if __name__ == '__main__':
    # print(devicesList().get_DevicesIP())
    devicesList().get_Tv_IP()
    devicesList().get_MobileName()

