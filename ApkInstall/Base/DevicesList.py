import yaml
import re

class devicesList:


    def openConfigFile(self):
        file = open('Data/DeviceIP.yaml', 'r', encoding="utf-8")
        file_data = file.read()
        file.close()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        return data

    def get_DevicesIP(self):
        data = str(self.openConfigFile())
        IP = re.findall("'IP': '(.*?)'", data ,re.S)
        return IP

if __name__ == '__main__':
    # print(devicesList().get_DevicesIP())
    devicesList().get_DevicesIP()
