import os
import glob
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QFont, QScreen
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from datetime import datetime
import sys
import cv2
import numpy as np
from menu_caras import MenuCaras

class VideoPlayer(QMainWindow):
    def __init__(self, video_path, main_panel):
        super().__init__()
        self.main_panel = main_panel
        QMainWindow.__init__(self)
        self.setWindowTitle("Reproductor de Video con Detección de Rostros")
        self.setGeometry(200, 200, 1000, 800)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        self.video_widget = QVideoWidget()
        layout.addWidget(self.video_widget)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))
        self.player.play()
        self.showMaximized()

        self.btn_play = QPushButton("Play")
        self.btn_pause = QPushButton("Pause")
        self.btn_stop = QPushButton("Stop")
        self.btn_forward = QPushButton("Adelantar 10s")
        self.btn_return = QPushButton("Volver al inicio")

        for btn in [self.btn_play, self.btn_pause, self.btn_stop, self.btn_forward, self.btn_return]:
            btn.setFont(QFont('Tahoma', 14))
            btn.setStyleSheet("background-color: #888; color: black; padding: 8px;")
            layout.addWidget(btn)

        self.btn_play.clicked.connect(self.play_video)
        self.btn_pause.clicked.connect(self.pause_video)
        self.btn_stop.clicked.connect(self.stop_video)
        self.btn_forward.clicked.connect(self.forward_video)
        self.btn_return.clicked.connect(self.return_to_main)

        self.central_widget.setLayout(layout)
        self.face_cascade = cv2.CascadeClassifier('C:/repo final/ProyectoFaceDetectionVideo/haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier('C:/repo final/ProyectoFaceDetectionVideo/haarcascade_eye.xml')
        self.data_path = 'C:/repo final/ProyectoFaceDetectionVideo/Data/Jose'

    def play_video(self):
        self.player.play()

    def clean_up(self, folder_path):
        for file in glob.glob(f"{folder_path}/*paused_frame*.jpg"):
            if 'rostro' not in file:
                os.remove(file)


    def pause_video(self):
        now = datetime.now()
        date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
        folder_path = os.path.join(self.data_path, date_string)
        os.makedirs(folder_path, exist_ok=True)
        self.player.pause()
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.video_widget.winId())
        path = os.path.join(folder_path, f"paused_frame_{date_string}.jpg")
        screenshot.save(path, "jpg")
        self.process_faces(path, folder_path, date_string)
        self.clean_up(folder_path)
        self.menu_caras = MenuCaras(folder_path) 

    def process_faces(self, path, folder_path, date_string):
        frame = cv2.imread(path)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        for count, (x, y, w, h) in enumerate(faces, start=1):
            roi_gray = gray[y:y+h, x:x+w]
            face_filename = os.path.join(folder_path, f"rostro{count}_paused_frame_{date_string}.jpg")
            cv2.imwrite(face_filename, roi_gray)

    
    def stop_video(self):
        self.player.stop()

    def forward_video(self):
        self.player.setPosition(self.player.position() + 10000)

    def return_to_main(self):
        self.close()  # Cierra la ventana actual de VideoPlayer
        self.main_panel.show()  # Muestra la ventana principal

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VideoPlayer("path_to_your_video.mp4")  # Cambia con la ruta a tu video
    sys.exit(app.exec_())
