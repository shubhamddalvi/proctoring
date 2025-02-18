#!C:/Python311/python.exe

import cgi

print("Content-Type: text/html\n")

# Get form data
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

# Hardcoded credentials
if username == "admin" and password == "password":
    print('<meta http-equiv="refresh" content="0;url=/proctoring_tool/cgi-bin/capture.py">')
else:
    print("<h1>Login Failed</h1><a href='/proctoring_tool/login.html'>Try Again</a>")
