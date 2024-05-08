import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog
from video_player import VideoPlayer


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
