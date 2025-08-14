import sys
from PyQt6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QWidget, QApplication, QFrame,
    QPushButton, QLabel, QLineEdit, QCheckBox,
    
)
from PyQt6.QtCore import Qt
from style import *
from w_label import W_Label
from w_button import W_button
from w_lineEdit import W_LineEdit
from w_checkBox import W_checkBox
from w_radioButton import W_radioButton
from w_frame import W_Frame

class Windows(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()

        
        w_label = W_Label()
        w_button = W_button()    
        w_lineEdit = W_LineEdit()
        w_checkBox = W_checkBox()
        w_radioButton = W_radioButton()
        w_frame = W_Frame()
        
        # colocando Layouts
        layout_main.addWidget(w_label)
        layout_main.addWidget(w_button)
        layout_main.addWidget(w_lineEdit)
        layout_main.addWidget(w_checkBox)
        layout_main.addWidget(w_radioButton)
        layout_main.addWidget(w_frame)

        self.setLayout(layout_main)

    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_Escape: # type: ignore
            self.close()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Windows()
    app.setStyleSheet(get_style())
    window.show()
    sys.exit(app.exec())
