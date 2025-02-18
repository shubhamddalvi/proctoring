#!/usr/bin/python3

import cgi
import json
import cv2
import base64
import numpy as np

# Dummy verification - in real application, you should use a face recognition model
valid_face = None

print("Content-Type: application/json")
print()

form = cgi.FieldStorage()
image_data = form.getvalue("image")

if image_data:
    # Decode the base64 image data
    image_data = image_data.replace("data:image/png;base64,", "")
    image_bytes = base64.b64decode(image_data)
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert image to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    if len(faces) > 0:  # If a face is detected
        # Simulate face verification (replace with actual face recognition)
        valid_face = True
        response = {'success': valid_face}
    else:
        valid_face = False
        response = {'success': False}

    print(json.dumps(response))
