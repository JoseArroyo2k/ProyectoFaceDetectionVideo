import sys
from PyQt5.QtWidgets import QApplication
from main_panel import MainPanel

def main():
    app = QApplication(sys.argv)  
    main_panel = MainPanel()      
    main_panel.show()             
    sys.exit(app.exec_())         

if __name__ == "__main__":
    main()
