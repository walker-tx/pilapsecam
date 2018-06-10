import json
import logging

class Timelapse:
            
    def getConfig(self, setting=None): 
        
        if setting is None:
            return self.config_dict
        else:
            try:
                x = self.config_dict[setting]
                return x
            except:
                logging.getLogger().warning('Problem accessing setting \"' + setting + '\". Key likely does not exist.')

    
    def setDefaultConfig(self):
        config_file = open('PLC_config', 'w+')
        default_config_dict = {'photo_local_root': '/home/pi/Desktop/images', 
                                'FILE_TYPE': 'RAW', 'INTERVAL': 15, 
                                'FINISH_HOUR': '17', 'START_HOUR': '7'}
        
        json.dump(default_config_dict, config_file, indent=4, sort_keys=True, separators=(',', ':'))
        config_file.close()
        logging.getLogger().warning("PLC_config has been reset.")
        
        
    def loadConfig(self):
        try:
            config_file = open('PLC_config', 'r')
            self.config_dict = json.load(config_file)
            config_file.close()
        except:
            logging.getLogger().warning('Problem accessing the configuration data. Either PLC_config does not exist, or the file has no JSON data in it... Resetting PLC_config to default')
            config_file.close()
            self.setDefaultConfig()
        
        
    def __init__(self):
        self.loadConfig()