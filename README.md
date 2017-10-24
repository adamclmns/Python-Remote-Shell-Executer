# Python-Remote-Shell-Executer
upload and execute bash scripts from a windows pc on many remote linux hosts


Description of files:
* src/condaEnv.bat - bat file to import and activate the conda environment file
* src/config.py - generates the config file shRemote.cfg
* src/makeExe.bat - uses pyinstaller to create a .exe in the dist/ directory
* src/shRemote.py - the Script that does all the work
* src/testScript.sh - test bash script - needs LF line endings to work
* src/shRemote.cfg - generated configuration file
* src/shRemote.yml - Exported conda environment file.

You can use Notepad++ or Atom to fix the line endings. See the respective documentation for details.

Requires Python 2.7 x86 and Fabric module. You can also just use the provided conda Env file with miniconda for windows (any version should work)

NOTE: this is an unfinished project. Features are incomplete.


Background:
  In a previous job, I would write bash scripts that would search logs for certain errors or messages for troubleshooting production environments. Some of these scripts would get way too long for a one-liner, and often they needed to be run against 8 or more servers. 
  
  To make running the script on a set of servers easier, I created this tool.
  Now, as I dive deeper into raspberry pi, I'm finding that I need to upload and run python code over ssh, and this tool will be extended to upload any file and execute any command, with a few specific short-cut commands for running python scripts on a remote host and pipe the output back to a terminal. 
  
