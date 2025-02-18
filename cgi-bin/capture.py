#!C:/Python311/python.exe
import os
import face_recognition
from io import BytesIO
import cgi
from PIL import Image
import base64

print("Content-Type: text/html\n")
print("""
<html>
<head>
    <title>Capture Photo</title>
    <script>
        function capturePhoto() {
            navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                document.getElementById('video').srcObject = stream;
            });
        }

        function sendPhoto() {
            var canvas = document.createElement('canvas');
            var video = document.getElementById('video');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            var ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            
            var dataURL = canvas.toDataURL('image/png');
            document.getElementById('photoData').value = dataURL;
            document.getElementById('photoForm').submit();
        }
    </script>
</head>
<body onload="capturePhoto()">
    <h1>Capture Your Photo</h1>
    <video id="video" autoplay></video>
    <br>
    <form id="photoForm" action="exam.py" method="post">
        <input type="hidden" id="photoData" name="photo">
        <button type="button" onclick="sendPhoto()">Submit Photo</button>
    </form>
</body>
</html>
""")
