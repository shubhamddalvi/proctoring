#!/usr/bin/python3

import cgi

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
answer = form.getvalue("q1")

# Simple answer validation (hardcoded check)
if answer == "4":
    print("<html><body>")
    print("<h3>Correct answer! You have completed the exam.</h3>")
    print('<a href="/proctoring_tool/templates/login.html">Logout</a>')
    print("</body></html>")
else:
    print("<html><body>")
    print("<h3>Incorrect answer. Please try again.</h3>")
    print('<a href="/proctoring_tool/templates/exam_dashboard.html">Back to Exam</a>')
    print("</body></html>")
