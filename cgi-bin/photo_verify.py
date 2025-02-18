#!/usr/bin/python3

import cgi, json, base64
import cv2
import numpy as np

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
image_data = form.getvalue("image")

if image_data:
    image_data = image_data.replace("data:image/png;base64,", "")
    image_bytes = base64.b64decode(image_data)
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Simulating verification (always allow in this example)
    print("success")
else:
    print("failure")
