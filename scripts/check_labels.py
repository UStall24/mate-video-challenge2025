import os

img_dir = "data/frames/images/train"
label_dir = "data/frames/labels/train"

img_files = [f for f in os.listdir(img_dir) if f.endswith(".jpg")]
valid = 0
invalid = []

for img in img_files:
    label_file = img.replace(".jpg", ".txt")
    label_path = os.path.join(label_dir, label_file)

    if not os.path.exists(label_path):
        invalid.append((img, "❌ Kein Label"))
    elif os.path.getsize(label_path) == 0:
        invalid.append((img, "⚠️ Leeres Label"))
    else:
        valid += 1

print(f"✅ Gültige Trainingsbeispiele: {valid}")
print(f"❌ Ungültige/fehlende Labels: {len(invalid)}")

for img, reason in invalid:
    print(f"{img}: {reason}")
