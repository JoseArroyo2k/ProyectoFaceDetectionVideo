import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reproductor de Video con Detección de Rostros")
        self.setGeometry(100, 100, 800, 600)  # X, Y, width, height

        # Contenedor central para los widgets
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Layout para los botones
        layout = QVBoxLayout()

        # Botones
        self.btn_play = QPushButton("Play", self)
        self.btn_pause = QPushButton("Pause", self)
        self.btn_stop = QPushButton("Stop", self)
        self.btn_advance = QPushButton("Adelantar", self)

        # Añadir botones al layout
        layout.addWidget(self.btn_play)
        layout.addWidget(self.btn_pause)
        layout.addWidget(self.btn_stop)
        layout.addWidget(self.btn_advance)

        # Establecer el layout en el widget central
        self.central_widget.setLayout(layout)

        # Conexiones de los botones
        self.btn_play.clicked.connect(self.play_video)
        self.btn_pause.clicked.connect(self.pause_video)
        self.btn_stop.clicked.connect(self.stop_video)
        self.btn_advance.clicked.connect(self.advance_video)

    def play_video(self):
        print("Reproduciendo video")

    def pause_video(self):
        print("Video pausado")

    def stop_video(self):
        print("Video detenido")

    def advance_video(self):
        print("Adelantando video")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
