# Adam Clemons -  proof of concept
from fabric.api import hide, run, env, put
from fabric.tasks import execute
from fabric import state

import os, time, datetime
from getpass import getpass


def getInstanceString():
    string = "##-- shRemote.py by Adam Clemons --"
    string+= env.host_string
    string += '-'
    string += unicode(datetime.datetime.now())
    string += '-'
    return string


def writeFile(filename, content):
    # wb - write binary, truncates file before writing
    # ab - append binary
    # binary will keep original line endings, and not make the file look ugly in notepad++
    outFile = open(filename, 'ab')
    # TODO: Handle Exceptions
    outFile.write(getInstanceString() + '\n')
    outFile.write(content + '\n')

    outFile.close()

def authorize():
    # env.password = getpass("Enter your password for %s" % env.host_string)
    pass

def deploySh(scriptFile='testScript.sh', filename='testScript.sh'):
    # TODO: use Tkinter to browse for the file and get filename from path
    authorize()
    put(scriptFile, '~/'+filename, mode=0775)
    out = run('~/'+filename)
    writeFile('output', out)

if __name__=='__main__':
    # TODO: Document this, don't make the user retype their password everytime.
    #env.user=os.getenv('username')
    env.user='pi'
    env.password = 'raspberry'
    env.hosts = ['raspberrypi', '192.168.1.85']
    with hide('output'):
        execute(deploySh)
