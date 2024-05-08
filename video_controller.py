import os
import threading
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import cv2
from opencv_engine import opencv_engine

class video_controller(QObject):
    def __init__(self, video_path, ui):
        
        super().__init__()
        self.video_path = video_path
        self.ui = ui
        self.qpixmap_fix_width = 800
        self.qpixmap_fix_height = 450
        self.current_frame_no = 0
        self.videoplayer_state = "stop"
        self.face_count = 0
        self.face_cascade = cv2.CascadeClassifier('C:/Repo Proyecto 4/haarcascade_frontalface_default.xml') 
        self.eye_cascade = cv2.CascadeClassifier('C:/Repo Proyecto 4/haarcascade_eye.xml') 
        self.init_video_info()
        self.set_video_player()
        self.person_name = 'Jose' 
        self.data_path = 'C:/Repo Proyecto 4/Data/Jose' 

        self.paused_frame_count = 0
        self.pause_start_frame = 0
        self.stop_processing = False

    def init_video_info(self):
        videoinfo = opencv_engine.getvideoinfo(self.video_path)
        self.vc = videoinfo["vc"] 
        self.video_fps = videoinfo["fps"] 
        self.video_total_frame_count = videoinfo["frame_count"] 
        self.video_width = videoinfo["width"]
        self.video_height = videoinfo["height"]

    def set_video_player(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_timeout_job)
        self.timer.start(1)

    def __get_frame_from_frame_no(self, frame_no):
        self.vc.set(1, frame_no)
        ret, frame = self.vc.read()
        self.ui.label_framecnt.setText(f"frame number: {frame_no}/{self.video_total_frame_count}")
        return frame

    def __update_label_frame(self, frame):       
        bytesPerline = 3 * self.video_width
        qimg = QImage(frame, self.video_width, self.video_height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(qimg)

        if self.qpixmap.width()/16 >= self.qpixmap.height()/9:
            self.qpixmap = self.qpixmap.scaledToWidth(self.qpixmap_fix_width)
        else:
            self.qpixmap = self.qpixmap.scaledToHeight(self.qpixmap_fix_height)
        self.ui.label_videoframe.setPixmap(self.qpixmap)
        self.ui.label_videoframe.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def play(self):
        self.videoplayer_state = "play"

    def stop(self):
        self.videoplayer_state = "stop"

    def pause(self):
        if self.videoplayer_state == "play":
            self.pause_start_frame = self.current_frame_no
            self.videoplayer_state = "pause"
            self.timer.stop()
            self.capture_faces(self.current_frame_no, self.current_frame_no + 1)
        elif self.videoplayer_state == "pause":
            print("ingreso aqui")

    def timer_timeout_job(self):
        frame = self.__get_frame_from_frame_no(self.current_frame_no)
        self.__update_label_frame(frame)

        if self.videoplayer_state == "play":
            self.current_frame_no += 1

            if self.current_frame_no >= self.video_total_frame_count:
                self.stop()

        elif self.videoplayer_state == "pause":
            if self.current_frame_no < self.video_total_frame_count:
                self.capture_faces(self.pause_start_frame, self.current_frame_no)

    def capture_faces(self, start_frame, end_frame):
        cap = cv2.VideoCapture(self.video_path)

        if not cap.isOpened():
            print("Error: No se pudo abrir el archivo de video.")
            return -1

        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        face_count = 0  

        while cap.get(cv2.CAP_PROP_POS_FRAMES) < end_frame:
            ret, img = cap.read()

            if not ret:
                print("Error al leer el fotograma.")
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                cv2.imwrite(f"{self.data_path}/face_{self.current_frame_no}_{face_count}.jpg", roi_gray)
                face_count += 1

        cap.release()

    def procesar_rostro(self):
        def procesar_rostro_thread():
            cap = cv2.VideoCapture(self.video_path)

            if not cap.isOpened():
                print("Error: No se pudo abrir el archivo de video.")
                return -1

            while not self.stop_processing:  # Continuar procesando mientras la variable de estado sea False
                ret, img = cap.read()

                if not ret:
                    print("Fin del video.")
                    break

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = img[y:y+h, x:x+w]

                    eyes = self.eye_cascade.detectMultiScale(roi_gray)

                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 127, 255), 2)

                qimg = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888).rgbSwapped()
                qpixmap = QPixmap.fromImage(qimg)
                qpixmap = qpixmap.scaledToWidth(self.qpixmap_fix_width)
                self.ui.label_videoframe.setPixmap(qpixmap)
                self.ui.label_videoframe.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            cap.release()
            cv2.destroyAllWindows()

        thread = threading.Thread(target=procesar_rostro_thread)
        thread.start()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    video_controller_instance = video_controller('video_path', ui)
    MainWindow.show()
    sys.exit(app.exec())
