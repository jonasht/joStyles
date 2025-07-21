import sys
from PyQt6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QWidget, QApplication, QFrame,
    QPushButton, QLabel, QLineEdit, QCheckBox,
    
)
from PyQt6.QtCore import Qt
from style import *


class Windows(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()

        # labels 
        layout_label = QHBoxLayout()
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
        self.lb_lbInverse = QLabel('LabelInverse:')
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
        
        # QpushButton
        layout_bt = QHBoxLayout()
        self.lb_bt = QLabel('QpushButton:')
        self.bt_primary = QPushButton(PRIMARY)
        self.bt_secondary = QPushButton(SECONDARY)
        self.bt_success = QPushButton(SUCCESS)
        self.bt_info = QPushButton(INFO)
        self.bt_warning = QPushButton(WARNING)
        self.bt_danger = QPushButton(DANGER)
        self.bt_link = QPushButton(LINK)
        self.bt_primary.setObjectName(PRIMARY)
        self.bt_secondary.setObjectName(SECONDARY)
        self.bt_success.setObjectName(SUCCESS)
        self.bt_info.setObjectName(INFO)
        self.bt_warning.setObjectName(WARNING)
        self.bt_danger.setObjectName(DANGER)
        self.bt_link.setObjectName(LINK)
        
        layout_bt.addWidget(self.lb_bt)
        layout_bt.addWidget(self.bt_primary)
        layout_bt.addWidget(self.bt_secondary)
        layout_bt.addWidget(self.bt_success)
        layout_bt.addWidget(self.bt_info)
        layout_bt.addWidget(self.bt_warning)
        layout_bt.addWidget(self.bt_danger)
        layout_bt.addWidget(self.bt_link)

        # QPushButton Outline
        layout_btOutline = QHBoxLayout()
        self.lb_btOutline = QLabel('buttonOutline:')
        self.bt_primaryOutline = QPushButton(PRIMARY_OUTLINE)
        self.bt_secondaryOutline = QPushButton(SECONDARY_OUTLINE)
        self.bt_successOutline = QPushButton(SUCCESS_OUTLINE)
        self.bt_infoOutline = QPushButton(INFO_OUTLINE)
        self.bt_warningOutline = QPushButton(WARNING_OUTLINE)
        self.bt_dangerOutline = QPushButton(DANGER_OUTLINE)

        self.bt_primaryOutline.setObjectName(PRIMARY_OUTLINE)
        self.bt_secondaryOutline.setObjectName(SECONDARY_OUTLINE)
        self.bt_successOutline.setObjectName(SUCCESS_OUTLINE)
        self.bt_infoOutline.setObjectName(INFO_OUTLINE)
        self.bt_warningOutline.setObjectName(WARNING_OUTLINE)
        self.bt_dangerOutline.setObjectName(DANGER_OUTLINE)

        layout_btOutline.addWidget(self.lb_btOutline)
        layout_btOutline.addWidget(self.bt_primaryOutline)
        layout_btOutline.addWidget(self.bt_secondaryOutline)
        layout_btOutline.addWidget(self.bt_successOutline)
        layout_btOutline.addWidget(self.bt_infoOutline)
        layout_btOutline.addWidget(self.bt_warningOutline)
        layout_btOutline.addWidget(self.bt_dangerOutline)
        

        
        # QCheckBox
        layout_cb = QHBoxLayout()
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

        layout_main.addLayout(layout_btOutline)
        layout_main.addLayout(layout_label)
        layout_main.addLayout(layout_labelInverse)
        layout_main.addLayout(layout_labelBorder)
        layout_main.addLayout(layout_bt)
        layout_main.addLayout(layout_cb)
        self.setLayout(layout_main)

    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_Escape: # type: ignore
            self.close()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Windows()
    app.setStyleSheet(load_style())
    window.show()
    sys.exit(app.exec())
