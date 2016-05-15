# Adam Clemons -  proof of concept
from fabric.api import hide, run, env, put
from fabric.tasks import execute
from fabric import state

import os, time, datetime, Tkinter as tk,tkFileDialog, argparse, ConfigParser
from getpass import getpass

config=ConfigParser.ConfigParser()
config.read('shRemote.cfg')

DEFAULT_SCRIPT = config.get('shRemote-Configuration','DEFAULT_SCRIPT')
DEFAULT_PASSWORD = config.get('shRemote-Configuration','DEFAULT_PASSWORD')
DEFAULT_HOSTS = config.get('shRemote-Configuration','DEFAULT_HOSTS')
DEFAULT_USER = config.get('shRemote-Configuration','DEFAULT_USER')
DEFAULT_AUTHORIZE = config.get('shRemote-Configuration','DEFAULT_AUTHORIZE')

def getInstanceString():
    string = "##-- shRemote.py by Adam Clemons --"
    string += env.host_string
    string += '-'
    string += unicode(datetime.datetime.now())
    string += '-'
    return string

def getFilename():
    file_opt = options = {}
    options['filetypes'] = [ ('shell script', '.sh'), ('all files', '.*')]
    options['initialdir'] = os.getcwd()
    options['parent'] = tk.Frame()
    options['title'] = 'select a shell script source file: '
    filepath=tkFileDialog.askopenfilename(**file_opt)
    
    return filepath

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
    if DEFAULT_AUTHORIZE:
        env.password = DEFAULT_PASSWORD
    else:
        env.password = getpass("Enter your password for %s" % env.host_string)
    
def deploySh(filepath=DEFAULT_SCRIPT):
    # split file name seperately
    path, filename=os.path.split(filepath)
    authorize()
    put(filepath, '~/'+filename, mode=0775)
    out = run('~/'+filename)
    writeFile('output', out)

if __name__=='__main__':
    
    #Command line params for fun
    parser = argparse.ArgumentParser(description="executes shell scripts remotely over ssh")
    parser.add_argument('--hosts', dest='hosts', required=False)
    parser.add_argument('--username',dest='user',required=False)
    parser.add_argument('--script',dest='script',required=False)
    parser.add_argument('--pass',dest='password',required=False)
    # Parse args
    args=parser.parse_args()
    
    # Check if Arguments provided, if so, Apply the argument, else apply default or ask
    if args.hosts != None:
        # TODO: make this parse correctly into an array
        env.hosts = args.hosts
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
        ScriptPath = getFilename()
    
    # Make the Magic Happen
    with hide('output'):
        execute(deploySh)
