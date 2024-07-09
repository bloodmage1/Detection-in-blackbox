# 블랙박스 영상에 차량 파악

## 1. 시연

<img src="https://github.com/bloodmage1/Detection-in-blackbox/blob/main/Demonstration/first_capture.png"/>

실행했을 시 첫화면이다.

---
<img src="https://github.com/bloodmage1/Detection-in-blackbox/blob/main/Demonstration/load_file.png"/>

원하는 영상을 불러올 수 있다. 현재 업로드된 사용할 수 있는 파일은 TRAIN_0000.mp4, TRAIN_0001.mp4, TRAIN_0004.mp4, TRAIN_0008.mp4 총 네개다. 각 파일들은 test_mp4 폴더 안에 존재한다.

---

<img src="https://github.com/bloodmage1/Detection-in-blackbox/blob/main/Demonstration/Original_video_play.gif"/>

불러온 파일을 재생할 수 있다. 원본 파일은 1280x720이지만, 재생 영상은 640x360으로 resize 된 후 재생된다.

---

<img src="https://github.com/bloodmage1/Detection-in-blackbox/blob/main/Demonstration/predict_video.png"/>

predict 버튼을 클릭하여 yolo 모델을 이용해, predicted_video.mp4 파일을 생성할 수 있다. 이 파일은 불러온 영상에 차량을 predict하여 boundingbox를 칠한 영상이다.

---
<img src="https://github.com/bloodmage1/Detection-in-blackbox/blob/main/Demonstration/Predicted_video_play.gif"/>

predict한 파일을 재생할 수 있다. 

## 2. 개발환경

- Window OS, Window 11
- Python 3.8.7
- PySide6
- torch 2.3.1+cu11.8
- torchaudio 2.3.1+cu11.8
- torchvision 0.18.1+cu11.8

## 3. 디렉토리 구조

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
  
## 4. 각 함수의 기능 설명

### OriginalVideo 클래스
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
  

### PredictVideo 클래스
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

### Controller 클래스
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


## 5. 데이터
[https://dacon.io/competitions/official/236064/overview/description] 이 곳에서 데이터를 확인하실 수 있습니다. 전체 50프레임이고 5초 길이에 1280x720 해상도의 1초당 10프레임이 재생됩니다.


