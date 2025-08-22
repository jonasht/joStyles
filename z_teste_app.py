from PyQt6.QtWidgets import (
    QWidget, QApplication, QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QLineEdit,
)
import sys
from style import *
from z_jstyle import *


class W_Teste(QWidget):
    def __init__(self) -> None:
        super().__init__()
        lay_main = QVBoxLayout()
        lay_1 = QHBoxLayout()
        lay_2 = QHBoxLayout()

        self.lb_ = QLabel('botao:')
        self.le_ = QLineEdit()
        self.bt_ = QPushButton('botao')
        lb_ = QLabel('botao:')
        le_ = QLineEdit()
        bt_ = QPushButton('botao')

        lay_1.addWidget(self.lb_)
        lay_1.addWidget(self.le_)
        lay_1.addWidget(self.bt_) 
        lay_2.addWidget(lb_)
        lay_2.addWidget(le_)
        lay_2.addWidget(bt_) 

        self.bt_.setObjectName(SUCCESS)       
        self.le_.setObjectName(SUCCESS)
        
        lay_main.addLayout(lay_1)
        lay_main.addLayout(lay_2)
        
        self.setLayout(lay_main)

        print('tipo self lb:', self.lb_.__class__.__name__)
        print('self le', self.le_.__class__.__name__)
        print('self bt', self.bt_.__class__.__name__)
        print()
        print('lb', lb_.__class__.__name__)
        print('le', le_.__class__.__name__)
        print('bt', bt_.__class__.__name__)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    app.setStyleSheet(get_style())
    window = W_Teste()
    window.show()
    window.setGeometry(100, 100, 800, 800)

    sys.exit(app.exec())
    
        
