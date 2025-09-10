from ultralytics import YOLO

def main():
    model = YOLO("runs/detect/modelV1/weights/best.pt")
    model.predict(
        source="data/raw_video.mp4",
        save=True,
        save_txt=True,
        project="runs/detect",
        name="predict",
        exist_ok=True,
        conf=0.25,
        device=0
    )

if __name__ == "__main__":
    main()
