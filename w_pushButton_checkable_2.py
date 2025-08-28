import sys
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame, QApplication, QButtonGroup,
    QPushButton, QLabel, QLineEdit, QStackedWidget,
)
from PyQt6.QtCore import Qt
from style import *

class W_pushButtonChecableExclusive(QWidget):
    def __init__(self):
        super().__init__()


        layout = QVBoxLayout(self)
        
        layout_middle = QHBoxLayout()
        layout_left = QHBoxLayout()
        layout_center = QVBoxLayout()
        layout_right = QVBoxLayout()
        layout_bottom = QHBoxLayout()


        layout_bt = QVBoxLayout()
        fr_bt = QFrame()
        fr_bt.setLayout(layout_bt)


        self.bt_primary = QPushButton(PRIMARY)
        self.bt_secondary = QPushButton(SECONDARY)
        self.bt_success = QPushButton(SUCCESS)
        self.bt_info = QPushButton(INFO)
        self.bt_warning = QPushButton(WARNING)
        self.bt_danger = QPushButton(DANGER)

        self.bt_primary.setCheckable(True)
        self.bt_secondary.setCheckable(True)
        self.bt_success.setCheckable(True)
        self.bt_info.setCheckable(True)
        self.bt_warning.setCheckable(True)
        self.bt_danger.setCheckable(True)
        
        self.group_bt = QButtonGroup()
        self.group_bt.setExclusive(True)
        self.group_bt.addButton(self.bt_primary)
        self.group_bt.addButton(self.bt_secondary)
        self.group_bt.addButton(self.bt_success)
        self.group_bt.addButton(self.bt_info)
        self.group_bt.addButton(self.bt_warning)
        self.group_bt.addButton(self.bt_danger)
        
        layout_bt.addWidget(self.bt_primary)
        layout_bt.addWidget(self.bt_secondary)
        layout_bt.addWidget(self.bt_success)
        layout_bt.addWidget(self.bt_info)
        layout_bt.addWidget(self.bt_warning)
        layout_bt.addWidget(self.bt_danger)

        # QPushButton Outline ---------------------------------------
        layout_btOutline = QVBoxLayout()
        fr_btOutline = QFrame()
        fr_btOutline.setLayout(layout_btOutline)

        self.bt_primaryOutline = QPushButton(PRIMARY_OUTLINE)
        self.bt_secondaryOutline = QPushButton(SECONDARY_OUTLINE)
        self.bt_successOutline = QPushButton(SUCCESS_OUTLINE)
        self.bt_infoOutline = QPushButton(INFO_OUTLINE)
        self.bt_warningOutline = QPushButton(WARNING_OUTLINE)
        self.bt_dangerOutline = QPushButton(DANGER_OUTLINE)

        self.bt_primaryOutline.setCheckable(True)
        self.bt_secondaryOutline.setCheckable(True)
        self.bt_successOutline.setCheckable(True)
        self.bt_infoOutline.setCheckable(True)
        self.bt_warningOutline.setCheckable(True)
        self.bt_dangerOutline.setCheckable(True)

        self.group_bt.addButton(self.bt_primaryOutline)
        self.group_bt.addButton(self.bt_secondaryOutline)
        self.group_bt.addButton(self.bt_successOutline)
        self.group_bt.addButton(self.bt_infoOutline)
        self.group_bt.addButton(self.bt_warningOutline)
        self.group_bt.addButton(self.bt_dangerOutline)

        layout_btOutline.addWidget(self.bt_primaryOutline)
        layout_btOutline.addWidget(self.bt_secondaryOutline)
        layout_btOutline.addWidget(self.bt_successOutline)
        layout_btOutline.addWidget(self.bt_infoOutline)
        layout_btOutline.addWidget(self.bt_warningOutline)
        layout_btOutline.addWidget(self.bt_dangerOutline)

        # QPushButton link -----------------------------------
        layout_btLink = QHBoxLayout()
        fr_btLink = QFrame()
        fr_btLink.setLayout(layout_btLink)

        self.bt_primaryLink = QPushButton(PRIMARY_LINK)
        self.bt_secondaryLink = QPushButton(SECONDARY_LINK)
        self.bt_successLink = QPushButton(SUCCESS_LINK)
        self.bt_infoLink = QPushButton(INFO_LINK)
        self.bt_warningLink = QPushButton(WARNING_LINK)
        self.bt_dangerLink = QPushButton(DANGER_LINK)
        
        self.bt_primaryLink.setCheckable(True)
        self.bt_secondaryLink.setCheckable(True)
        self.bt_successLink.setCheckable(True)
        self.bt_infoLink.setCheckable(True)
        self.bt_warningLink.setCheckable(True)
        self.bt_dangerLink.setCheckable(True)
        
        self.group_bt.addButton(self.bt_primaryLink)
        self.group_bt.addButton(self.bt_secondaryLink)
        self.group_bt.addButton(self.bt_successLink)
        self.group_bt.addButton(self.bt_infoLink)
        self.group_bt.addButton(self.bt_warningLink)
        self.group_bt.addButton(self.bt_dangerLink)

        layout_btLink.addWidget(self.bt_primaryLink)
        layout_btLink.addWidget(self.bt_secondaryLink)
        layout_btLink.addWidget(self.bt_successLink)
        layout_btLink.addWidget(self.bt_infoLink)
        layout_btLink.addWidget(self.bt_warningLink)
        layout_btLink.addWidget(self.bt_dangerLink)


        #  stack widget------------------------------------- 
        self.stack = QStackedWidget()
        
        self.pagePrimary = W_Page()
        self.pageSecondary = W_Page()
        self.pageSuccess = W_Page()
        self.pageInfo = W_Page()
        self.pageWarning = W_Page()
        self.pageDanger = W_Page()
        
        self.pagePrimaryOutline = W_Page()
        self.pageSecondaryOutline = W_Page()
        self.pageSuccessOutline = W_Page()
        self.pageInfoOutline = W_Page()
        self.pageWarningOutline = W_Page()
        self.pageDangerOutline = W_Page()
        
        self.pagePrimaryLink = W_Page()
        self.pageSecondaryLink = W_Page()
        self.pageSuccessLink = W_Page()
        self.pageInfoLink = W_Page()
        self.pageWarningLink = W_Page()
        self.pageDangerLink = W_Page()


        self.stack.addWidget(self.pagePrimary)
        self.stack.addWidget(self.pageSecondary)
        self.stack.addWidget(self.pageSuccess)
        self.stack.addWidget(self.pageInfo)
        self.stack.addWidget(self.pageWarning)
        self.stack.addWidget(self.pageDanger)
        
        self.stack.addWidget(self.pagePrimaryOutline)
        self.stack.addWidget(self.pageSecondaryOutline)
        self.stack.addWidget(self.pageSuccessOutline)
        self.stack.addWidget(self.pageInfoOutline)
        self.stack.addWidget(self.pageWarningOutline)
        self.stack.addWidget(self.pageDangerOutline)

        self.stack.addWidget(self.pagePrimaryLink)
        self.stack.addWidget(self.pageSecondaryLink)
        self.stack.addWidget(self.pageSuccessLink)
        self.stack.addWidget(self.pageInfoLink)
        self.stack.addWidget(self.pageWarningLink)
        self.stack.addWidget(self.pageDangerLink)

        self.bt_primary.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.bt_secondary.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.bt_success.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        self.bt_info.clicked.connect(lambda: self.stack.setCurrentIndex(3))
        self.bt_warning.clicked.connect(lambda: self.stack.setCurrentIndex(4))
        self.bt_danger.clicked.connect(lambda: self.stack.setCurrentIndex(5))
        
        
        self.bt_primaryOutline.clicked.connect(lambda: self.stack.setCurrentIndex(6))
        self.bt_secondaryOutline.clicked.connect(lambda: self.stack.setCurrentIndex(7))
        self.bt_successOutline.clicked.connect(lambda: self.stack.setCurrentIndex(8))
        self.bt_infoOutline.clicked.connect(lambda: self.stack.setCurrentIndex(9))
        self.bt_warningOutline.clicked.connect(lambda: self.stack.setCurrentIndex(10))
        self.bt_dangerOutline.clicked.connect(lambda: self.stack.setCurrentIndex(11))

        self.bt_primaryLink.clicked.connect(lambda: self.stack.setCurrentIndex(12))
        self.bt_secondaryLink.clicked.connect(lambda: self.stack.setCurrentIndex(13))
        self.bt_successLink.clicked.connect(lambda: self.stack.setCurrentIndex(14))
        self.bt_infoLink.clicked.connect(lambda: self.stack.setCurrentIndex(15))
        self.bt_warningLink.clicked.connect(lambda: self.stack.setCurrentIndex(16))
        self.bt_dangerLink.clicked.connect(lambda: self.stack.setCurrentIndex(17))

        self.setup_style()
        self.setup_pageConfig()
        
        # add layouts principais -------
        layout_left.addWidget(fr_bt)
        layout_center.addWidget(self.stack)
        layout_right.addWidget(fr_btOutline)
        layout_bottom.addWidget(fr_btLink)


        layout_middle.addLayout(layout_left)
        layout_middle.addLayout(layout_center)
        layout_middle.addLayout(layout_right)
        layout.addLayout(layout_middle)
        layout.addLayout(layout_bottom)
        self.setLayout(layout)

        
    def setup_pageConfig(self):
        self.pagePrimary.lb.setText(PRIMARY+':')
        self.pageSecondary.lb.setText(SECONDARY+':')
        self.pageSuccess.lb.setText(SUCCESS+':')
        self.pageInfo.lb.setText(INFO+':')
        self.pageWarning.lb.setText(WARNING+':')
        self.pageDanger.lb.setText(DANGER+':')
        
        self.pagePrimary.le.setPlaceholderText(PRIMARY)
        self.pageSecondary.le.setPlaceholderText(SECONDARY)
        self.pageSuccess.le.setPlaceholderText(SUCCESS)
        self.pageInfo.le.setPlaceholderText(INFO)
        self.pageWarning.le.setPlaceholderText(WARNING)
        self.pageDanger.le.setPlaceholderText(DANGER)

        self.pagePrimary.bt.setText(PRIMARY)
        self.pageSecondary.bt.setText(SECONDARY)
        self.pageSuccess.bt.setText(SUCCESS)
        self.pageInfo.bt.setText(INFO)
        self.pageWarning.bt.setText(WARNING)
        self.pageDanger.bt.setText(DANGER)
        
        self.pagePrimary.lb.setObjectName(PRIMARY)
        self.pageSecondary.lb.setObjectName(SECONDARY)
        self.pageSuccess.lb.setObjectName(SUCCESS)
        self.pageInfo.lb.setObjectName(INFO)
        self.pageWarning.lb.setObjectName(WARNING)
        self.pageDanger.lb.setObjectName(DANGER)

        self.pagePrimary.le.setObjectName(PRIMARY)
        self.pageSecondary.le.setObjectName(SECONDARY)
        self.pageSuccess.le.setObjectName(SUCCESS)
        self.pageInfo.le.setObjectName(INFO)
        self.pageWarning.le.setObjectName(WARNING)
        self.pageDanger.le.setObjectName(DANGER)

        self.pagePrimary.bt.setObjectName(PRIMARY)
        self.pageSecondary.bt.setObjectName(SECONDARY)
        self.pageSuccess.bt.setObjectName(SUCCESS)
        self.pageInfo.bt.setObjectName(INFO)
        self.pageWarning.bt.setObjectName(WARNING)
        self.pageDanger.bt.setObjectName(DANGER)
        
        # outline ----------------
        self.pagePrimaryOutline.lb.setText(PRIMARY+':')
        self.pageSecondaryOutline.lb.setText(SECONDARY+':')
        self.pageSuccessOutline.lb.setText(SUCCESS+':')
        self.pageInfoOutline.lb.setText(INFO+':')
        self.pageWarningOutline.lb.setText(WARNING+':')
        self.pageDangerOutline.lb.setText(DANGER+':')
        
        self.pagePrimaryOutline.le.setPlaceholderText(PRIMARY)
        self.pageSecondaryOutline.le.setPlaceholderText(SECONDARY)
        self.pageSuccessOutline.le.setPlaceholderText(SUCCESS)
        self.pageInfoOutline.le.setPlaceholderText(INFO)
        self.pageWarningOutline.le.setPlaceholderText(WARNING)
        self.pageDangerOutline.le.setPlaceholderText(DANGER)

        self.pagePrimaryOutline.bt.setText(PRIMARY)
        self.pageSecondaryOutline.bt.setText(SECONDARY)
        self.pageSuccessOutline.bt.setText(SUCCESS)
        self.pageInfoOutline.bt.setText(INFO)
        self.pageWarningOutline.bt.setText(WARNING)
        self.pageDangerOutline.bt.setText(DANGER)
        
        self.pagePrimaryOutline.lb.setObjectName(PRIMARY)
        self.pageSecondaryOutline.lb.setObjectName(SECONDARY)
        self.pageSuccessOutline.lb.setObjectName(SUCCESS)
        self.pageInfoOutline.lb.setObjectName(INFO)
        self.pageWarningOutline.lb.setObjectName(WARNING)
        self.pageDangerOutline.lb.setObjectName(DANGER)

        self.pagePrimaryOutline.le.setObjectName(PRIMARY)
        self.pageSecondaryOutline.le.setObjectName(SECONDARY)
        self.pageSuccessOutline.le.setObjectName(SUCCESS)
        self.pageInfoOutline.le.setObjectName(INFO)
        self.pageWarningOutline.le.setObjectName(WARNING)
        self.pageDangerOutline.le.setObjectName(DANGER)

        self.pagePrimaryOutline.bt.setObjectName(PRIMARY_OUTLINE)
        self.pageSecondaryOutline.bt.setObjectName(SECONDARY_OUTLINE)
        self.pageSuccessOutline.bt.setObjectName(SUCCESS_OUTLINE)
        self.pageInfoOutline.bt.setObjectName(INFO_OUTLINE)
        self.pageWarningOutline.bt.setObjectName(WARNING_OUTLINE)
        self.pageDangerOutline.bt.setObjectName(DANGER_OUTLINE)

        # link -----------
        self.pagePrimaryLink.lb.setText(PRIMARY+':')
        self.pageSecondaryLink.lb.setText(SECONDARY+':')
        self.pageSuccessLink.lb.setText(SUCCESS+':')
        self.pageInfoLink.lb.setText(INFO+':')
        self.pageWarningLink.lb.setText(WARNING+':')
        self.pageDangerLink.lb.setText(DANGER+':')
        
        self.pagePrimaryLink.le.setPlaceholderText(PRIMARY)
        self.pageSecondaryLink.le.setPlaceholderText(SECONDARY)
        self.pageSuccessLink.le.setPlaceholderText(SUCCESS)
        self.pageInfoLink.le.setPlaceholderText(INFO)
        self.pageWarningLink.le.setPlaceholderText(WARNING)
        self.pageDangerLink.le.setPlaceholderText(DANGER)

        self.pagePrimaryLink.bt.setText(PRIMARY)
        self.pageSecondaryLink.bt.setText(SECONDARY)
        self.pageSuccessLink.bt.setText(SUCCESS)
        self.pageInfoLink.bt.setText(INFO)
        self.pageWarningLink.bt.setText(WARNING)
        self.pageDangerLink.bt.setText(DANGER)
        
        self.pagePrimaryLink.lb.setObjectName(PRIMARY)
        self.pageSecondaryLink.lb.setObjectName(SECONDARY)
        self.pageSuccessLink.lb.setObjectName(SUCCESS)
        self.pageInfoLink.lb.setObjectName(INFO)
        self.pageWarningLink.lb.setObjectName(WARNING)
        self.pageDangerLink.lb.setObjectName(DANGER)

        self.pagePrimaryLink.le.setObjectName(PRIMARY)
        self.pageSecondaryLink.le.setObjectName(SECONDARY)
        self.pageSuccessLink.le.setObjectName(SUCCESS)
        self.pageInfoLink.le.setObjectName(INFO)
        self.pageWarningLink.le.setObjectName(WARNING)
        self.pageDangerLink.le.setObjectName(DANGER)

        self.pagePrimaryLink.bt.setObjectName(PRIMARY_LINK)
        self.pageSecondaryLink.bt.setObjectName(SECONDARY_LINK)
        self.pageSuccessLink.bt.setObjectName(SUCCESS_LINK)
        self.pageInfoLink.bt.setObjectName(INFO_LINK)
        self.pageWarningLink.bt.setObjectName(WARNING_LINK)
        self.pageDangerLink.bt.setObjectName(DANGER_LINK)


    def setup_style(self):
        self.bt_primary.setFixedWidth(200)
        self.bt_primary.setObjectName(PRIMARY)
        self.bt_secondary.setObjectName(SECONDARY)
        self.bt_success.setObjectName(SUCCESS)
        self.bt_info.setObjectName(INFO)
        self.bt_warning.setObjectName(WARNING)
        self.bt_danger.setObjectName(DANGER)

        # outline
        self.bt_primaryOutline.setObjectName(PRIMARY_OUTLINE)
        self.bt_secondaryOutline.setObjectName(SECONDARY_OUTLINE)
        self.bt_successOutline.setObjectName(SUCCESS_OUTLINE)
        self.bt_infoOutline.setObjectName(INFO_OUTLINE)
        self.bt_warningOutline.setObjectName(WARNING_OUTLINE)
        self.bt_dangerOutline.setObjectName(DANGER_OUTLINE)
        
        # link
        self.bt_primaryLink.setObjectName(PRIMARY_LINK)
        self.bt_secondaryLink.setObjectName(SECONDARY_LINK)
        self.bt_successLink.setObjectName(SUCCESS_LINK)
        self.bt_infoLink.setObjectName(INFO_LINK)
        self.bt_warningLink.setObjectName(WARNING_LINK)
        self.bt_dangerLink.setObjectName(DANGER_LINK)


class W_Page(QWidget):
    def __init__(self) -> None:
        super().__init__()


        layout = QVBoxLayout(self)
        layout_frame = QHBoxLayout()
        self.frame = QFrame()
        self.frame.setLayout(layout_frame)
        
        self.lb = QLabel('')
        self.le = QLineEdit()
        self.bt = QPushButton()
        layout_frame.addWidget(self.lb)
        layout_frame.addWidget(self.le)
        layout_frame.addWidget(self.bt)

        layout.addWidget(self.frame)

        

        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet(get_style())
    window = W_pushButtonChecableExclusive()
    # window.resize(800, 400)
    window.show()
    sys.exit(app.exec())
