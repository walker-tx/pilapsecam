import json

class timelapse:
            
    def getConfig(self, setting=None):
        
        try:
            config_file = open('PLC_config', 'r')
            self.config_dict = json.load(config_file)
            
            if setting is None:
                return self.config_dict
            else:
                try:
                    x = self.config_dict[setting]
                    return x
                except KeyError as error:
                    print("ERROR: ", error, "is not an acceptable setting.")
                    
        except OSError as error:
            print("ERROR OPENING PLC_config\n", error, "\nConsider running setDefaultConfig()")
        
        
        
        
    def setDefaultConfig(self):
        config_file = open('PLC_config', 'w+')
        default_config_dict = {'photo_local_root': '/home/pi/Desktop/images', 
                                'FILE_TYPE': 'RAW', 'INTERVAL': 15, 
                                'FINISH_HOUR': '17', 'START_HOUR': '7'}
        
        json.dump(default_config_dict, config_file, indent=4, sort_keys=True, separators=(',', ':'))
        config_file.close()
        
        
    def printConfig(self):
        print('Config : ')
        print(self.config_dict)
        
        
    def __init__(self):
        config_file = open('PLC_config', 'w+')
    
        try:
            self.config_dict = json.load(config_file)
            config_file.close()
        except:
            config_file.close()
            self.setDefaultConfig()