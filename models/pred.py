# Description: Predict the bounding boxes of the input image.

from ultralytics import YOLO


# Load a model
version = "cubic100-v8m"
model = YOLO(f"runs/detect/{version}/weights/best.pt")

# Run batched inference on a list of images
path_raw = "../datasets_raw/EVABlocks/cube/cube"
results = model([path_raw + "100.jpg"])  # return a list of Results objects

# Process results list
for result in results:
    print(f"Load {version}")
    boxes = result.boxes  # Boxes object for bounding box outputs
    result.show()  # display to screen
    # result.save(filename='result.jpg')
