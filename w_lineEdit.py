from PyQt6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QLineEdit, QFrame
)
import sys
from style import *

class W_editLine(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout_main = QVBoxLayout()

        # QlineEdit 
        layout_le = QHBoxLayout()
        frame_le = QFrame()
        frame_le.setLayout(layout_le)
        self.lb_le = QLabel('QLineEdit:')
        self.le_primary = QLineEdit()
        self.le_secondary = QLineEdit()
        self.le_success = QLineEdit()
        self.le_info = QLineEdit()
        self.le_warning = QLineEdit()
        self.le_danger = QLineEdit()
        self.le_primary.setPlaceholderText(PRIMARY)
        self.le_secondary.setPlaceholderText(SECONDARY)
        self.le_success.setPlaceholderText(SUCCESS)
        self.le_info.setPlaceholderText(INFO)
        self.le_warning.setPlaceholderText(WARNING)
        self.le_danger.setPlaceholderText(DANGER)

        self.le_primary.setObjectName(PRIMARY)
        self.le_secondary.setObjectName(SECONDARY)
        self.le_success.setObjectName(SUCCESS)
        self.le_info.setObjectName(INFO)
        self.le_warning.setObjectName(WARNING)
        self.le_danger.setObjectName(DANGER)

        layout_le.addWidget(self.lb_le)
        layout_le.addWidget(self.le_primary)
        layout_le.addWidget(self.le_secondary)
        layout_le.addWidget(self.le_success)
        layout_le.addWidget(self.le_info)
        layout_le.addWidget(self.le_warning)
        layout_le.addWidget(self.le_danger)
        
        
        layout_main.addWidget(frame_le)
        self.setLayout(layout_main)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = W_editLine()
    window.setStyleSheet(load_style())
    window.setGeometry(800, 800, 800, 500)

    window.show()
    sys.exit(app.exec())