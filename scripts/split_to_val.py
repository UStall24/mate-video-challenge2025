import os
import random
import shutil

# Pfade anpassen, falls nötig
image_dir = "frames/images/train"
label_dir = "frames/labels/train"
val_image_dir = "frames/images/val"
val_label_dir = "frames/labels/val"

# Zielordner erstellen, falls nicht vorhanden
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# Liste aller Bilddateien
images = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]
val_images = random.sample(images, 10)  # 10 zufällige Bilder

for img_name in val_images:
    # Passende Label-Datei (gleicher Name, aber .txt)
    label_name = img_name.replace(".jpg", ".txt")

    # Dateien verschieben
    shutil.move(os.path.join(image_dir, img_name), os.path.join(val_image_dir, img_name))
    shutil.move(os.path.join(label_dir, label_name), os.path.join(val_label_dir, label_name))

print(f"✅ Verschoben: {len(val_images)} Bilder und Labels nach val/")
