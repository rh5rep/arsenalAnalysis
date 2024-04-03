import sys

import cv2

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QFileDialog


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


        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.import_video_button)
        layout.addWidget(self.analyze_video_button)



        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def import_video(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Video files (*.mp4 *.avi *.mov)")
        file_dialog.setViewMode(QFileDialog.Detail)

        if file_dialog.exec():
            video_path = file_dialog.selectedFiles([0])

import cv2

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QFileDialog


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


        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.import_video_button)
        layout.addWidget(self.analyze_video_button)



        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

        self.video_capture = None

    def import_video(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Video files (*.mp4 *.avi *.mov)")
        file_dialog.setViewMode(QFileDialog.Detail)

        if file_dialog.exec():
            video_path = file_dialog.selectedFiles()[0]
            self.video_capture = cv2.VideoCapture(video_path)
            self.display_frame()

    def analyze_video(self):
        pass

    def display_frame(self):
        if self.video_capture is not None:
            ret, frame = self.video_capture.read()
            if ret:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                height, width, channel = frame_rgb.shape
                bytes_per_line = 3*width
                q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
                self.video_label.setPixmap(QPixmap.fromImage(q_image))


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()

    def analyze_video(self):
        pass


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()