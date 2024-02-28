# Real-time XR Object Detection



## **Casting Meta Quest 3 View**

- Developer Hub - Beta Cast 2.0
- Add the casting window to [OBS](https://obsproject.com/) sources
- Stream settings
  - Server: `rtmp://127.0.0.1`
  - Set an arbitrary **Stream Key**
- Use [MonaServer](https://www.monaserver.ovh/) for local RTMP streaming
  - `rtmp://127.0.0.1//<Stream Key>`
- Output Settings
  - Video Bitrate: 1800 Kbps
  - Audio Bitrate: 64
  - Encoder Preset: Fastest
- Video Settings
  - Resolution: 1280 * 1280
  - FPS: 30



## [YOLOv8](https://docs.ultralytics.com/)

### [**GitHub**](https://github.com/ultralytics/ultralytics)

### Resources

- YouTube
  - [Ultralytics YOLOv8](https://www.youtube.com/playlist?list=PL1FZnkj4ad1PFJTjW4mWpHZhzgJinkNV0)
  - [YOLOv8 Tutorial](https://www.youtube.com/playlist?list=PLZCA39VpuaZZ1cjH4vEIdXIb0dCpZs3Y5)
  
- Colab
  - [YOLOv8 Tutorial](https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/tutorial.ipynb#scrollTo=ZY2VXXXu74w5)
  - [How to Train YOLOv8 Object Detection on a Custom Dataset](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb)

- Prepare the dataset
  
  - Shot with iPhone
  - Compressed to 1280 * 1280
  
  - Annotation
    - [roboflow](https://app.roboflow.com/)
    - review



### Installation

* Install [Anaconda](https://www.anaconda.com/download)
* `conda create --name yolov8 python=3.8`
* `conda activate yolov8`
* Install in a **CUDA** environment
  * `conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 ultralytics`
  * If stuck at solving environment, try `conda config --set channel_priority strict`



### [Dataset](datasets_zip) - EVA Block

<img src="docs/img/evablock1.png" alt="evablock1"  />



#### Cubic100: 100 images of cubes and cuboids

#### Classes

<img src="docs/img/Cubic100-classes.png" alt="Cubic100-classes"  />



| Preprocessing                                 | Augmentation                                        | Train | Valid | Split |
| --------------------------------------------- | --------------------------------------------------- | ----- | ----- | ----- |
| Auto-Orient<br />Resize: Stretch to 640 * 640 | Flip: Horizontal<br />Rotation: Between -15 and +15 | 209   | 20    | 10    |



### [Train Custom Models](models/custom)

| Model           | Dataset  | Pretrained | Epochs | Size |
| --------------- | -------- | ---------- | ------ | ---- |
| Cubic100-v8n.pt | Cubic100 | yolov8n.pt | 100    | 640  |



### Evaluation

| Model                                       |      |      |      |
| ------------------------------------------- | ---- | ---- | ---- |
| [Cubic100-v8n.pt](models/runs/detect/train) |      |      |      |

