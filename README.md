# YOLO on Quest 3

This project utilises the cameras of Quest 3 to identify the shapes and colours of a set of EVA blocks using YOLOv8.

<br>

## **Casting Meta Quest 3 View**

- Developer Hub - Beta Cast 2.0
  - Original (1:1)
  - Left Eye

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
  - Resolution: 1280 &times; 1280
  - FPS: 30

<br>

## [YOLOv8](https://docs.ultralytics.com/)

### [**GitHub**](https://github.com/ultralytics/ultralytics)

### Resources

- YouTube
  - [Ultralytics YOLOv8](https://www.youtube.com/playlist?list=PL1FZnkj4ad1PFJTjW4mWpHZhzgJinkNV0)
  - [YOLOv8 Tutorial](https://www.youtube.com/playlist?list=PLZCA39VpuaZZ1cjH4vEIdXIb0dCpZs3Y5)
- Colab
  - [YOLOv8 Tutorial](https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/tutorial.ipynb#scrollTo=ZY2VXXXu74w5)
  - [How to Train YOLOv8 Object Detection on a Custom Dataset](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb)
- [YOLOv8 Models](https://docs.ultralytics.com/models/yolov8/#overview)

### Installation

* Install [Anaconda](https://www.anaconda.com/download)
* `conda create --name yolov8 python=3.8`
* `conda activate yolov8`
* Install in a **CUDA** environment
  * `conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 ultralytics`
  * If stuck at solving environment, try `conda config --set channel_priority strict`

<br>

## [Dataset](datasets_zip)

### Preparation

- Shot with iPhone
- Compressed to 1280 &times; 1280

- Annotation
  - [roboflow](https://app.roboflow.com/)
  - Secondary check



### EVA Block

<img src="docs/img/evablock1.png" alt="evablock1"  />



#### Cubic100: 100 images of cubes and cuboids

#### Classes

<img src="docs/img/Cubic100-classes.png" alt="Cubic100-classes"  />

| Preprocessing                                       | Augmentation                                                 | Train | Valid | Split |
| --------------------------------------------------- | ------------------------------------------------------------ | ----- | ----- | ----- |
| Auto-Orient<br />Resize: Stretch to 640 &times; 640 | Flip: Horizontal<br />Rotation: Between -15&deg; and +15&deg; | 209   | 20    | 10    |



### [Train Custom Models](models/custom)

|  Model  | dataset  | epochs | size<br />(pixels) |                     results                     |
| :-----: | :------: | :----: | :----------------: | :---------------------------------------------: |
| yolov8n | Cubic100 |  100   |        640         | [cubic100-v8n](models/runs/detect/cubic100-v8n) |
| yolov8s | Cubic100 |  100   |        640         | [cubic100-v8s](models/runs/detect/cubic100-v8s) |
| yolov8m | Cubic100 |  100   |        640         | [cubic100-v8m](models/runs/detect/cubic100-v8m) |
| yolov8l | Cubic100 |  100   |        640         | [cubic100-v8l](models/runs/detect/cubic100-v8l) |
| yolov8x | Cubic100 |  100   |        640         | [cubic100-v8x](models/runs/detect/cubic100-v8x) |



### Performance

##### Device: NVIDIA GeForce RTX 4090

|                            Model                             | mAP<sup>val</sup><br />50-95 | preprocess<br />(ms) | inference<br />(ms) | postprocess<br />(ms) | params<br />(M) | FLOPs<br />(B) |
| :----------------------------------------------------------: | :--------------------------: | :------------------: | :-----------------: | :-------------------: | :-------------: | :------------: |
| [cubic100-v8n](https://www.youtube.com/watch?v=XrV9wmnmguc&list=PLGZ6M30GmbVM7x_OCORl0q7Z4LuDY4KiY&index=1) |            0.927             |         1.6          |        10.1         |          3.3          |       3.2       |      8.7       |
| [cubic100-v8s](https://www.youtube.com/watch?v=stGOMXj_bpk&list=PLGZ6M30GmbVM7x_OCORl0q7Z4LuDY4KiY&index=2) |            0.937             |         1.8          |        11.3         |          3.2          |      11.2       |      28.6      |
| [cubic100-v8m](https://www.youtube.com/watch?v=ShZzQ32Dk94&list=PLGZ6M30GmbVM7x_OCORl0q7Z4LuDY4KiY&index=3) |            0.944             |         1.6          |        14.4         |          3.2          |      25.9       |      78.9      |
|                         cubic100-v8l                         |            0.943             |         2.2          |        16.9         |          3.5          |      43.7       |     165.2      |
|                         cubic100-v8x                         |            0.919             |         2.3          |        19.4         |          3.1          |      68.2       |     257.8      |

