import sys
from PyQt5.QtCore import Qt, QFile, QTextStream 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout, QMessageBox
from PyQt5.QtGui import QFont, QPalette, QColor
from app import App

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = App()
    player.show()
    sys.exit(app.exec_())