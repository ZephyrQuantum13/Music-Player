from PyQt5.QtCore import Qt, QFile, QTextStream 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout, QMessageBox, QSlider
from PyQt5.QtGui import QFont, QPalette, QColor


class App(QWidget):

    def __init__ (self):    
        super().__init__()
        self.UI()

    def UI(self):

        self.setWindowTitle('Music Player')
        self.resize(500, 400)
        font = QFont("Segoe UI", 10)

       
    # create Widgets 

        self.list_musics = QListWidget()
        self.list_musics_label = QLabel("Music List")
        self.play_button = QPushButton("PLAY")
        self.stop_button = QPushButton("STOP")
        self.add_button = QPushButton("Add")
        self.image_music = QLabel("Music Cover")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)      
        self.slider.setValue(50)       
        self.slider.setTickPosition(QSlider.TicksBelow)  
        self.slider.setTickInterval(10)     
        



# Layouts

        self.LayoutMain = QHBoxLayout()
        self.H1Layout = QHBoxLayout()
        self.V1Layout = QVBoxLayout()
        self.V2Layout = QVBoxLayout()

# 1 vertical layout
        self.V1Layout.addWidget(self.list_musics_label)
        self.V1Layout.addWidget(self.list_musics)
        self.V1Layout.addWidget(self.add_button)

# 1 horisont layout 

        self.H1Layout.addWidget(self.play_button)
        self.H1Layout.addWidget(self.stop_button)

# 2 vertical layout

        self.V2Layout.addWidget(self.image_music)
        self.V2Layout.addWidget(self.slider)
       

        self.V2Layout.addLayout(self.H1Layout)

# Main layout

        self.LayoutMain.addLayout(self.V1Layout)
        self.LayoutMain.addLayout(self.V2Layout)

        self.setLayout(self.LayoutMain)




