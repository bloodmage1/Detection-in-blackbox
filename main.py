import sys
from PySide6.QtWidgets import QApplication
from ui.main_screen import FindCarInBlackbox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    execute_instance = FindCarInBlackbox(app)
    app.exec()