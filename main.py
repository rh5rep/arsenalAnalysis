import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Soccer Analysis Platform")
        self.setGeometry(100, 100, 800, 600)

        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)

        self.import_video_button = QPushButton("Import Video")
        self.import_video_button.clicked.connect(self.import_video)

        self.analyze_video_button = QPushButton("Analyze Video")
        self.analyze_video_button.clicked.connect(self.analyze_video)


        layout = QVBoxLayout(self.video_label)

        self.setCentralWidget(self.video_label)

    def import_video(self):
        pass

    def analyze_video(self):
        pass


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()