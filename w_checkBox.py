import sys
from PyQt6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QFrame, QApplication,
    QLabel, QWidget, QCheckBox
)
from style import *

class W_checkBox(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()

        # QCheckBox
        layout_cb = QHBoxLayout()
        frame_cb = QFrame()
        frame_cb.setLayout(layout_cb)
        
        self.lb_cb = QLabel('CheckBox:')
        self.cb_primary = QCheckBox(PRIMARY)
        self.cb_secondary = QCheckBox(SECONDARY)
        self.cb_success = QCheckBox(SUCCESS)
        self.cb_info = QCheckBox(INFO)
        self.cb_warning = QCheckBox(WARNING)
        self.cb_danger = QCheckBox(DANGER)

        self.cb_primary.setObjectName(PRIMARY)
        self.cb_secondary.setObjectName(SECONDARY)
        self.cb_success.setObjectName(SUCCESS)
        self.cb_info.setObjectName(INFO)
        self.cb_warning.setObjectName(WARNING)
        self.cb_danger.setObjectName(DANGER)
        
        self.cb_primary.setChecked(True)
        self.cb_secondary.setChecked(True)
        self.cb_success.setChecked(True)
        self.cb_info.setChecked(True)
        self.cb_warning.setChecked(True)
        self.cb_danger.setChecked(True)
        
        layout_cb.addWidget(self.lb_cb)
        layout_cb.addWidget(self.cb_primary)
        layout_cb.addWidget(self.cb_secondary)
        layout_cb.addWidget(self.cb_success)
        layout_cb.addWidget(self.cb_info)
        layout_cb.addWidget(self.cb_warning)
        layout_cb.addWidget(self.cb_danger)
        
        layout_main.addWidget(frame_cb)
        self.setLayout(layout_main)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = W_checkBox()
    app.setStyleSheet(load_style())

    window.show()

    sys.exit(app.exec())

