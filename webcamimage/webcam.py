import cv2
import dehaze  # Import your dehazing function

# Create a VideoCapture object for the default camera (webcam)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame from the webcam
    success, frame = video_capture.read()

    if not success:
        break

    # Call your dehazing function to process the frame
    processed_frame = dehaze.dehaze(frame)

    # Display the processed frame (optional)
    cv2.imshow('Processed Frame', processed_frame)

    # Press 'q' to quit the video capture loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close any OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
