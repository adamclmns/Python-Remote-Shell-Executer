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
