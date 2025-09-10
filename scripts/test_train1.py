from ultralytics import YOLO
import torch

def main():
    model = YOLO("yolov8n.yaml") 

    device = 0 if torch.cuda.is_available() else "cpu"

    model.train(
        data="data/data.yaml", 
        epochs=1000,   
        imgsz=640,
        batch=2,             
        device=device,        
        cache=True,      
        workers=2,           
        mosaic=0.4,
        mixup=0.0,
        project="runs/detect",
        name="train_cpu"
    )

if __name__ == "__main__":
    main()
