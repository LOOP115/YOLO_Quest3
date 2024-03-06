# Description: Predict the bounding boxes of the input image.

from ultralytics import YOLO


# Load a model
version = "cubic100-v8m"
model = YOLO(f"custom/{version}.pt")
print(f"Load {version}")

# Run batched inference on a list of images
path_raw = "../datasets_raw/EVABlocks/Cubic100_raw/cube"
results = model([path_raw + "100.jpg"])  # return a list of Results objects

# Process results list
for result in results:
    result.show()
    # result.save(filename="../datasets_raw/EVABlocks/Cubic100_pred/100.jpg")
