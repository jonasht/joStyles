from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import (
    QWidget, QApplication,
    QHBoxLayout, QVBoxLayout, QFrame,
    QLabel,
)
import sys
from style import *
from PyQt6.QtCore import Qt

class W_Label(QWidget):
    def __init__(self) -> None:
        super().__init__()
        def fmt_cons(cons):
            return cons
        layout_main = QVBoxLayout()


        # labels 
        layout_label = QHBoxLayout()
        frame_label = QFrame()
        frame_label.setLayout(layout_label)
        
        self.lb_lb = QLabel('Label:')
        self.lb_primary = QLabel(PRIMARY)
        self.lb_secondary = QLabel(SECONDARY)
        self.lb_success = QLabel(SUCCESS)
        self.lb_info = QLabel(INFO)
        self.lb_warning = QLabel(WARNING)
        self.lb_danger = QLabel(DANGER)

        self.lb_primary.setObjectName(PRIMARY)
        self.lb_secondary.setObjectName(SECONDARY)
        self.lb_success.setObjectName(SUCCESS)
        self.lb_info.setObjectName(INFO)
        self.lb_warning.setObjectName(WARNING)
        self.lb_danger.setObjectName(DANGER)

        layout_label.addWidget(self.lb_lb)
        layout_label.addWidget(self.lb_primary)
        layout_label.addWidget(self.lb_secondary)
        layout_label.addWidget(self.lb_success)
        layout_label.addWidget(self.lb_info)
        layout_label.addWidget(self.lb_warning)
        layout_label.addWidget(self.lb_danger)

        # label inverse
        layout_labelInverse = QHBoxLayout()
        frame_labelInverse = QFrame()
        frame_labelInverse.setLayout(layout_labelInverse)

        self.lb_lbInverse = QLabel('Label Inverse:')
        self.lb_primaryInverse = QLabel(PRIMARY_INVERSE)
        self.lb_secondaryInverse = QLabel(PRIMARY_INVERSE)
        self.lb_successInverse = QLabel(SUCCESS_INVERSE)
        self.lb_infoInverse = QLabel(INFO_INVERSE)
        self.lb_warningInverse = QLabel(WARNING_INVERSE)
        self.lb_dangerInverse = QLabel(DANGER_INVERSE)

        self.lb_primaryInverse.setObjectName(PRIMARY_INVERSE)
        self.lb_secondaryInverse.setObjectName(SECONDARY_INVERSE)
        self.lb_successInverse.setObjectName(SUCCESS_INVERSE)
        self.lb_infoInverse.setObjectName(INFO_INVERSE)
        self.lb_warningInverse.setObjectName(WARNING_INVERSE)
        self.lb_dangerInverse.setObjectName(DANGER_INVERSE)

        layout_labelInverse.addWidget(self.lb_lbInverse)
        layout_labelInverse.addWidget(self.lb_primaryInverse)
        layout_labelInverse.addWidget(self.lb_secondaryInverse)
        layout_labelInverse.addWidget(self.lb_successInverse)
        layout_labelInverse.addWidget(self.lb_infoInverse)
        layout_labelInverse.addWidget(self.lb_warningInverse)
        layout_labelInverse.addWidget(self.lb_dangerInverse)

        # label border
        layout_labelBorder = QHBoxLayout()
        frame_labelBorder = QFrame()
        frame_labelBorder.setLayout(layout_labelBorder)
        

        self.lb_lbBorder = QLabel('Label Border:')
        self.lb_primaryBorder = QLabel(PRIMARY_BORDER)
        self.lb_secondaryBorder = QLabel(SECONDARY_BORDER)
        self.lb_successBorder = QLabel(SUCCESS_BORDER)
        self.lb_infoBorder = QLabel(INFO_BORDER)
        self.lb_warningBorder = QLabel(WARNING_BORDER)
        self.lb_dangerBorder = QLabel(DANGER_BORDER)
        
        self.lb_primaryBorder.setObjectName(PRIMARY_BORDER)
        self.lb_secondaryBorder.setObjectName(SECONDARY_BORDER)
        self.lb_successBorder.setObjectName(SUCCESS_BORDER)
        self.lb_infoBorder.setObjectName(INFO_BORDER)
        self.lb_warningBorder.setObjectName(WARNING_BORDER)
        self.lb_dangerBorder.setObjectName(DANGER_BORDER)

        layout_labelBorder.addWidget(self.lb_lbBorder)
        layout_labelBorder.addWidget(self.lb_primaryBorder)
        layout_labelBorder.addWidget(self.lb_secondaryBorder)
        layout_labelBorder.addWidget(self.lb_successBorder)
        layout_labelBorder.addWidget(self.lb_infoBorder)
        layout_labelBorder.addWidget(self.lb_warningBorder)
        layout_labelBorder.addWidget(self.lb_dangerBorder)
        
        layout_main.addWidget(frame_label)
        layout_main.addWidget(frame_labelInverse)
        layout_main.addWidget(frame_labelBorder)

        self.setLayout(layout_main)
        self.setup_alignment()

    def setup_alignment(self) -> None:
        self.lb_lb.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.lb_lbBorder.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.lb_lbInverse.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        if a0.key() == Qt.Key.Key_Escape: #type: ignore
            self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(get_style())

    window = W_Label()
    window.show()
    
    sys.exit(app.exec())