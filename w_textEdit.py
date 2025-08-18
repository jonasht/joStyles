from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import (
    QWidget, QApplication, QHBoxLayout, QVBoxLayout,
    QTextEdit, QLabel, QFrame, QRadioButton,
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
        layout_rb = QVBoxLayout()

        layout_teFill = QHBoxLayout()
        frame_teFill = QFrame()
        frame_teFill.setLayout(layout_teFill)
        layout_rbFill = QVBoxLayout()

        self.lb_te = QLabel('TextEdit:')
        self.te_default = QTextEdit('='*12+'\ndefault\n'+'='*12)
        self.te_primary = QTextEdit('='*12+ f'\n{PRIMARY}\n'+'='*12)
        self.te_secondary = QTextEdit('='*12+ f'\n{SECONDARY}\n'+'='*12)
        self.te_success = QTextEdit('='*12+ f'\n{SUCCESS}\n'+'='*12)
        self.te_info = QTextEdit('='*12+ f'\n{INFO}\n'+'='*12)
        self.te_warning = QTextEdit('='*12+ f'\n{WARNING}\n'+'='*12)
        self.te_danger = QTextEdit('='*12+ f'\n{DANGER}\n'+'='*12)
        self.rb_normal = QRadioButton('Normal')
        self.rb_disabled = QRadioButton('Disable')
        self.rb_readonly = QRadioButton('ReadOnly')


        self.te_primary.setObjectName(PRIMARY)
        self.te_secondary.setObjectName(SECONDARY)
        self.te_success.setObjectName(SUCCESS)
        self.te_info.setObjectName(INFO)
        self.te_warning.setObjectName(WARNING)
        self.te_danger.setObjectName(DANGER)
        self.rb_normal.setObjectName(SUCCESS)
        self.rb_disabled.setObjectName(DANGER)
        self.rb_readonly.setObjectName(INFO)

        layout_te.addWidget(self.lb_te)
        layout_te.addWidget(self.te_default)
        layout_te.addWidget(self.te_primary)
        layout_te.addWidget(self.te_secondary)
        layout_te.addWidget(self.te_success)
        layout_te.addWidget(self.te_info)
        layout_te.addWidget(self.te_warning)
        layout_te.addWidget(self.te_danger)
        
        layout_rb.addWidget(self.rb_normal)
        layout_rb.addWidget(self.rb_disabled)
        layout_rb.addWidget(self.rb_readonly)
        layout_te.addLayout(layout_rb)
        self.rb_normal.clicked.connect(self.update_stateTe)
        self.rb_disabled.clicked.connect(self.update_stateTe)
        self.rb_readonly.clicked.connect(self.update_stateTe)
        # textEdit fill
        self.lb_teFill = QLabel('TextEdit Fill:')
        self.te_primaryFill = QTextEdit('='*12+ f'\n=={PRIMARY}\n'+'='*12)
        self.te_secondaryFill = QTextEdit('='*12+ f'\n=={SECONDARY}\n'+'='*12)
        self.te_successFill = QTextEdit('='*12+ f'\n=={SUCCESS}\n'+'='*12)
        self.te_infoFill = QTextEdit('='*12+ f'\n===={INFO}\n'+'='*12)
        self.te_warningFill = QTextEdit('='*12+ f'\n=={WARNING}\n'+'='*12)
        self.te_dangerFill = QTextEdit('='*12+ f'\n=={DANGER}\n'+'='*12)
        self.rb_normalFill = QRadioButton('Normal')
        self.rb_disabledFill = QRadioButton('Disabled')
        self.rb_readonlyFill = QRadioButton('ReadOnly')

        layout_teFill.addWidget(self.lb_teFill)
        layout_teFill.addWidget(self.te_primaryFill)
        layout_teFill.addWidget(self.te_secondaryFill)
        layout_teFill.addWidget(self.te_successFill)
        layout_teFill.addWidget(self.te_infoFill)
        layout_teFill.addWidget(self.te_warningFill)
        layout_teFill.addWidget(self.te_dangerFill)
        layout_rbFill.addWidget(self.rb_normalFill)
        layout_rbFill.addWidget(self.rb_disabledFill)
        layout_rbFill.addWidget(self.rb_readonlyFill)
        layout_teFill.addLayout(layout_rbFill)
        
        self.te_primaryFill.setObjectName(PRIMARY_FILL)
        self.te_secondaryFill.setObjectName(SECONDARY_FILL)
        self.te_successFill.setObjectName(SUCCESS_FILL)
        self.te_infoFill.setObjectName(INFO_FILL)
        self.te_warningFill.setObjectName(WARNING_FILL)
        self.te_dangerFill.setObjectName(DANGER_FILL)
        self.rb_normalFill.setObjectName(SUCCESS)
        self.rb_disabledFill.setObjectName(DANGER)
        self.rb_readonlyFill.setObjectName(INFO)

        self.rb_normalFill.clicked.connect(self.update_stateTeFill)
        self.rb_disabledFill.clicked.connect(self.update_stateTeFill)
        self.rb_readonlyFill.clicked.connect(self.update_stateTeFill)
        layout_main.addWidget(frame_te)
        layout_main.addWidget(frame_teFill)

        self.setLayout(layout_main)
        
        self.text_edits = [
            self.te_default, self.te_primary, self.te_secondary,
            self.te_success, self.te_info, self.te_warning, self.te_danger
        ]
        self.text_edits_fill = [
            self.te_primaryFill, self.te_secondaryFill, self.te_successFill,
            self.te_infoFill, self.te_warningFill, self.te_dangerFill
        ]

        
        self.rb_normal.setChecked(True)
        self.rb_normalFill.setChecked(True)
        self.update_stateTe()

    def update_stateTe(self):
        is_disabled = self.rb_disabled.isChecked()
        is_readonly = self.rb_readonly.isChecked()


        for te in self.text_edits:
            te.setEnabled(not is_disabled)
            te.setReadOnly(is_readonly)
            
    def update_stateTeFill(self):
        is_disabled = self.rb_disabledFill.isChecked()
        is_readonly = self.rb_readonlyFill.isChecked()


        for te in self.text_edits_fill:
            te.setEnabled(not is_disabled)
            te.setReadOnly(is_readonly)

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
