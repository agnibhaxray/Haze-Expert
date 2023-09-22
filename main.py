import subprocess
import sys

command = ["python3","break_video.py",sys.argv[1]]
try:
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Script output:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Error:", e)

command = ["python3","dehaze_frames.py"]
try:
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Script output:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Error:", e)

command = ["python3","save_video.py", sys.argv[2]]
try:
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Script output:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Error:", e)