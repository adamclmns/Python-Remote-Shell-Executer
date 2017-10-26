"""
Create "Sessions" to be saved for multiple hosts. 
Sessions can be combined into SessionSets which will allow execution across many hosts. 
"""
# TODO: Sessions will be stored in .cfg file managed with ConfigManager
# TODO: Sessions will only be used for holding and passing Session information, not for logic
import configparser


config = configparser.RawConfigParser()


config.add_section('shRemote-Configuration')
config.set('shRemoteConfiguration', 'DEFAULT_USER', 'pi')
config.set('shRemoteConfiguration', 'DEFAULT_HOSTS', "['raspberrypi','192.168.1.85']")
config.set('shRemoteConfiguration', 'DEFAULT_PASSWORD', 'raspberry')
config.set('shRemoteConfiguration', 'DEFAULT_SCRIPT', 'testScript.sh')
config.set('shRemoteConfiguration', 'DEFAULT_AUTHORIZE', 'True')

# Writing our configuration file to 'example.cfg'
with open('shRemote.cfg', 'w') as configfile:
    config.write(configfile)

class Session():
    def __init__(self, *args, **kwargs):
        self._host
        self._user
        self._passwd
        self.friendlyName
    
    
class SessionSet():
    def __init__(self, *args, **kwargs):
        self.set = []
        self.friendlyName = None

    