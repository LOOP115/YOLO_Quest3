import cv2
import numpy as np
from ultralytics import YOLO

labels = ["cube", "cuboid-a", "cuboid-b", "cuboid-c"]


def get_shape(path, image, show=False):
    # Load a model
    version = "cubic100-v8m"
    model = YOLO(f"../models/custom/{version}.pt")
    print(f"Load {version}")

    # Run batched inference on a list of images
    results = model(f"{path}/{image}.jpg")

    predictions = []
    for result in results:
        if show:
            result.show()

        pred = []
        boxes = result.boxes
        cls = boxes.cls.cpu().tolist()
        conf = boxes.conf.cpu().tolist()
        xyxy = boxes.xyxy.cpu().tolist()

        pred.append(cls)
        pred.append(conf)
        pred.append(xyxy)
        predictions.append(pred)
    return predictions


def get_color(image, bbox, focus_factor=0.5):
    (startX, startY, endX, endY) = bbox
    width = endX - startX
    height = endY - startY

    # Calculate the central region based on the focus factor
    center_x = startX + width // 2
    center_y = startY + height // 2
    focus_width = int(width * focus_factor) // 2
    focus_height = int(height * focus_factor) // 2

    # Define the focused ROI in the image
    roi = image[center_y - focus_height:center_y + focus_height, center_x - focus_width:center_x + focus_width]

    # Convert the object image to the HSV color space
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Calculate the most frequent hue in the HSV image
    hue = hsv[:, :, 0]
    hist = cv2.calcHist([hue], [0], None, [180], [0, 180])
    predominant_hue = np.argmax(hist)
    color = hue_to_color(predominant_hue)
    return color


# This function converts a hue value to a color name based on general hue ranges
def hue_to_color(hue):
    # print(hue)
    if hue < 5 or hue > 175:
        return 'red'
    elif hue < 33:
        return 'yellow'
    elif hue < 78:
        return 'green'
    elif hue < 131:
        return 'blue'
    elif hue < 170:
        return 'violet'
    else:
        return 'red'


def get_category(path, image, show=False):
    res = get_shape(path, image, show)[0]
    cls = res[0]
    conf = res[1]
    bboxes = res[2]

    cnt = 0
    print()
    for bbox in bboxes:
        bbox_int = [int(i) for i in bbox]
        color = get_color(cv2.imread(f"{path}/{image}.jpg"), bbox_int)
        print(f"{color} {labels[int(cls[cnt])]}  {round(conf[cnt], 2)}")
        cnt += 1


img_dir_path = "../datasets_raw/EVABlocks/Cubic100_raw"
img = "cube100"
get_category(img_dir_path, img, show=True)
