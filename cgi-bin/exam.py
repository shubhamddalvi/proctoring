#!C:/Python311/python.exe
import cgi
import face_recognition
from io import BytesIO
from PIL import Image
import base64

# Function to load and encode the captured photo from base64
def decode_image(image_data):
    image_data = image_data.split(",")[1]
    image_data = base64.b64decode(image_data)
    return Image.open(BytesIO(image_data))

print("Content-Type: text/html\n")

# Load the uploaded photo from the form
form = cgi.FieldStorage()
user_photo = form.getvalue("photo")

# Decode the uploaded photo
user_image = decode_image(user_photo)

# Load the saved reference photo (captured at login)
reference_photo_path = "captured_face.png"
reference_image = face_recognition.load_image_file(reference_photo_path)
reference_face_encoding = face_recognition.face_encodings(reference_image)[0]

# Encode the captured photo and compare faces
user_image_pil = user_image.convert("RGB")
user_image_pil.save("current_face.png")
user_image = face_recognition.load_image_file("current_face.png")
user_face_encodings = face_recognition.face_encodings(user_image)

# Compare the faces
match = False
if len(user_face_encodings) > 0:
    user_face_encoding = user_face_encodings[0]
    matches = face_recognition.compare_faces([reference_face_encoding], user_face_encoding)
    if matches[0]:
        match = True

# If the faces match, allow the exam; otherwise, disqualify
if match:
    print("""
    <html>
    <head>
        <title>Exam Panel</title>
        <script>
            let timer = 60;  // 1-minute timer

            function startTracking() {
                navigator.mediaDevices.getUserMedia({ video: true })
                .then(stream => {
                    document.getElementById('video').srcObject = stream;
                    setInterval(captureAndVerify, 5000); // Verify every 5 sec
                });
            }

            function captureAndVerify() {
                let canvas = document.createElement('canvas');
                let video = document.getElementById('video');
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                let ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
                let newPhoto = canvas.toDataURL('image/png');

                // Send new photo for comparison
                let xhr = new XMLHttpRequest();
                xhr.open("POST", "exam.py", true);
                xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
                xhr.send("photo=" + newPhoto);
            }

            function startTimer() {
                let timerInterval = setInterval(() => {
                    document.getElementById("timer").innerText = timer + " sec left";
                    timer--;
                    if (timer < 0) {
                        clearInterval(timerInterval);
                        document.getElementById("examForm").submit();  // Auto-submit
                    }
                }, 1000);
            }
        </script>
    </head>
    <body onload="startTracking(); startTimer();">
        <h1>Exam Panel</h1>
        <p id="timer">60 sec left</p>
        <video id="video" autoplay></video>
        <form id="examForm" action="submit.py" method="post">
            <button type="submit">Submit Exam</button>
        </form>
    </body>
    </html>
    """)
else:
    print("""
    <html>
    <head>
        <title>Disqualified</title>
    </head>
    <body>
        <h1>Face Mismatch! You are disqualified from the exam.</h1>
        <a href="/proctoring_tool/logout.py">Logout</a>
    </body>
    </html>
    """)
