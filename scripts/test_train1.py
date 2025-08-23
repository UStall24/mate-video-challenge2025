from ultralytics import YOLO

def main():
    model = YOLO("yolov8m.yaml")

    model.train(
        data="data/data.yaml",
        epochs=1000,
        imgsz=640,
        batch=4,
        device=0,
        cache="ram",
        workers=8,
        #patience=30,
        mosaic=0.4,
        mixup=0.0, 
        project="runs/detect",
        name="train",
    )

if __name__ == "__main__":
    main()
