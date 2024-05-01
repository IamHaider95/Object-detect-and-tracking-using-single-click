This is a repository which detects objects and starts tracking single object when clicked on it. 
This repository is using YOLOv7 detection algorithm with yolov7.pt weights and VIT tracker.

#How to use the repository#
* Clone YOLOv7 repository.
  git clone https://github.com/WongKinYiu/yolov7

* Install requirements.txt needed for YOLOv7 repository to work.
  pip3 install -r requirements.txt
  
* Download "VIT.onnx" tracker file.
  https://drive.google.com/file/d/1rxAobnFcV7A88T8LQtsALnfppgi7u27y/view?usp=sharing
  
* Run "run.py" file. Modify the code and change YOLOv7 repository, detection model weights and "VIT.onnx" paths.
  python3 run.py

#Features#
* Object detection.

* Single object tracking when clicked on a detected object in frame.

* Press 'r' to switch back from single object tracking mode to detection only mode.

  
