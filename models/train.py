# Description: Train a YOLO model on a custom dataset.

from ultralytics import YOLO


data_yaml = "../datasets/Cubic100/data.yaml"  # path to the data.yaml file

# Load a pretrained model
model = YOLO("yolov8x.pt")

if __name__ == '__main__':
    # Train the model
    results = model.train(data=data_yaml, epochs=100, imgsz=640, plots=True)
