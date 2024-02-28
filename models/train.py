# Description: Train a YOLO model on a custom dataset.

from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model

if __name__ == '__main__':
    # Train the model
    results = model.train(data="../datasets/Cubic100/data.yaml", epochs=100, imgsz=640, plots=True)
