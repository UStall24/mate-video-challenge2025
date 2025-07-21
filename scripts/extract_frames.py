import cv2
import os

video_path = 'data/raw_video.mp4'
output_folder = 'data/frames'
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if count % int(fps) == 0:  # 1 Frame pro Sekunde
        frame_filename = os.path.join(output_folder, f"frame_{count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
    count += 1

cap.release()
print("frames saved:", output_folder)