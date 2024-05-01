import cv2
import torch
import threading
import numpy as np
import time

# Load YOLOv5 model
class nazar():

    def __init__(self):
        
        self.cap = cv2.VideoCapture('Video source path')
        params = cv2.TrackerVit_Params()
        params.net = "Tracker VIT.onnx file path"

        self.tracker = cv2.TrackerVit_create(params)

        self.model = torch.hub.load("YOLOv7 repository path", "custom" , "Detector model weights path" , force_reload=True,source="local")
        self.detection_flag = True
        self.tracker_flag = False


    def video(self):
        while True:
            ret , self.frame = self.cap.read()
            
            if self.detection_flag is True:
                self.detections_list = self.detections(self.frame)

            elif self.tracker_flag is True:
                self.tracking, box = self.tracker.update(self.frame)
                cv2.rectangle(self.frame,(box[0],box[1]),(box[0]+box[2],box[1]+box[3]),(0,255,0),2)

            cv2.imshow('Video',self.frame)

            cv2.setMouseCallback('Video', self.mouse_callback)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('r'):
                self.detection_flag = True
                self.tracker_flag = False


    def detections(self,frame):
    
        try:
            self.detection_results = self.model(frame)
            return self.DrawDetectionBoxes(self.detection_results)

        except: pass
        #time.sleep(0.2)

    def DrawDetectionBoxes(self,detection_results):
        detections_list = []
        try:
            for i in range(len(detection_results.xyxy[0][0])):
                    
                if detection_results.xyxy[0][0] is not None:    
                    x1 = detection_results.xyxy[0][i][0]
                    y1 = detection_results.xyxy[0][i][1]
                    x2 = detection_results.xyxy[0][i][2]
                    y2 = detection_results.xyxy[0][i][3]


                    x1 = int(x1)
                    y1 = int(y1)
                    x2 = int(x2)
                    y2 = int(y2)

                    bbox = x1,y1,x2,y2
                    detections_list.append(bbox)
                    
                
                    detection_results.pandas().xyxy[0].value_counts('name')  
                
                    cv2.rectangle(self.frame,(x1,y1),(x2,y2),(255,0,0),2)
            return detections_list

        except: pass

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            for bbox in self.detections_list:
                x1, y1, x2, y2 = bbox
                if x1 <= x <= x2 and y1 <= y <= y2:
                    print("Clicked within bounding box:", bbox)
                    self.tracker_flag = True
                    self.detection_flag = False
                    tracker_box = (bbox[0],bbox[1],bbox[2]-bbox[0],bbox[3]-bbox[1])
                    self.tracker.init(self.frame,tracker_box)

   
            
        
if __name__=="__main__":
    
    obj = nazar()
    obj.video()



