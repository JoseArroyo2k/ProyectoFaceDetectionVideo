import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QFileDialog, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import shutil

class MenuCaras(QWidget):
    def __init__(self, folder_path):
        super().__init__()
        self.folder_path = folder_path
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle('Menú de Rostros Extraídos')
        
        # Listar todos los archivos de imagen en la carpeta
        for filename in os.listdir(self.folder_path):
            if filename.endswith('.jpg'):
                button = QPushButton()
                button.setIcon(QIcon(os.path.join(self.folder_path, filename)))
                button.setIconSize(QPixmap(os.path.join(self.folder_path, filename)).size())
                button.clicked.connect(lambda ch, filename=filename: self.show_options(filename))
                layout.addWidget(button)

        self.setGeometry(300, 300, 350, 300)
        self.show()

    def show_options(self, filename):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Opción de Guardado")
        msg_box.setText("¿Deseas guardar este rostro?")
        save_button = msg_box.addButton("Guardar", QMessageBox.AcceptRole)
        cancel_button = msg_box.addButton(QMessageBox.Cancel)
        msg_box.exec_()

        if msg_box.clickedButton() == save_button:
            self.save_photo(filename)

    def save_photo(self, filename):
        destination_folder = 'C:/repo final/ProyectoFaceDetectionVideo/Rostros Guardados'
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        source_path = os.path.join(self.folder_path, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.copy(source_path, destination_path)
        QMessageBox.information(self, "Foto Guardada", f"El rostro ha sido guardado en: {destination_path}")
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MenuCaras('path_to_your_folder')  # Reemplaza con la ruta de la carpeta generada al pausar
    sys.exit(app.exec_())
