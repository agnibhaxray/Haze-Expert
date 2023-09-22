import cv2
import numpy as np
from flask import Flask, render_template, Response

app = Flask(__name__)

# Create a VideoCapture object for the default camera (webcam)
video_capture = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # Capture frame-by-frame from the webcam
        success, frame = video_capture.read()

        if not success:
            break
        else:
            # Encode the frame as JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
