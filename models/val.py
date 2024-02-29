# Description: Validate the model.

from ultralytics import YOLO


data_yaml = "../datasets/Cubic100/data.yaml"  # path to the data.yaml file

# Load a model
# model = YOLO("custom/cubic100-v8n.pt")
model = YOLO("custom/cubic100-v8s.pt")

if __name__ == '__main__':
    metrics = model.val(data=data_yaml)  # no arguments needed, dataset and settings remembered
    # metrics.box.map    # map50-95
    # metrics.box.map50  # map50
    # metrics.box.map75  # map75
    # metrics.box.maps   # a list contains map50-95 of each category
