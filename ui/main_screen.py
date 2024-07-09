from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QScrollArea, QWidget
from PySide6.QtGui import QIcon
from qt_material import apply_stylesheet
from ui.original_video import OriginalVideo
from ui.predict_video import PredictVideo
from ui.controller import Controller

class FindCarInBlackbox(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.video_path = None  
        self.cap = None
        self.cap_p = None
        self.UI초기화()

    def UI초기화(self):
        main_box = QHBoxLayout()

        main_box.addStretch(1)
        main_box.addWidget(OriginalVideo(self), 7)
        main_box.addWidget(PredictVideo(self), 7)
        main_box.addWidget(Controller(self), 1)

        self.scrollArea = QScrollArea()
        self.setCentralWidget(self.scrollArea)

        central_widget = QWidget()
        central_widget.setLayout(main_box)
        self.scrollArea.setWidget(central_widget)
        self.scrollArea.setWidgetResizable(True) 

        apply_stylesheet(self.app, theme='light_cyan.xml')
        self.setWindowTitle('차 검출기')
        self.setWindowIcon(QIcon('./app_img/Title.png'))
        self.setGeometry(0, 0, 1400, 800)
        self.show()

    def closeEvent(self, event):
        if self.cap:
            self.cap.release()
        if self.cap_p:
            self.cap_p.release()