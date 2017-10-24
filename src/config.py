# This file will be kept seperate from compiled sources for easy configuration

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