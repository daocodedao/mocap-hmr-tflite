# Mocap with HMR : Tensorflow Lite
![](assets/demo.gif)


## Installation
1. Download [`models`](https://drive.google.com/file/d/113l-yZkstJJez2cCYQLkWo3jg-I7bdjs/view?usp=sharing) and place in project directory
models
    HMR.tflite
    lite_pose_detection.tflite
    smpl_model.pkl

2. Install python dependencies  
    ```
    python3.10 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    [>>> for Linux user](https://www.tensorflow.org/lite/guide/python#install_tensorflow_lite_for_python)
3. Install Blender and add to PATH

mac
```
brew install --cask blender
```

### Usage
```
venv/bin/python run.py
```

