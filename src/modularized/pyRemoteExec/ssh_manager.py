"""
Manages connections to hosts via ssh
"""

from fabric.api import hide, run, env, put
from fabric.tasks import execute
from fabric import state

import os, time, datetime
from getpass import getpass

class SSHManager():
    def __init__(host, user, pass):
        env.hosts = [host]
        env.user = user
        env.password = getpass()
        

    def _authorize():
        pass

    def _deployFile(filepath):
        path, filename = os.path.split(filepath)
        put(filepath, '~/' + filename, mode=775)


    def _deployDirectory():
        pass

    