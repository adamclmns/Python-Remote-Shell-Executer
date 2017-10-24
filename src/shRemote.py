# Adam Clemons - Code that needs a good refactoring and re-design.
# TODO: Add DocStrings
# TODO: Add Generic functionality for upload and run command
# TODO: Remove UI components
# TODO: Use Constants for Config names/sections
# TODO: Look at alternative to ConfigParser.
# TODO: First Setup Wizard (Conditionally imported for performance)
# TODO: Add quick-commands to Python_HOME/Scripts/ directory for easy access
# BUG: Doesn't run in Python3 properly.
# BUG: Dependencies are incomplete/wrong for python3
# BUG: Need python2/Python3 Requirements.txt and PyInstaller script for each
# TODO: Unit Tests for various functions. Will use Raspberry Pi via OTG for testing
# TODO: Test on something other than Windows.
# TODO: Add Git Support (for deploying code from git to ssh host and run
# post-clone commands)

from fabric.api import hide, run, env, put
from fabric.tasks import execute
from fabric import state

import os
import time
import datetime
import tkinter as tk
import tkinter.filedialog
import argparse
import configparser
from getpass import getpass

config = configparser.ConfigParser()
config.read('shRemote.cfg')
# TODO: Fix this, the API has changed
DEFAULT_SCRIPT = config.get('shRemoteConfiguration', 'DEFAULT_SCRIPT')
DEFAULT_PASSWORD = config.get('shRemoteConfiguration', 'DEFAULT_PASSWORD')
DEFAULT_HOSTS = config.get('shRemoteConfiguration', 'DEFAULT_HOSTS')
DEFAULT_USER = config.get('shRemoteConfiguration', 'DEFAULT_USER')
DEFAULT_AUTHORIZE = config.get('shRemoteConfiguration', 'DEFAULT_AUTHORIZE')
# so this is never null or empty, and initialized with a good value
# out-of-the-box
ScriptPath = DEFAULT_SCRIPT


def getInstanceString():
    '''
        This just creates a string that can be inserted into the output file so
        you can easily tell where each result set is coming from
    '''
    string = "##-- shRemote.py by Adam Clemons --"
    string += env.host_string
    string += '-'
    string += unicode(datetime.datetime.now())
    string += '-'
    return string


def getFilename():
    '''
        TODO: Remove this in favor of CLI interface. 
        this will get a filename using Tkinter browse dialoge
    '''
    file_opt = options = {}
    options['filetypes'] = [('shell script', '.sh'), ('all files', '.*')]
    options['initialdir'] = os.getcwd()
    frame = tk.Frame()
    options['parent'] = frame
    options['title'] = 'select a shell script source file: '
    filepath = tkinter.filedialog.askopenfilename(**file_opt)
    frame.destroy()
    return filepath


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


def authorize():
    '''
        gets a pasword, from default Config if DEFAULT_AUTHORIZE=TRUE, 
        or from the terminal DEFAULT_AUTHORIZE=FALSE
    '''
    if DEFAULT_AUTHORIZE:
        env.password = DEFAULT_PASSWORD
    else:
        env.password = getpass("Enter your password for %s" % env.host_string)


def deploySh(filepath=ScriptPath):
    # TODO: Genericise this to any code file.
    # split file name seperately
    path, filename = os.path.split(filepath)
    authorize()
    put(filepath, '~/' + filename, mode=775)
    out = run('~/' + filename)
    writeFile('output', out)


if __name__ == '__main__':

    # Command line params, because the UI isn't designed yet
    parser = argparse.ArgumentParser(
        description="executes shell scripts remotely over ssh")
    parser.add_argument('--hosts', dest='hosts', required=False)
    parser.add_argument('--username', dest='user', required=False)
    parser.add_argument('--script', dest='script', required=False)
    parser.add_argument('--pass', dest='password', required=False)
    # adding short-hand arguments for convinence.
    # BUG With this line
    # parser.add_argument('-s', dest='server', required=False)
    parser.add_argument('-u', dest='user', required=False)
    parser.add_argument('-s', dest='script', required=False)
    parser.add_argument('-p', dest='password', required=False)
    # TODO: add a -? --help command switch to print the help documentation
    # (maybe a new module/resource in the package?)

    # Parse args
    args = parser.parse_args()

    # Check if Arguments provided, if so, Apply the argument, else apply
    # default or ask
    if args.hosts != None:
        hostList = args.hosts.split(',')
        env.hosts = hostList
        print(env.hosts)
    else:
        env.hosts = DEFAULT_HOSTS
        print("Using Default Hosts:")
        print(env.hosts)
        print("use --hosts hostname1,hostname2 to specify")

    if args.user != None:
        env.user = args.user
    else:
        # TODO: Give user the option to use their System Username
        # env.user=os.getenv('username')
        env.user = DEFAULT_USER
        print("Using default username pi")

    if args.password != None:
        env.password = args.password

    if args.script != None:
        ScriptPath = args.script
    else:
        # TODO: BUG: There's a gitHub issue related to this line.
        ScriptPath = DEFAULT_SCRIPT

    # Make the Magic Happen
    with hide('output'):
        execute(deploySh)
