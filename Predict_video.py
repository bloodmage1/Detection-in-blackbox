import sys
sys.coinit_flags = 2

import pythoncom
import pyautogui

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from queue import Queue
import threading
from qt_material import apply_stylesheet
import pyrealsense2 as rs

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PIL import Image, ImageDraw, ImageFont

from time import time, sleep
import cv2
import numpy as np
from sklearn.cluster import DBSCAN
import socket
import io

import warnings

warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2

button_size_x = 180
button_size_y = 40
edit_line_size = 120
c_size = 30

hover_style = """
    QPushButton:hover {
        color: #FFFFFF;
        font-weight: bold;}
"""

class Find_Car_in_blackbox(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.UI초기화()

    def UI초기화(self):
        Main_box = QHBoxLayout()

        Main_box.addStretch(1)
        Main_box.addWidget(self.Original_Video(), 7)
        Main_box.addWidget(self.Predict_Video(), 7)
        Main_box.addWidget(self.Controller(), 1)

        self.scrollArea = QScrollArea()
        self.setCentralWidget(self.scrollArea)

        central_widget = QWidget()
        central_widget.setLayout(Main_box)
        self.scrollArea.setWidget(central_widget)
        self.scrollArea.setWidgetResizable(True) 

        apply_stylesheet(self.app, theme='light_cyan.xml')
        self.setWindowTitle('차 검출기')
        self.setWindowIcon(QIcon('Title.png'))
        self.setGeometry(0, 0, 1500, 900)
        self.show()

    def Original_Video(self):
        main_screen_widget = QWidget(self)

        main_screen_layout = QVBoxLayout(main_screen_widget)

        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 640, 360)  # Set the QLabel size to fit the new window size
        main_screen_layout.addWidget(self.label)

        self.play_button = QPushButton('Play', self)
        self.play_button.clicked.connect(self.play_video)
        main_screen_layout.addWidget(self.play_button)

        self.cap = cv2.VideoCapture(video_path)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        return main_screen_widget
    

    def play_video(self):
        self.timer.start(30)  # Start the timer to update the frame every 30 ms

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 360))  # Resize the frame to fit the QLabel
            image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_BGR888)
            self.label.setPixmap(QPixmap.fromImage(image))
        else:
            self.timer.stop()
            self.cap.release()

    def closeEvent(self, event):
        self.cap.release()

    def Predict_Video(self):
        main_screen_widget = QWidget(self)

        main_screen_layout = QVBoxLayout(main_screen_widget)

        self.label_p = QLabel(self)
        self.label_p.setGeometry(10, 10, 640, 360)  # Set the QLabel size to fit the new window size
        main_screen_layout.addWidget(self.label_p)

        self.play_button_p = QPushButton('Play', self)
        self.play_button_p.clicked.connect(self.play_video_p)
        main_screen_layout.addWidget(self.play_button_p)

        self.cap_p = cv2.VideoCapture(video_path)
        self.timer_p = QTimer()
        self.timer_p.timeout.connect(self.update_frame_p)
        return main_screen_widget

    def play_video_p(self):
        self.timer_p.start(30)  # Start the timer to update the frame every 30 ms

    def update_frame_p(self):
        ret, frame = self.cap_p.read()
        if ret:
            frame = cv2.resize(frame, (640, 360))  # Resize the frame to fit the QLabel
            image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_BGR888)
            self.label_p.setPixmap(QPixmap.fromImage(image))
        else:
            self.timer_p.stop()
            self.cap_p.release()


    def closeEvent(self, event):
        self.cap_p.release()


    def Controller(self):
        Load_Image_widget = QWidget(self)

        self.Load_Image_label = QLabel('File', self)
        self.Load_Image_label.setFont(QFont('Helvetica',pointSize=15, weight=1))

        self.Load_button = QPushButton('Load File', self)
        self.Load_button.setFixedSize(button_size_x, button_size_y) 
        self.Load_button.setStyleSheet(hover_style)
        self.Load_button.clicked.connect(self.Load_image)

        self.Predict_button = QPushButton('Predict', self)
        self.Predict_button.setFixedSize(button_size_x, button_size_y) 
        self.Predict_button.setStyleSheet(hover_style)
        self.Predict_button.clicked.connect(self.Predict_image)

        self.Delete_button = QPushButton('Delete', self)
        self.Delete_button.setFixedSize(button_size_x, button_size_y) 
        self.Delete_button.setStyleSheet(hover_style)
        self.Delete_button.clicked.connect(self.Delete_image)

        AGV_state_layout = QVBoxLayout(Load_Image_widget)
        AGV_state_layout.addWidget(self.Load_Image_label)
        AGV_state_layout.addWidget(self.Load_button)
        AGV_state_layout.addWidget(self.Predict_button)
        AGV_state_layout.addWidget(self.Delete_button)

        Load_Image_widget.setLayout(AGV_state_layout)
        return Load_Image_widget
    

####
    def Load_image(self):
        '''
        RGB IMAGE 불러오기를 클릭하여 
        파일 확장자명이 .jpg이면 This_is_rgb_screen에 jpg 이미지를 띄운다.
        '''
        self.Image_name = QFileDialog.getOpenFileName(self, 'Open file', './')

        if self.Image_name[0].endswith('.png') or self.Image_name[0].endswith('.jpg'):
            self.image_file_rgb = cv2.imread(self.Image_name[0])
            
            self.backup_image = self.image_file_rgb.copy()
            self.This_is_screen.figure.clear() 
            ax = self.This_is_screen.figure.add_subplot(111)
            ax.axis('off')
            ax.imshow(self.image_file_rgb)
            self.This_is_screen.draw()
            self.image_displayed_rgb = True
        else:
            QMessageBox.warning(self, "알림", "이것은 이미지 파일이 아닙니다!!")

    def Predict_image(self):
        pass

    def Delete_image(self):
        self.This_is_rgb_screen.figure.clear()
        ax = self.This_is_rgb_screen.figure.add_subplot(111)
        ax.axis('off')
        self.This_is_rgb_screen.draw()

app = QApplication(sys.argv)
video_path = "../train/TRAIN_0000.mp4"
execute_instance = Find_Car_in_blackbox(app)
app.exec()
