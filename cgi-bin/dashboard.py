#!C:/Python311/python.exe

import cgi

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
photo = form.getvalue("photo")

if photo:
    print("<h1>Photo Received. Exam Starting...</h1>")
else:
    print("<h1>Photo Verification Failed</h1>")

print("""
<html>
<head>
    <title>Exam Dashboard</title>
    <script>
        function trackUser() {
            setInterval(() => {
                console.log("Tracking user activity...");
            }, 5000);
        }
    </script>
</head>
<body onload="trackUser()">
    <h1>Welcome to the Exam</h1>
    <p>Tracking user activity...</p>
    <form action="submit.py" method="post">
        <button type="submit">Submit Exam</button>
    </form>
</body>
</html>
""")
