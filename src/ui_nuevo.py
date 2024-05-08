from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)  # Tamaño más grande para más controles
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)

        # Label para mostrar el video
        self.videoLabel = QtWidgets.QLabel("Video no cargado")
        self.videoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.videoLabel, 0, 0, 1, 2)  # Expandir a dos columnas

        # Botones de control
        self.playButton = QtWidgets.QPushButton("Play")
        self.gridLayout.addWidget(self.playButton, 1, 0)

        self.pauseButton = QtWidgets.QPushButton("Pause")
        self.gridLayout.addWidget(self.pauseButton, 1, 1)

        self.stopButton = QtWidgets.QPushButton("Stop")
        self.gridLayout.addWidget(self.stopButton, 2, 0)

        self.advanceButton = QtWidgets.QPushButton("Adelantar 10s")
        self.gridLayout.addWidget(self.advanceButton, 2, 1)

        # Estado del video
        self.statusLabel = QtWidgets.QLabel("Estado del video")
        self.gridLayout.addWidget(self.statusLabel, 3, 0, 1, 2)  # Expandir a dos columnas

        # Conectar eventos
        self.playButton.clicked.connect(self.play_video)
        self.pauseButton.clicked.connect(self.pause_video)
        self.stopButton.clicked.connect(self.stop_video)
        self.advanceButton.clicked.connect(self.advance_video)

    def play_video(self):
        # Lógica para reproducir el video
        pass

    def pause_video(self):
        # Lógica para pausar el video
        pass

    def stop_video(self):
        # Lógica para detener el video
        pass

    def advance_video(self):
        # Lógica para avanzar el video 10 segundos
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
