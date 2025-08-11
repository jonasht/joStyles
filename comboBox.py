from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QFrame, QLabel, QVBoxLayout, QHBoxLayout,
    QComboBox,
)
import sys
from style import *
from PyQt6.QtCore import Qt


class W_comboBox(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        layout_main = QVBoxLayout()
        
        
        
        
        # ComboBox ============================================
        layout_combox = QHBoxLayout()
        frame_combox = QFrame()
        frame_combox.setLayout(layout_combox)
        
        self.lb_combox = QLabel('QComboBox:')
        layout_combox.addWidget(self.lb_combox)
        


        # comboBox primary ----------------------------
        items_primary = list(map(lambda x: 'thing'+str(x) if x != 0 else PRIMARY.upper(), (range(50))))
        self.combox_primary = QComboBox()
        # self.combox_primary.setEditable(True)
        self.combox_primary.addItems(items_primary)
        self.combox_primary.setPlaceholderText('primary')
        layout_combox.addWidget(self.combox_primary)
        self.combox_primary.setObjectName(PRIMARY)
        
        # comboBox secondary ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else SECONDARY, (range(30))))
        self.combox_secondary = QComboBox()
        # self.combox_secondary.setEditable(True)
        self.combox_secondary.addItems(items)
        self.combox_secondary.setPlaceholderText(SECONDARY)
        layout_combox.addWidget(self.combox_secondary)
        self.combox_secondary.setObjectName(SECONDARY)
        
        # comboBox success ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else SUCCESS, (range(30))))
        self.combox_success = QComboBox()
        # self.combox_success.setEditable(True)
        self.combox_success.addItems(items)
        layout_combox.addWidget(self.combox_success)
        self.combox_success.setObjectName(SUCCESS)
        
        # comboBox info ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else SECONDARY, (range(30))))
        self.combox_info = QComboBox()
        # self.combox_info.setEditable(True)
        self.combox_info.addItems(items)
        layout_combox.addWidget(self.combox_info)
        self.combox_info.setObjectName(INFO)
        
        # comboBox warning ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else WARNING, (range(30))))
        self.combox_warning = QComboBox()
        # self.combox_warning.setEditable(True)
        self.combox_warning.addItems(items)
        layout_combox.addWidget(self.combox_warning)
        self.combox_warning.setObjectName(WARNING)

        # comboBox warning ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else DANGER, (range(30))))
        self.combox_danger = QComboBox()
        # self.combox_danger.setEditable(True)
        self.combox_danger.addItems(items)
        layout_combox.addWidget(self.combox_danger)
        self.combox_danger.setObjectName(DANGER)
        
        # ComboBox Desabilitado
        self.combo_disabled = QComboBox()
        self.combo_disabled.setPlaceholderText('disabled')
        self.combo_disabled.setEnabled(False)
        layout_combox.addWidget(self.combo_disabled)

        # comboBox fill ===============================================================================
        layout_comboxFill = QHBoxLayout()
        frame_comboxFill = QFrame()
        frame_comboxFill.setLayout(layout_comboxFill)
        
        self.lb_combox = QLabel('QComboBox:')
        layout_comboxFill.addWidget(self.lb_combox)

        # comboBox primary fill ----------------------------
        items_primary = list(map(lambda x: 'thing'+str(x) if x != 0 else PRIMARY_FILL, (range(50))))
        self.combox_primary = QComboBox()
        # self.combox_primary.setEditable(True)
        self.combox_primary.addItems(items_primary)
        self.combox_primary.setPlaceholderText('primary')
        layout_comboxFill.addWidget(self.combox_primary)
        self.combox_primary.setObjectName(PRIMARY_FILL)
        
        # comboBox secondary fill ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else SECONDARY_FILL, (range(30))))
        self.combox_secondary = QComboBox()
        # self.combox_secondary.setEditable(True)
        self.combox_secondary.addItems(items)
        self.combox_secondary.setPlaceholderText(SECONDARY)
        layout_comboxFill.addWidget(self.combox_secondary)
        self.combox_secondary.setObjectName(SECONDARY)
        
        # comboBox success fill ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else SUCCESS_FILL, (range(30))))
        self.combox_success = QComboBox()
        # self.combox_success.setEditable(True)
        self.combox_success.addItems(items)
        layout_comboxFill.addWidget(self.combox_success)
        self.combox_success.setObjectName(SUCCESS)
        
        # comboBox info fill ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else INFO_FILL, (range(30))))
        self.combox_info = QComboBox()
        # self.combox_info.setEditable(True)
        self.combox_info.addItems(items)
        layout_comboxFill.addWidget(self.combox_info)
        self.combox_info.setObjectName(INFO)
        
        # comboBox warning fill ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else WARNING_FILL, (range(30))))
        self.combox_warning = QComboBox()
        # self.combox_warning.setEditable(True)
        self.combox_warning.addItems(items)
        layout_comboxFill.addWidget(self.combox_warning)
        self.combox_warning.setObjectName(WARNING)

        # comboBox danger fill ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else DANGER_FILL, (range(30))))
        self.combox_danger = QComboBox()
        # self.combox_danger.setEditable(True)
        self.combox_danger.addItems(items)
        layout_comboxFill.addWidget(self.combox_danger)
        self.combox_danger.setObjectName(DANGER)
        
        
        layout_main.addWidget(frame_combox)
        layout_main.addWidget(frame_comboxFill)
        self.setLayout(layout_main)
    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        if a0.key() == Qt.Key.Key_Escape: 
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = W_comboBox()
    window.show()
    window.setGeometry(100, 100, 800, 800)
    
    app.setStyleSheet(load_style())

    sys.exit(app.exec())
