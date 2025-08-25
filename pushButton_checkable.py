import sys
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QHBoxLayout
from PyQt6.QtCore import Qt
from style import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()


        layout = QHBoxLayout()

        layout_1 = QVBoxLayout()
        fr_1 = QFrame()
        fr_1.setLayout(layout_1)

        self.lb_bt = QLabel('PushButton:')
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

        self.bt_primary.setObjectName(PRIMARY)
        self.bt_secondary.setObjectName(SECONDARY)
        self.bt_success.setObjectName(SUCCESS)
        self.bt_info.setObjectName(INFO)
        self.bt_warning.setObjectName(WARNING)
        self.bt_danger.setObjectName(DANGER)
        
        layout_1.addWidget(self.lb_bt)
        layout_1.addWidget(self.bt_primary)
        layout_1.addWidget(self.bt_secondary)
        layout_1.addWidget(self.bt_success)
        layout_1.addWidget(self.bt_info)
        layout_1.addWidget(self.bt_warning)
        layout_1.addWidget(self.bt_danger)
        # QPushButton OUTLINE ---------------------------------------
        layout_2 = QVBoxLayout()
        fr_2 = QFrame()
        fr_2.setLayout(layout_2)

        self.lb_btOutline = QLabel('PushButton outline:')
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

        self.bt_primaryOutline.setObjectName(PRIMARY_OUTLINE)
        self.bt_secondaryOutline.setObjectName(SECONDARY_OUTLINE)
        self.bt_successOutline.setObjectName(SUCCESS_OUTLINE)
        self.bt_infoOutline.setObjectName(INFO_OUTLINE)
        self.bt_warningOutline.setObjectName(WARNING_OUTLINE)
        self.bt_dangerOutline.setObjectName(DANGER_OUTLINE)
        
        layout_2.addWidget(self.lb_btOutline)
        layout_2.addWidget(self.bt_primaryOutline)
        layout_2.addWidget(self.bt_secondaryOutline)
        layout_2.addWidget(self.bt_successOutline)
        layout_2.addWidget(self.bt_infoOutline)
        layout_2.addWidget(self.bt_warningOutline)
        layout_2.addWidget(self.bt_dangerOutline)

        layout.addWidget(fr_1)
        layout.addWidget(fr_2)
        self.setLayout(layout)
    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        if a0.key() == Qt.Key.Key_Escape: # type: ignore
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyleSheet(get_style())
    window.show()
    sys.exit(app.exec())
