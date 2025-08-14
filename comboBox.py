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
        layout_comboxMain = QVBoxLayout()
        frame_comboxMain = QFrame()
        frame_comboxMain.setLayout(layout_comboxMain)

        layout_combox = QHBoxLayout()
        self.lb_combox = QLabel('QComboBox:')
        layout_combox.addWidget(self.lb_combox)
        


        # comboBox primary ----------------------------
        items_primary = list(map(lambda x: 'thing'+str(x) if x != 0 else PRIMARY.upper(), (range(12))))
        self.combox_primary = QComboBox()
        # self.combox_primary.setEditable(True)
        self.combox_primary.addItems(items_primary)
        self.combox_primary.setPlaceholderText('primary')
        layout_combox.addWidget(self.combox_primary)
        self.combox_primary.setObjectName(PRIMARY)
        
        # comboBox secondary ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else SECONDARY, (range(12))))
        self.combox_secondary = QComboBox()
        # self.combox_secondary.setEditable(True)
        self.combox_secondary.addItems(items)
        self.combox_secondary.setPlaceholderText(SECONDARY)
        layout_combox.addWidget(self.combox_secondary)
        self.combox_secondary.setObjectName(SECONDARY)
        
        # comboBox success ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else SUCCESS, (range(12))))
        self.combox_success = QComboBox()
        # self.combox_success.setEditable(True)
        self.combox_success.addItems(items)
        layout_combox.addWidget(self.combox_success)
        self.combox_success.setObjectName(SUCCESS)
        
        # comboBox info ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else SECONDARY, (range(12))))
        self.combox_info = QComboBox()
        # self.combox_info.setEditable(True)
        self.combox_info.addItems(items)
        layout_combox.addWidget(self.combox_info)
        self.combox_info.setObjectName(INFO)
        
        # comboBox warning ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else WARNING, (range(12))))
        self.combox_warning = QComboBox()
        # self.combox_warning.setEditable(True)
        self.combox_warning.addItems(items)
        layout_combox.addWidget(self.combox_warning)
        self.combox_warning.setObjectName(WARNING)

        # comboBox warning ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else DANGER, (range(12))))
        self.combox_danger = QComboBox()
        # self.combox_danger.setEditable(True)
        self.combox_danger.addItems(items)
        layout_combox.addWidget(self.combox_danger)
        self.combox_danger.setObjectName(DANGER)
        
        # comboBox Disabled =============================================================================
        layout_comboxDisabled = QHBoxLayout()
        
        self.lb_comboxDisbled = QLabel('Disabled:')
        layout_comboxDisabled.addWidget(self.lb_comboxDisbled)

        # comboBox primary --------------------------
        self.combox_primaryDisabled = QComboBox()
        self.combox_primaryDisabled.addItems(items_primary)
        self.combox_primaryDisabled.setPlaceholderText('primary')
        layout_comboxDisabled.addWidget(self.combox_primaryDisabled)
        self.combox_primaryDisabled.setEnabled(False)

        self.combox_primaryDisabled.setObjectName(PRIMARY)
        
        # comboBox secondary ----------------------------------------------------------------------
        self.combox_secondaryDisabled = QComboBox()
        self.combox_secondaryDisabled.setPlaceholderText(SECONDARY)
        layout_comboxDisabled.addWidget(self.combox_secondaryDisabled)
        self.combox_secondaryDisabled.setEnabled(False)
        self.combox_secondaryDisabled.setObjectName(SECONDARY)
        
        # comboBox success ----------------------------------------------------------------------
        self.combox_successDisabled = QComboBox()
        self.combox_successDisabled.addItems(items)
        layout_comboxDisabled.addWidget(self.combox_successDisabled)
        self.combox_successDisabled.setEnabled(False)
        self.combox_successDisabled.setObjectName(SUCCESS)
        
        # comboBox info ----------------------------------------------------------------------
        self.combox_infoDisabled = QComboBox()
        self.combox_infoDisabled.addItems(items)
        layout_comboxDisabled.addWidget(self.combox_infoDisabled)
        self.combox_infoDisabled.setEnabled(False)
        self.combox_infoDisabled.setObjectName(INFO)
        
        # comboBox warning ----------------------------------------------------------------------
        self.combox_warningDisabled = QComboBox()
        self.combox_warningDisabled.addItems(items)
        layout_comboxDisabled.addWidget(self.combox_warningDisabled)
        self.combox_warningDisabled.setEnabled(False)
        self.combox_warningDisabled.setObjectName(WARNING)

        # comboBox warning ----------------------------------------------------------------------
        self.combox_dangerDisabled = QComboBox()
        self.combox_dangerDisabled.addItems(items)
        layout_comboxDisabled.addWidget(self.combox_dangerDisabled)
        self.combox_dangerDisabled.setEnabled(False)
        self.combox_dangerDisabled.setObjectName(DANGER)

        layout_comboxMain.addLayout(layout_combox)
        layout_comboxMain.addLayout(layout_comboxDisabled)
        
        # comboBox fill ===============================================================================
        layout_comboxFillMain = QVBoxLayout()
        frame_comboxFillMain = QFrame()
        frame_comboxFillMain.setLayout(layout_comboxFillMain)
        layout_comboxFill = QHBoxLayout()
        self.lb_comboxFill = QLabel('QComboBox Fill:')
        layout_comboxFill.addWidget(self.lb_comboxFill)

        # comboBox primary fill ----------------------------
        items_primary = list(map(lambda x: 'thing'+str(x) if x != 0 else PRIMARY_FILL, (range(12))))
        self.combox_primaryFill = QComboBox()
        self.combox_primaryFill.addItems(items_primary)
        self.combox_primaryFill.setPlaceholderText('primary')
        layout_comboxFill.addWidget(self.combox_primaryFill)
        self.combox_primaryFill.setObjectName(PRIMARY_FILL)
        
        # comboBox secondary fill ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else SECONDARY_FILL, (range(12))))
        self.combox_secondaryFill = QComboBox()
        self.combox_secondaryFill.addItems(items)
        self.combox_secondaryFill.setPlaceholderText(SECONDARY_FILL)
        layout_comboxFill.addWidget(self.combox_secondaryFill)
        self.combox_secondaryFill.setObjectName(SECONDARY_FILL)
        
        # comboBox success fill ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else SUCCESS_FILL, (range(12))))
        self.combox_successFill = QComboBox()
        self.combox_successFill.addItems(items)
        layout_comboxFill.addWidget(self.combox_successFill)
        self.combox_successFill.setObjectName(SUCCESS_FILL)
        
        # comboBox info fill ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else INFO_FILL, (range(12))))
        self.combox_infoFill = QComboBox()
        self.combox_infoFill.addItems(items)
        layout_comboxFill.addWidget(self.combox_infoFill)
        self.combox_infoFill.setObjectName(INFO_FILL)
        
        # comboBox warning fill ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else WARNING_FILL, (range(12))))
        self.combox_warningFill = QComboBox()
        self.combox_warningFill.addItems(items)
        layout_comboxFill.addWidget(self.combox_warningFill)
        self.combox_warningFill.setObjectName(WARNING_FILL)

        # comboBox danger fill ----------------------------------------------------------------------
        items = list(map(lambda x: 'thing'+str(x) if x != 0 else DANGER_FILL, (range(12))))
        self.combox_dangerFill = QComboBox()
        self.combox_dangerFill.addItems(items)
        layout_comboxFill.addWidget(self.combox_dangerFill)
        self.combox_dangerFill.setObjectName(DANGER_FILL)
        layout_comboxFillMain.addLayout(layout_comboxFill)
        
        # combox Fill Disabled ==============================================================================
        layout_comboxFillDisabled = QHBoxLayout()
        self.lb_comboxFillDisabled = QLabel('Disabled:')
        layout_comboxFillDisabled.addWidget(self.lb_comboxFillDisabled)

        # comboBox primary fill ----------------------------
        self.combox_primaryFillDisabled = QComboBox()
        self.combox_primaryFillDisabled.setPlaceholderText('primary')
        self.combox_primaryFillDisabled.setEnabled(False)
        layout_comboxFillDisabled.addWidget(self.combox_primaryFillDisabled)
        self.combox_primaryFillDisabled.setObjectName(PRIMARY_FILL)
        
        # comboBox secondary fill ----------------------------------------------------------------------
        self.combox_secondaryFillDisabled = QComboBox()
        self.combox_secondaryFillDisabled.setPlaceholderText(SECONDARY_FILL)
        self.combox_secondaryFillDisabled.setEnabled(False)
        layout_comboxFillDisabled.addWidget(self.combox_secondaryFillDisabled)
        self.combox_secondaryFillDisabled.setObjectName(SECONDARY_FILL)
        
        # comboBox success fill ----------------------------------------------------------------------
        self.combox_successFillDisabled = QComboBox()
        self.combox_successFillDisabled.setPlaceholderText(SUCCESS_FILL)
        self.combox_successFillDisabled.setEnabled(False)
        layout_comboxFillDisabled.addWidget(self.combox_successFillDisabled)
        self.combox_successFillDisabled.setObjectName(SUCCESS_FILL)
        
        # comboBox info fill ----------------------------------------------------------------------
        self.combox_infoFillDisabled = QComboBox()
        self.combox_infoFillDisabled.setPlaceholderText(INFO_FILL)
        self.combox_infoFillDisabled.setEnabled(False)
        layout_comboxFillDisabled.addWidget(self.combox_infoFillDisabled)
        self.combox_infoFillDisabled.setObjectName(INFO_FILL)
        
        # comboBox warning fill ----------------------------------------------------------------------
        self.combox_warningFillDisabled = QComboBox()
        self.combox_warningFillDisabled.setPlaceholderText(WARNING_FILL)
        self.combox_warningFillDisabled.setEnabled(False)
        layout_comboxFillDisabled.addWidget(self.combox_warningFillDisabled)
        self.combox_warningFillDisabled.setObjectName(WARNING_FILL)

        # comboBox danger fill ----------------------------------------------------------------------
        self.combox_dangerFillDisabled = QComboBox()
        self.combox_dangerFillDisabled.setPlaceholderText(DANGER_FILL)
        self.combox_dangerFillDisabled.setEnabled(False)
        self.combox_dangerFillDisabled.setObjectName(DANGER_FILL)
        layout_comboxFillDisabled.addWidget(self.combox_dangerFillDisabled)
        
        
        layout_comboxFillMain.addLayout(layout_comboxFill)
        layout_comboxFillMain.addLayout(layout_comboxFillDisabled)

        layout_main.addWidget(frame_comboxMain)
        layout_main.addWidget(frame_comboxFillMain)
        self.setLayout(layout_main)
        
    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        if a0.key() == Qt.Key.Key_Escape: # type: ignore
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = W_comboBox()
    window.show()
    window.setGeometry(100, 100, 800, 800)
    
    app.setStyleSheet(get_style())

    sys.exit(app.exec())
