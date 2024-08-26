# Detection_in_blackbox

## 1. Demonstration

This repository contains a tutorial of Car detection using YOLO.

<img src="https://github.com/bloodmage1/Detection-in-blackbox/blob/main/Demonstration/first_capture.png"/>

This is the first screen when you run the application.

---
<img src="https://github.com/bloodmage1/Detection-in-blackbox/blob/main/Demonstration/load_file.png"/>

You can import the video you want. Currently, there are four files available that have been uploaded. Each file is 'TRAIN_0000.mp4', 'TRAIN_0001.mp4', 'TRAIN_0004.mp4', and TRAIN_0008.mp4. that located in the 'test_mp4' folder.

---

<img src="https://github.com/bloodmage1/Detection-in-blackbox/blob/main/Demonstration/Original_video_play.gif"/>

You can play the imported file. The original file is 1280x720, but the video is played is resized to 640x360, and then played.

---

<img src="https://github.com/bloodmage1/Detection-in-blackbox/blob/main/Demonstration/predict_video.png"/>

By clicking the 'predict' button, the 'predicted_video.mp4' file can be created using the yolo model. This file is an image in which the bounding box is painted by predicting the vehicle on the imported image.

---
<img src="https://github.com/bloodmage1/Detection-in-blackbox/blob/main/Demonstration/Predicted_video_play.gif"/>

You can play the predicted video.

## 2. Setup the environment

The OS is ubuntu-16.04, cuda:11.8. A Dockerfile with all dependencies is provided. You can build it with


```
docker build -t your_container:your_tag .
```

## 3. Object detection model

I choose [yolov5](https://pytorch.org/hub/ultralytics_yolov5/) an object detection model


## 4. Enabling Python Virtual Environments
```
source blackbox_car/bin/activate
```

## 5. Running Detection_in_blackbox

CAR DETECTION can be performed using the GUI program(Detection_in_blackbox). As shown in 1(Demonstration), an video file is imported and prediction proceeds.


## 6. Development Environment

- Window OS, Window 11
- Python 3.8.7
- PySide6
- torch 2.3.1+cu11.8
- torchaudio 2.3.1+cu11.8
- torchvision 0.18.1+cu11.8

## 7. Directory Structure

```
FindCarInBlackbox/
│
├── main.py
├── ui/
│   ├── main_screen.py
│   ├── original_video.py
│   ├── predict_video.py
│   └── controller.py
└── utils_car/
    └── model.py
```
  
## 8. 각 함수의 기능 설명

### OriginalVideo 
  - 원본 비디오를 표시하는 위젯을 생성하고 반환합니다.
  - 비디오 표시를 위한 QLabel과 비디오 재생을 시작하는 재생 버튼을 설정합니다.
  - 비디오 캡처 객체와 비디오 프레임을 업데이트하기 위한 타이머를 초기화합니다.
 
- def play_video(self)
  - 기존의 비디오 캡처 객체를 해제합니다.
  - video_path에 지정된 비디오 파일을 열고 프레임을 업데이트하기 위한 타이머를 시작합니다.
  - 비디오 파일이 로드되지 않은 경우 경고를 표시합니다.

- def update_frame(self)
  - 비디오 캡처 객체에서 프레임을 읽어옵니다.
  - 프레임을 크기 조정하고 QImage로 변환하여 QLabel을 업데이트하여 프레임을 표시합니다.
  - 비디오가 끝나면 타이머를 중지하고 비디오 캡처 객체를 해제합니다.
  

### PredictVideo 
  - 예측 비디오를 표시하는 위젯을 생성하고 반환합니다.
  - 비디오 표시를 위한 QLabel과 예측 비디오 재생을 시작하는 재생 버튼을 설정합니다.
  - 예측 비디오 프레임을 업데이트하기 위한 비디오 캡처 객체와 타이머를 초기화합니다.

- def play_video_p(self)
  - 기존의 예측 비디오 캡처 객체를 해제합니다.
  - 예측 비디오 파일을 열고 프레임을 업데이트하기 위한 타이머를 시작합니다.

- def update_frame_p(self)
  - 예측 비디오 캡처 객체에서 프레임을 읽어옵니다.
  - 프레임을 크기 조정하고 QImage로 변환하여 QLabel을 업데이트하여 프레임을 표시합니다.
  - 예측 비디오가 끝나면 타이머를 중지하고 비디오 캡처 객체를 해제합니다.

### Controller 
  - 컨트롤 버튼(파일 로드, 예측, 삭제)이 있는 위젯을 생성하고 반환합니다.
  - 컨트롤 버튼의 레이아웃과 스타일을 설정합니다.
  - 버튼을 해당 메서드(Load_Video, Predict_image, Delete_image)에 연결합니다.

- def load_video(self)
  - 파일 대화 상자를 열어 비디오 파일을 선택하고 video_path를 업데이트합니다.
  - 비디오 경로가 업데이트되었음을 나타내는 메시지를 표시합니다.
  - 파일을 선택하지 않은 경우 경고를 표시합니다.

- def predict_image(self)
  - YOLO 객체 감지기를 사용하여 video_path에 지정된 비디오 파일에서 객체 감지를 수행합니다.
  - 예측이 완료되었음을 나타내는 메시지를 표시합니다.
  - 비디오 파일이 로드되지 않은 경우 경고를 표시합니다.

- def delete_image(self)
  - 원본 및 예측 비디오를 표시하는 QLabel을 지웁니다.

## 9. Errors I encountered
If an error occurs, please contact us via email.

breakprejudice@naver.com
