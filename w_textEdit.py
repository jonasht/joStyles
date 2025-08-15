from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import (
    QWidget, QApplication, QHBoxLayout, QVBoxLayout,
    QTextEdit, QLabel, QFrame
)
from PyQt6.QtCore import Qt
from style import *
import sys

class W_textEdit(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()

        
        layout_te = QHBoxLayout()
        frame_te = QFrame()
        frame_te.setLayout(layout_te)

        layout_teFill = QHBoxLayout()
        frame_teFill = QFrame()
        frame_teFill.setLayout(layout_teFill)

        self.lb_te = QLabel('TextEdit:')
        self.te_default = QTextEdit('default')
        self.te_primary = QTextEdit(PRIMARY)
        self.te_secondary = QTextEdit(SECONDARY)
        self.te_success = QTextEdit(SUCCESS)
        self.te_info = QTextEdit(INFO)
        self.te_warning = QTextEdit(WARNING)
        self.te_danger = QTextEdit(DANGER)



        self.te_primary.setObjectName(PRIMARY)
        self.te_secondary.setObjectName(SECONDARY)
        self.te_success.setObjectName(SUCCESS)
        self.te_info.setObjectName(INFO)
        self.te_warning.setObjectName(WARNING)
        self.te_danger.setObjectName(DANGER)
        
        layout_te.addWidget(self.lb_te)
        layout_te.addWidget(self.te_default)
        layout_te.addWidget(self.te_primary)
        layout_te.addWidget(self.te_secondary)
        layout_te.addWidget(self.te_success)
        layout_te.addWidget(self.te_info)
        layout_te.addWidget(self.te_warning)
        layout_te.addWidget(self.te_danger)
        

        # textEdit fill
        self.lb_teFill = QLabel('TextEdit Fill:')
        self.te_primaryFill = QTextEdit(PRIMARY)
        self.te_secondaryFill = QTextEdit(SECONDARY)
        self.te_successFill = QTextEdit(SUCCESS)
        self.te_infoFill = QTextEdit(INFO)
        self.te_warningFill = QTextEdit(WARNING)
        self.te_dangerFill = QTextEdit(DANGER)
        
        layout_teFill.addWidget(self.lb_teFill)
        layout_teFill.addWidget(self.te_primaryFill)
        layout_teFill.addWidget(self.te_secondaryFill)
        layout_teFill.addWidget(self.te_successFill)
        layout_teFill.addWidget(self.te_infoFill)
        layout_teFill.addWidget(self.te_warningFill)
        layout_teFill.addWidget(self.te_dangerFill)
        
        self.te_primaryFill.setObjectName(PRIMARY_FILL)
        self.te_secondaryFill.setObjectName(SECONDARY_FILL)
        self.te_successFill.setObjectName(SUCCESS_FILL)
        self.te_infoFill.setObjectName(INFO_FILL)
        self.te_warningFill.setObjectName(WARNING_FILL)
        self.te_dangerFill.setObjectName(DANGER_FILL)


        layout_main.addWidget(frame_te)
        layout_main.addWidget(frame_teFill)

        self.setLayout(layout_main)

    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        if a0.key() == Qt.Key.Key_Escape: #type: ignore
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = W_textEdit()
    window.show()
    app.setStyleSheet(get_style())
    # window.setGeometry(100, 100, 1000, 800)
    
    sys.exit(app.exec())
