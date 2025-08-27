import os
import random
import shutil

# Quelle
image_dir = "data/frames/images/all"
label_dir = "data/frames/labels/all"

# Zielverzeichnisse
train_image_dir = "data/frames/images/train"
val_image_dir = "data/frames/images/val"
train_label_dir = "data/frames/labels/train"
val_label_dir = "data/frames/labels/val"

# Zielordner erstellen, falls nicht vorhanden
for directory in [train_image_dir, val_image_dir, train_label_dir, val_label_dir]:
    os.makedirs(directory, exist_ok=True)

# Alle .jpg-Dateien auflisten
all_images = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]

# Zufällig mischen und aufteilen
random.shuffle(all_images)
val_count = int(0.2 * len(all_images))  # z.B. 20 % für Validation
val_images = all_images[:val_count]
train_images = all_images[val_count:]

def copy_files(image_list, target_image_dir, target_label_dir):
    for img_name in image_list:
        label_name = img_name.replace(".jpg", ".txt")

        src_img = os.path.join(image_dir, img_name)
        src_lbl = os.path.join(label_dir, label_name)

        dst_img = os.path.join(target_image_dir, img_name)
        dst_lbl = os.path.join(target_label_dir, label_name)

        shutil.copy(src_img, dst_img)
        if os.path.exists(src_lbl):
            shutil.copy(src_lbl, dst_lbl)

# Dateien kopieren
copy_files(train_images, train_image_dir, train_label_dir)
copy_files(val_images, val_image_dir, val_label_dir)

print(f"✅ Kopiert: {len(train_images)} Training-Bilder und {len(val_images)} Validation-Bilder.")
