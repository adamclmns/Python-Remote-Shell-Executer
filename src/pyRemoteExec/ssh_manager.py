"""
Manages connections to hosts via ssh
"""

from fabric.api import hide, run, env, put
from fabric.tasks import execute
from fabric import state

import os
import time
import datetime
from getpass import getpass

# TIP: with hide('output'): will hide console output from console
class SSHManager():
    def __init__(self, host, user, pass):
        env.hosts = [host]
        env.user = user
        env.password = getpass()

    def deploy(self, path_to_deploy):
        isFile = True
        if (isFile):
            execute(self._deployFile(path_to_deploy))
        else:
            execute(self._deployDirectory())

    def runCommand(self, command):
        execute(self._runCommand(command))

    def _deployFile(self, filepath):
        path, filename = os.path.split(filepath)
        put(filepath, '~/' + filename, mode=775)

    def _deployDirectory():
        pass

    def _runCommand(self, commandString):
        out = run(commandString)
        return out

    @staticmethod
    def writeFile(filename, content):
    '''
        TODO: Optionally pipe output to the terminal
        this writes some given content to a given filename in binary append mode
    '''
    # wb - write binary, truncates file before writing
    # ab - append binary
    # binary will keep original line endings, and not make the file look ugly
    # in notepad++
    outFile = open(filename, 'ab')
    # TODO: Handle Exceptions
    outFile.write(getInstanceString() + '\n')
    outFile.write(content + '\n')
    outFile.close()
