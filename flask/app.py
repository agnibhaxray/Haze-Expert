import cv2
import numpy as np
import argparse
import dehaze
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

# Define a folder to store processed videos
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Create the folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']

        if uploaded_file.filename != '':
            # Save the uploaded video to the uploads folder
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            uploaded_file.save(video_path)

            # Process the video
            processed_video_path = process_video(video_path)

            return render_template('result.html', processed_video=processed_video_path)

    return redirect(url_for('index'))

def process_video(video_path):
    # Define the path for the processed video
    processed_video_path = os.path.join(app.config['PROCESSED_FOLDER'], 'processed_' + os.path.basename(video_path))

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Create a VideoWriter object to write the processed video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can choose a different codec if needed
    out = cv2.VideoWriter(processed_video_path, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Apply your dehazing algorithm to 'frame' here
        # Replace this with your actual dehazing code
        processed_frame = frame

        out.write(processed_frame)

    cap.release()
    out.release()

    return processed_video_path

if __name__ == '__main__':
    app.run(debug=True)
