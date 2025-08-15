import sys
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QFrame, QApplication,
    QLabel, QWidget, QCheckBox
)
from style import *
from PyQt6.QtCore import Qt

class W_checkBox(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()

        # QCheckBox
        layout_cb = QHBoxLayout()
        layout_cbBorder = QHBoxLayout()

        frame_cb = QFrame()
        frame_cbBorder = QFrame()
        frame_cb.setLayout(layout_cb)
        frame_cbBorder.setLayout(layout_cbBorder)
        
        # checkbox normal
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
        
        
        layout_cb.addWidget(self.lb_cb)
        layout_cb.addWidget(self.cb_primary)
        layout_cb.addWidget(self.cb_secondary)
        layout_cb.addWidget(self.cb_success)
        layout_cb.addWidget(self.cb_info)
        layout_cb.addWidget(self.cb_warning)
        layout_cb.addWidget(self.cb_danger)
        
        # checkBox border
        self.lb_cbBorder = QLabel('CheckBox Border:')
        self.cb_primaryBorder = QCheckBox(PRIMARY_BORDER)
        self.cb_secondaryBorder = QCheckBox(SECONDARY_BORDER)
        self.cb_successBorder = QCheckBox(SUCCESS_BORDER)
        self.cb_infoBorder = QCheckBox(INFO_BORDER)
        self.cb_warningBorder = QCheckBox(WARNING_BORDER)
        self.cb_dangerBorder = QCheckBox(DANGER_BORDER)

        self.cb_primaryBorder.setObjectName(PRIMARY_BORDER)
        self.cb_secondaryBorder.setObjectName(SECONDARY_BORDER)
        self.cb_successBorder.setObjectName(SUCCESS_BORDER)
        self.cb_infoBorder.setObjectName(INFO_BORDER)
        self.cb_warningBorder.setObjectName(WARNING_BORDER)
        self.cb_dangerBorder.setObjectName(DANGER_BORDER)
        
        
        layout_cbBorder.addWidget(self.lb_cbBorder)
        layout_cbBorder.addWidget(self.cb_primaryBorder)
        layout_cbBorder.addWidget(self.cb_secondaryBorder)
        layout_cbBorder.addWidget(self.cb_successBorder)
        layout_cbBorder.addWidget(self.cb_infoBorder)
        layout_cbBorder.addWidget(self.cb_warningBorder)
        layout_cbBorder.addWidget(self.cb_dangerBorder)
        
        layout_main.addWidget(frame_cb)
        layout_main.addWidget(frame_cbBorder)
        self.setLayout(layout_main)
    
        self.set_checkAll()
        
    def set_checkAll(self):
        self.cb_primary.setChecked(True)
        self.cb_secondary.setChecked(True)
        self.cb_success.setChecked(True)
        self.cb_info.setChecked(True)
        self.cb_warning.setChecked(True)
        self.cb_danger.setChecked(True)
        
    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        if a0.key() == Qt.Key.Key_Escape: #type: ignore 
            self.close()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = W_checkBox()
    app.setStyleSheet(get_style())

    window.show()

    sys.exit(app.exec())

