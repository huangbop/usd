import os
import sys
    
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)
import usd
from usd.views.titles import BaseTitle

        



class MainForm(QMainWindow):
    """
    """
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.FramelessWindowHint)

        # Background
        self.bg = QWidget(self)
        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.bg)
        self.setCentralWidget(self.bg)
                
        self.title = BaseTitle(self)
        self.title.setFixedHeight(128)
        
        self.content = QPushButton('jfjsjff', self.bg)
                

        bg_vlayout = QVBoxLayout(self.bg)
        bg_vlayout.addWidget(self.title)
        bg_vlayout.addStretch()
        bg_vlayout.addWidget(self.content)        

        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.resize(800, 600)
    form.setWindowTitle('SSD Uart Diag Tool')
    form.show()
    sys.exit(app.exec_())

