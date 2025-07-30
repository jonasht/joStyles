from PyQt6.QtWidgets import (
    QWidget, QApplication,
    QHBoxLayout, QVBoxLayout, QFrame,
    QLabel,
)
import sys
from style import *

class W_Label(QWidget):
    def __init__(self) -> None:
        super().__init__()
        def fmt_cons(cons):
            return (cons.upper()).replace('-', '_')

        layout_main = QVBoxLayout()


        # labels 
        layout_label = QHBoxLayout()
        frame_label = QFrame()
        frame_label.setLayout(layout_label)
        
        self.lb_lb = QLabel('Label:')
        self.lb_primary = QLabel(PRIMARY.upper())
        self.lb_secondary = QLabel(SECONDARY.upper())
        self.lb_success = QLabel(SUCCESS.upper())
        self.lb_info = QLabel(INFO.upper())
        self.lb_warning = QLabel(WARNING.upper())
        self.lb_danger = QLabel(DANGER.upper())

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

        self.lb_lbInverse = QLabel('LabelInverse:')
        self.lb_primaryInverse = QLabel(fmt_cons(PRIMARY_INVERSE))
        self.lb_secondaryInverse = QLabel(fmt_cons(PRIMARY_INVERSE))
        self.lb_successInverse = QLabel(fmt_cons(SUCCESS_INVERSE))
        self.lb_infoInverse = QLabel(fmt_cons(INFO_INVERSE))
        self.lb_warningInverse = QLabel(fmt_cons(WARNING_INVERSE))
        self.lb_dangerInverse = QLabel(fmt_cons(DANGER_INVERSE))

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
        self.lb_primaryBorder = QLabel(fmt_cons(PRIMARY_BORDER))
        self.lb_secondaryBorder = QLabel(fmt_cons(SECONDARY_BORDER))
        self.lb_successBorder = QLabel(fmt_cons(SUCCESS_BORDER))
        self.lb_infoBorder = QLabel(fmt_cons(INFO_BORDER))
        self.lb_warningBorder = QLabel(fmt_cons(WARNING_BORDER))
        self.lb_dangerBorder = QLabel(fmt_cons(DANGER_BORDER))
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(load_style())

    window = W_Label()
    window.show()
    
    sys.exit(app.exec())