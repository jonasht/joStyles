import sys
from PyQt6.QtWidgets import (
    QWidget, QApplication,
    QVBoxLayout, QHBoxLayout, QFrame,
    QLabel, QPushButton
)
from style import *


class W_button(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout_main = QVBoxLayout()

        
        # QpushButton ---------------------------------------------
        layout_bt = QHBoxLayout()
        frame_bt = QFrame()
        frame_bt.setLayout(layout_bt)

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

        # QPushButton Outline ----------------------------------------
        layout_btOutline = QHBoxLayout()
        frame_btOutline = QFrame()
        frame_btOutline.setLayout(layout_btOutline)

        self.lb_btOutline = QLabel('QpushButton outline:')
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
        
        # QButton Link ---------------------------------------------
        layout_btLink = QHBoxLayout() 
        frame_btLink = QFrame()
        frame_btLink.setLayout(layout_btLink)

        self.lb_bt = QLabel('QpushButton Link:')
        self.bt_primaryLink = QPushButton(PRIMARY_LINK)
        self.bt_secondaryLink = QPushButton(SECONDARY_LINK)
        self.bt_successLink = QPushButton(SUCCESS_LINK)
        self.bt_infoLink = QPushButton(INFO_LINK)
        self.bt_warningLink = QPushButton(WARNING_LINK)
        self.bt_dangerLink = QPushButton(DANGER_LINK)

        self.bt_primaryLink.setObjectName(PRIMARY_LINK)
        self.bt_secondaryLink.setObjectName(SECONDARY_LINK)
        self.bt_successLink.setObjectName(SUCCESS_LINK)
        self.bt_infoLink.setObjectName(INFO_LINK)
        self.bt_warningLink.setObjectName(WARNING_LINK)
        self.bt_dangerLink.setObjectName(DANGER_LINK)
        
        layout_btLink.addWidget(self.lb_bt)
        layout_btLink.addWidget(self.bt_primaryLink)
        layout_btLink.addWidget(self.bt_secondaryLink)
        layout_btLink.addWidget(self.bt_successLink)
        layout_btLink.addWidget(self.bt_infoLink)
        layout_btLink.addWidget(self.bt_warningLink)
        layout_btLink.addWidget(self.bt_dangerLink)
        
        
        layout_main.addWidget(frame_bt)
        layout_main.addWidget(frame_btOutline)
        layout_main.addWidget(frame_btLink)

        self.setLayout(layout_main)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(load_style())
    window = W_button()
    window.show()

    sys.exit(app.exec())