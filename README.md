# proctoring_tool

Make sure to install venv inside of folder

1. Ensure the project is placed inside the htdocs folder of your XAMPP installation at:
C:\xampp\htdocs\proctoring_tool

2. Configuring Apache for Python
To enable Python CGI execution, modify the Apache configuration file (httpd.conf).
Navigate to:
C:\xampp\apache\conf\httpd.conf

3. Make the Following Changes
# Enable CGI execution
LoadModule cgi_module modules/mod_cgi.so

# Allow execution of Python scripts in the cgi-bin directory
<Directory "C:/xampp/htdocs/proctoring_tool/cgi-bin">
    Options +ExecCGI
    AddHandler cgi-script .py
    Require all granted
</Directory>

# Ensure .py files are recognized as CGI scripts
AddHandler cgi-script .py
ScriptInterpreterSource Registry

Step 3: Save and Restart Apache
Save httpd.conf.
Open XAMPP Control Panel → Click Stop on Apache → Click Start again.

4. Configuring Python in Scripts
Every Python script should start with the correct shebang line to specify the Python interpreter.
Step 1: Find Your Python Path
Open Command Prompt (CMD).
command to run in terminal => where python
Copy the first path displayed. Example: C:\Python311\python.exe
paste this path at the top of each python file
ex : #!C:/Python311/python.exe