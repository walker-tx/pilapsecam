import json

class timelapse:
    
    def __init__(self):
        config_file = open('PLC_config', 'r')
        self.config_dict = json.load(open('PLC_config', 'r'))
        config_file.close()  
        
    def printConfig(self):
        print('Config : ')
        print(self.config_dict)