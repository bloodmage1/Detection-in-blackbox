import os
import cv2
import torch

class YOLOObjectDetector:
    def __init__(self, model_name='yolov5s'):
        self.model = torch.hub.load('ultralytics/yolov5', model_name, pretrained=True)

    def detect_objects_in_video_and_save_frames(self, video_path, output_dir="./testtest", frame_rate=10):
        cap = cv2.VideoCapture(video_path)
        frame_count = 0

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = self.model(frame)
            detections = results.xyxy[0].cpu().numpy()  

            for *xyxy, conf, cls in detections:
                if results.names[int(cls)] == 'car': 
                    label = f'{results.names[int(cls)]} {conf:.2f}'
                    x1, y1, x2, y2 = map(int, xyxy)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.png')
            cv2.imwrite(frame_filename, frame)
            frame_count += 1

        cap.release()
        images = [img for img in os.listdir(output_dir) if img.endswith(".png")]
        images.sort() 

        first_frame_path = os.path.join(output_dir, images[0])
        frame = cv2.imread(first_frame_path)
        height, width, layers = frame.shape

        fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
        video_writer = cv2.VideoWriter("predicted_video.mp4", fourcc, frame_rate, (width, height))
        for image in images:
            img_path = os.path.join(output_dir, image)
            frame = cv2.imread(img_path)
            video_writer.write(frame)

        video_writer.release()