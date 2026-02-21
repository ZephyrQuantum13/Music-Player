import sys
from PyQt5.QtCore import Qt, QFile, QTextStream 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout, QMessageBox
from PyQt5.QtGui import QFont, QPalette, QColor
from app import App

if __name__ == '__main__':
    app = QApplication(sys.argv)

    file = QFile("styles/black_theme.qss")  
    if file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(file)
        stream.setCodec("UTF-8")  
        app.setStyleSheet(stream.readAll())
        file.close()
   
    player = App()
    player.show()
    sys.exit(app.exec_())