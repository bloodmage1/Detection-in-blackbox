# 블랙박스 영상에 차량 파악

## 1. 시연

<img src="https://github.com/bloodmage1/Detection-in-blackbox
/blob/main/Demonstration/first_capture.png"/>

인상 품질 판독기의 첫화면이다.

---
<img src="https://github.com/bloodmage1/Detection-in-blackbox
/blob/main/Demonstration/load_file.png"/>

원하는 영상을 불러올 수 있다. 현재 업로드된 사용할 수 있는 파일은 TRAIN_0000.mp4, TRAIN_0001.mp4, TRAIN_0004.mp4, TRAIN_0008.mp4 총 네개다. 

---

<img src="https://github.com/bloodmage1/Detection-in-blackbox
/blob/main/Demonstration/Original_video_play.png"/>

불러온 파일을 재생할 수 있다. 원본 파일은 1280x 720이지만, 

---

<img src="https://github.com/bloodmage1/Detection-in-blackbox
/blob/main/Demonstration/first_capture.png"/>

predict 버튼을 클릭하면 인삼의 품질을 확인할 수 있다.

---
<img src="https://github.com/bloodmage1/Detection-in-blackbox
/blob/main/Demonstration/first_capture.png"/>

predict 버튼을 클릭하면 인삼의 품질을 확인할 수 있다.



## 2. 데이터
[https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71319] 이 곳에서 데이터를 확인하실 수 있습니다.


## 3. 학습결과

Yolov5를 사용하여 69.5%의 결과를 찾은 것을 확인하고, 왜 분류모델에 객체 탐지에 적합한 Yolo를 쓰는 것보다 최신 분류모델을 쓰는 것이 더 결과가 잘 나올 것 같아, 직접 사용해 보고 그 것을 쉽게 확인할 수 있도록 PyQt에 담았다.

생각보다 육안으로 확인해보아도 이미지에 유별난 특징을 찾기 힘들어, 이미지의 크기를 256X256 까지 줄이는 대신 batch_size를 늘리고 학습률은 줄여 학습시간을 단축시켰다. 하지만 학습 정확도는 85.9% 까지 늘릴 수 있었다.