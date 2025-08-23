import os
import csv
import matplotlib.pyplot as plt
from pathlib import Path

# === Parameter ===
label_dir = Path("runs/detect/predict/labels")
output_csv = Path("output/spreadsheet/fish_counts_all_frames.csv")
output_plot = Path("output/graphs/fish_count_all_frames.png")

total_frames = 4545
video_duration_seconds = 151  # 2min 31s = 151s
frame_rate = total_frames / video_duration_seconds

# === Frameweise Fische zählen ===
frame_counts = {}

for label_file in sorted(label_dir.glob("*.txt")):
    # Dateinamen wie 'raw_video_123.txt' → extrahiere 123
    try:
        name_parts = label_file.stem.split('_')
        frame_num = int(name_parts[-1])  # letztes Element
    except ValueError:
        print(f"[WARNUNG] Datei übersprungen: {label_file.name}")
        continue

    with open(label_file, "r") as f:
        detections = f.readlines()
        frame_counts[frame_num] = len(detections)

# === CSV exportieren ===
output_csv.parent.mkdir(parents=True, exist_ok=True)
with open(output_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Time (s)", "Fish Count"])
    for frame_num in sorted(frame_counts.keys()):
        time_sec = round(frame_num / frame_rate, 2)
        writer.writerow([time_sec, frame_counts[frame_num]])

print(f"[✓] CSV gespeichert: {output_csv}")

# === Diagramm erzeugen ===
times = [round(f / frame_rate, 2) for f in sorted(frame_counts.keys())]
counts = [frame_counts[f] for f in sorted(frame_counts.keys())]

plt.figure(figsize=(12, 6))
plt.plot(times, counts, linestyle="-", linewidth=1.5)
plt.xlabel("Time (seconds)")
plt.ylabel("# of Fish")
plt.title("Fish Count per Frame")
plt.grid(True)
plt.tight_layout()
output_plot.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_plot)
plt.show()

print(f"[✓] Diagramm gespeichert: {output_plot}")
