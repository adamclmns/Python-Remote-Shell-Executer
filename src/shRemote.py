# Adam Clemons -  slightly-refined, but still rough, proof of concept
#
from fabric.api import hide, run, env, put
from fabric.tasks import execute
from fabric import state

import os, time, datetime, tkinter as tk, tkinter.filedialog, argparse, configparser
from getpass import getpass

config=configparser.ConfigParser()
config.read('shRemote.cfg')

DEFAULT_SCRIPT = config.get('DEFAULT','DEFAULT_SCRIPT')
DEFAULT_PASSWORD = config.get('DEFAULT','DEFAULT_PASSWORD')
DEFAULT_HOSTS = config.get('DEFAULT','DEFAULT_HOSTS')
DEFAULT_USER = config.get('DEFAULT','DEFAULT_USER')
DEFAULT_AUTHORIZE = config.get('DEFAULT','DEFAULT_AUTHORIZE')
ScriptPath = DEFAULT_SCRIPT # so this is never null or empty, and initialized with a good value out-of-the-box

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
        this will get a filename using Tkinter browse dialoge
    '''
    file_opt = options = {}
    options['filetypes'] = [ ('shell script', '.sh'), ('all files', '.*')]
    options['initialdir'] = os.getcwd()
    frame =  tk.Frame()
    options['parent'] = frame
    options['title'] = 'select a shell script source file: '
    filepath=tkinter.filedialog.askopenfilename(**file_opt)
    frame.destroy()
    return filepath

def writeFile(filename, content):
    '''
        this writes some given content to a given filename in binary append mode
    '''
    # wb - write binary, truncates file before writing
    # ab - append binary
    # binary will keep original line endings, and not make the file look ugly in notepad++
    outFile = open(filename, 'ab')
    # TODO: Handle Exceptions
    outFile.write(getInstanceString() + '\n')
    outFile.write(content + '\n')
    outFile.close()

def authorize():
    '''
        gets a pasword, from default Config if DEFAULT_AUTHORIZE=TRUE, or from the terminal DEFAULT_AUTHORIZE=FALSE
    '''
    if DEFAULT_AUTHORIZE:
        env.password = DEFAULT_PASSWORD
    else:
        env.password = getpass("Enter your password for %s" % env.host_string)

def deploySh(filepath=ScriptPath):
    # split file name seperately
    path, filename=os.path.split(filepath)
    authorize()
    put(filepath, '~/'+filename, mode=775)
    out = run('~/'+filename)
    writeFile('output', out)

if __name__=='__main__':

    #Command line params, because the UI isn't designed yet
    parser = argparse.ArgumentParser(description="executes shell scripts remotely over ssh")
    parser.add_argument('--hosts', dest='hosts', required=False)
    parser.add_argument('--username',dest='user',required=False)
    parser.add_argument('--script',dest='script',required=False)
    parser.add_argument('--pass',dest='password',required=False)
    # adding short-hand arguments for convinence.
    # BUG With this line
    # parser.add_argument('-s', dest='server', required=False)
    parser.add_argument('-u',dest='user',required=False)
    parser.add_argument('-s',dest='script',required=False)
    parser.add_argument('-p',dest='password',required=False)
    # TODO: add a -? --help command switch to print the help documentation (maybe a new module/resource in the package?)

    # Parse args
    args = parser.parse_args()

    # Check if Arguments provided, if so, Apply the argument, else apply default or ask
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
        # env.user=os.getenv('username')
        env.user=DEFAULT_USER
        print("Using default username pi")

    if args.password != None:
        env.password = args.password

    if args.script != None:
        ScriptPath = args.script
    else:
        ScriptPath = DEFAULT_SCRIPT

    # Make the Magic Happen
    with hide('output'):
        execute(deploySh)
