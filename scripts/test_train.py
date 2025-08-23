from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.yaml")
    model.train(
        data="data/data.yaml",
        epochs=100,
        imgsz=960,
        batch=8,
        device=0,
        cache="ram",
        workers=8,
        amp=False,
        warmup_epochs=5,
        patience=15,
        hsv_h=0.015, hsv_s=0.7, hsv_v=0.4,
        degrees=0.3, translate=0.1, scale=0.5, shear=0.2,
        flipud=0.5, fliplr=0.5,
        mosaic=1.0, mixup=0.2,
        project="runs/detect",
        name="train"
    )

if __name__ == "__main__":
    main()
