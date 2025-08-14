import sys
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import (
    QWidget, QApplication,
    QVBoxLayout, QHBoxLayout, QFrame,
    QLabel, QPushButton, QCheckBox,
)
from style import *
from PyQt6.QtCore import Qt

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
        self.cb_bt = QCheckBox('Disable Buttons')
        
        self.bt_primary.setObjectName(PRIMARY)
        self.bt_secondary.setObjectName(SECONDARY)
        self.bt_success.setObjectName(SUCCESS)
        self.bt_info.setObjectName(INFO)
        self.bt_warning.setObjectName(WARNING)
        self.bt_danger.setObjectName(DANGER)
        self.bt_link.setObjectName(LINK)
        self.cb_bt.setObjectName(INFO)

        layout_bt.addWidget(self.lb_bt)
        layout_bt.addWidget(self.bt_primary)
        layout_bt.addWidget(self.bt_secondary)
        layout_bt.addWidget(self.bt_success)
        layout_bt.addWidget(self.bt_info)
        layout_bt.addWidget(self.bt_warning)
        layout_bt.addWidget(self.bt_danger)
        layout_bt.addWidget(self.bt_link)
        layout_bt.addWidget(self.cb_bt)
        
        self.cb_bt.stateChanged.connect(self.disabled_bts)

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

        self.cb_btOutline = QCheckBox('Disable Buttons')
        
        self.bt_primaryOutline.setObjectName(PRIMARY_OUTLINE)
        self.bt_secondaryOutline.setObjectName(SECONDARY_OUTLINE)
        self.bt_successOutline.setObjectName(SUCCESS_OUTLINE)
        self.bt_infoOutline.setObjectName(INFO_OUTLINE)
        self.bt_warningOutline.setObjectName(WARNING_OUTLINE)
        self.bt_dangerOutline.setObjectName(DANGER_OUTLINE)

        self.cb_btOutline.setObjectName(INFO)

        layout_btOutline.addWidget(self.lb_btOutline)
        layout_btOutline.addWidget(self.bt_primaryOutline)
        layout_btOutline.addWidget(self.bt_secondaryOutline)
        layout_btOutline.addWidget(self.bt_successOutline)
        layout_btOutline.addWidget(self.bt_infoOutline)
        layout_btOutline.addWidget(self.bt_warningOutline)
        layout_btOutline.addWidget(self.bt_dangerOutline)
        layout_btOutline.addWidget(self.cb_btOutline)
        
        self.cb_btOutline.clicked.connect(self.disabled_btsOutline)
        # QButton Link ---------------------------------------------
        layout_btLink = QHBoxLayout() 
        frame_btLink = QFrame()
        frame_btLink.setLayout(layout_btLink)

        self.lb_btLink = QLabel('QpushButton Link:')
        self.bt_primaryLink = QPushButton(PRIMARY_LINK)
        self.bt_secondaryLink = QPushButton(SECONDARY_LINK)
        self.bt_successLink = QPushButton(SUCCESS_LINK)
        self.bt_infoLink = QPushButton(INFO_LINK)
        self.bt_warningLink = QPushButton(WARNING_LINK)
        self.bt_dangerLink = QPushButton(DANGER_LINK)
        self.cb_btlink = QCheckBox('Disabled Buttons')

        self.bt_primaryLink.setObjectName(PRIMARY_LINK)
        self.bt_secondaryLink.setObjectName(SECONDARY_LINK)
        self.bt_successLink.setObjectName(SUCCESS_LINK)
        self.bt_infoLink.setObjectName(INFO_LINK)
        self.bt_warningLink.setObjectName(WARNING_LINK)
        self.bt_dangerLink.setObjectName(DANGER_LINK)
        self.cb_btlink.setObjectName(INFO)

        layout_btLink.addWidget(self.lb_btLink)
        layout_btLink.addWidget(self.bt_primaryLink)
        layout_btLink.addWidget(self.bt_secondaryLink)
        layout_btLink.addWidget(self.bt_successLink)
        layout_btLink.addWidget(self.bt_infoLink)
        layout_btLink.addWidget(self.bt_warningLink)
        layout_btLink.addWidget(self.bt_dangerLink)
        layout_btLink.addWidget(self.cb_btlink)
        
        self.cb_btlink.clicked.connect(self.disabled_btLink)
        
        layout_main.addWidget(frame_bt)
        layout_main.addWidget(frame_btOutline)
        layout_main.addWidget(frame_btLink)

        self.setLayout(layout_main)
        # self.bt_danger.setEnabled(False)

        # self.disabled_btsOutline(True)
    
    def disabled_btLink(self, state):
        var = not bool(state)
        print('var btsOutline:', var, state)
        
        self.bt_primaryLink.setEnabled(var)
        self.bt_secondaryLink.setEnabled(var)
        self.bt_successLink.setEnabled(var)
        self.bt_infoLink.setEnabled(var)
        self.bt_warningLink.setEnabled(var)
        self.bt_dangerLink.setEnabled(var)

    def disabled_btsOutline(self, state):
        var = not bool(state)
        print('var btsOutline:', var, state)
        
        self.bt_primaryOutline.setEnabled(var)
        self.bt_secondaryOutline.setEnabled(var)
        self.bt_successOutline.setEnabled(var)
        self.bt_infoOutline.setEnabled(var)
        self.bt_warningOutline.setEnabled(var)
        self.bt_dangerOutline.setEnabled(var)

    
    def disabled_bts(self, state):
        var = not bool(state)    
        print('var bts:', var, state)
        
        self.bt_primary.setEnabled(var)
        self.bt_secondary.setEnabled(var)
        self.bt_success.setEnabled(var)
        self.bt_info.setEnabled(var)
        self.bt_warning.setEnabled(var)
        self.bt_danger.setEnabled(var)
        self.bt_link.setEnabled(var)
    
        
    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        if a0.key() == Qt.Key.Key_Escape:
            self.close()
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(get_style())
    window = W_button()
    window.show()

    sys.exit(app.exec())