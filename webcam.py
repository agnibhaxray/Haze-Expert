import cv2
import numpy as np
from flask import Flask, render_template, Response

app = Flask(__name__)

# Create a VideoCapture object for the default camera (webcam)
video_capture = cv2.VideoCapture(0)

def process_webcam_frames(frame):
    # Example: Invert the colors of the frame
    return cv2.bitwise_not(frame)

def generate_frames():
    while True:
        # Capture frame-by-frame from the webcam
        success, frame = video_capture.read()

        if not success:
            break
        else:
            # Process the frame using your function (e.g., process_webcam_frames)
            processed_frame = process_webcam_frames(frame)

            # Encode the processed frame as JPEG
            _, buffer = cv2.imencode('.jpg', processed_frame)
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
