pyinstaller --exclude-module config --clean --onefile  src/shRemote.py
copy src\shRemote.cfg dist\shRemote.cfg
copy src\testScript.sh dist\testScript.sh
xcopy /v /i dist shRemote
jar -cMf shRemote.zip shRemote
echo "Compilation complete"
rmdir /Q /S shRemote
start explorer.exe shRemote.zip
echo "Packaging complete."
