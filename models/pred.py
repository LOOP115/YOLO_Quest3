# Description: Predict the bounding boxes of the input image.

from ultralytics import YOLO


# Load a model
model = YOLO("custom/cubic100-v8m.pt")

# Run batched inference on a list of images
path_raw = "../datasets_raw/EVABlocks/cube/cube"
results = model([path_raw + "100.jpg"])  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    # masks = result.masks  # Masks object for segmentation masks outputs
    # keypoints = result.keypoints  # Keypoints object for pose outputs
    # probs = result.probs  # Probs object for classification outputs
    result.show()  # display to screen
    # result.save(filename='result.jpg')  # save to disk
