import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class VideoPlayer(QMainWindow):
    def __init__(self, video_path):
        super().__init__()
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
        self.player.play()  # Reproducción automática al abrir la ventana

        self.btn_play = QPushButton("Play")
        self.btn_pause = QPushButton("Pause")
        self.btn_stop = QPushButton("Stop")
        self.btn_forward = QPushButton("Adelantar 10s")
        self.btn_process_faces = QPushButton("Procesar rostros")
        self.btn_return = QPushButton("Volver al inicio")

        for btn in [self.btn_play, self.btn_pause, self.btn_stop, self.btn_forward, self.btn_process_faces, self.btn_return]:
            btn.setFont(QFont('Tahoma', 14))
            btn.setStyleSheet("background-color: #888; color: black; padding: 8px;")
            layout.addWidget(btn)

        self.btn_play.clicked.connect(self.play_video)
        self.btn_pause.clicked.connect(self.pause_video)
        self.btn_stop.clicked.connect(self.stop_video)
        self.btn_forward.clicked.connect(self.forward_video)
        self.btn_process_faces.clicked.connect(self.process_faces)
        self.btn_return.clicked.connect(self.return_to_main)

        self.central_widget.setLayout(layout)

    def play_video(self):
        self.player.play()

    def pause_video(self):
        self.player.pause()

    def stop_video(self):
        self.player.stop()

    def forward_video(self):
        self.player.setPosition(self.player.position() + 10000)

    def process_faces(self):
        pass

    def return_to_main(self):
        self.close()


class MainPanel(QWidget):
    """Clase principal que representa el panel de carga de video."""

    def __init__(self):
        """Inicializa la interfaz de usuario del panel."""
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configura tamaño y posición de la ventana
        self.setWindowTitle('Panel Principal - Reproductor de Video')
        self.setGeometry(300, 300, 600, 600)
        self.setStyleSheet("background-color: white;")

        grid_layout = QGridLayout()

        # Configuramos el label del texto
        label_description = QLabel('Inserte el video a reproducir y procesar', self)
        label_description.setFont(QFont('Tahoma', 20))
        label_description.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(label_description, 0, 0, 1, 3)  # Posición (0,0) y se extiende 1 fila y 3 columnas

        # Configuramos el label para la imagen
        label_with_monkey = QLabel(self)
        pixmap = QPixmap('assets/monito.png')
        label_with_monkey.setPixmap(pixmap.scaledToWidth(250))
        label_with_monkey.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(label_with_monkey, 1, 0, 1, 3)  # Debajo del label de descripción

        # Configuramos el botón
        btn_open_file = QPushButton('Abrir archivo', self)
        btn_open_file.clicked.connect(self.openFileDialog)
        # Estilos del botón
        btn_open_file.setStyleSheet("QPushButton {"
                                    "background-color: black;"
                                    "color: white;"
                                    "font-weight: bold;"
                                    "font-size: 16px;"
                                    "height: 40px;"
                                    "}")
        btn_open_file.setFixedSize(200, 40)
        grid_layout.addWidget(btn_open_file, 2, 1)  # Posición centrada en la fila 2

        self.setLayout(grid_layout)  # Establece el layout en el widget principal

    def openFileDialog(self):
        """Abre un diálogo para seleccionar archivos .mp4."""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self,
                                                   "Seleccione un video",
                                                   "",  # Directorio inicial
                                                   "Videos (*.mp4)",  # Filtrar por .mp4
                                                   options=options)
        if file_name:
            self.video_player = VideoPlayer(file_name)  # Pasar la ruta del archivo al constructor
            self.video_player.show()  # Mostrar la ventana de reproductor de video
            self.hide()  # Ocultar el panel principal


# Punto de entrada principal para la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainPanel()
    ex.show()  # Muestra la ventana principal
    sys.exit(app.exec_())  # Comienza el bucle de eventos de la aplicación
