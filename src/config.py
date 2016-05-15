# This file will be kept seperate from compiled sources for easy configuration

import ConfigParser


config = ConfigParser.RawConfigParser()


config.add_section('shRemote-Configuration')
config.set('shRemote-Configuration', 'DEFAULT_USER', 'pi')
config.set('shRemote-Configuration', 'DEFAULT_HOSTS', "['raspberrypi','192.168.1.85']")
config.set('shRemote-Configuration', 'DEFAULT_PASSWORD', 'raspberry')
config.set('shRemote-Configuration', 'DEFAULT_SCRIPT', 'testScript.sh')
config.set('shRemote-Configuration', 'DEFAULT_AUTHORIZE', 'True')

# Writing our configuration file to 'example.cfg'
with open('shRemote.cfg', 'wb') as configfile:
    config.write(configfile)