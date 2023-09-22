import os
import time
import threading
import stream_frame
fps=30.0
directory = './input_frames/'

not_available_counter=0
for i in range(10000):  # 0000 to 9999
    filename = f'frame_{i:04d}.jpg'  # Format the filename with leading zeros
    filepath = os.path.join(directory, filename)
    print(not_available_counter)
    if(not_available_counter > 2):
          print("stream completed")
          exit(0)
    if os.path.exists(filepath):
        print("filepath:"+filepath)
        print("directory"+directory)
        print("filename:"+filename)
        #stream_video.stream_images(directory,fps)
        stream_frame.stream_images(directory,filename,fps)
        # Do something with the file (e.g., read or process it)
        print(f"Processing {filepath}")
    else:
        print("not available, waiting: for file " + filepath)
        not_available_counter=not_available_counter+1
        print(not_available_counter)
        time.sleep(1)
        i=i-1
        continue
    
        
