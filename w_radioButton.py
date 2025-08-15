import sys
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout, QFrame,
    QRadioButton, QLabel,
)
from style import *
from PyQt6.QtCore import Qt

class W_radioButton(QWidget):
    def __init__(self) -> None:
        super().__init__()

        layout_main = QVBoxLayout()

        layout_rb = QHBoxLayout()
        frame_rb = QFrame()
        frame_rb.setLayout(layout_rb)

        layout_rbFill = QHBoxLayout()
        frame_rbFill = QFrame()
        frame_rbFill.setLayout(layout_rbFill)

        self.lb_rb = QLabel('QRadioButton:')
        self.rb_primary = QRadioButton(PRIMARY)
        self.rb_success = QRadioButton(SUCCESS)
        self.rb_secondary = QRadioButton(SECONDARY)
        self.rb_info = QRadioButton(INFO)
        self.rb_warning = QRadioButton(WARNING)
        self.rb_danger = QRadioButton(DANGER)

        self.rb_primary.setObjectName(PRIMARY)
        self.rb_secondary.setObjectName(SECONDARY)
        self.rb_success.setObjectName(SUCCESS)
        self.rb_info.setObjectName(INFO)
        self.rb_warning.setObjectName(WARNING)
        self.rb_danger.setObjectName(DANGER)
        
        layout_rb.addWidget(self.lb_rb)
        layout_rb.addWidget(self.rb_primary)
        layout_rb.addWidget(self.rb_secondary)
        layout_rb.addWidget(self.rb_success)
        layout_rb.addWidget(self.rb_info)
        layout_rb.addWidget(self.rb_warning)
        layout_rb.addWidget(self.rb_danger)

        # radioButton fill
        self.lb_rbFill = QLabel('RadioButton Fill:')
        self.rb_primaryFill = QRadioButton(PRIMARY)
        self.rb_successFill = QRadioButton(SUCCESS)
        self.rb_secondaryFill = QRadioButton(SECONDARY)
        self.rb_infoFill = QRadioButton(INFO)
        self.rb_warningFill = QRadioButton(WARNING)
        self.rb_dangerFill = QRadioButton(DANGER)

        self.rb_primaryFill.setObjectName(PRIMARY_FILL)
        self.rb_secondaryFill.setObjectName(SECONDARY_FILL)
        self.rb_successFill.setObjectName(SUCCESS_FILL)
        self.rb_infoFill.setObjectName(INFO_FILL)
        self.rb_warningFill.setObjectName(WARNING_FILL)
        self.rb_dangerFill.setObjectName(DANGER_FILL)
        
        layout_rbFill.addWidget(self.lb_rbFill)
        layout_rbFill.addWidget(self.rb_primaryFill)
        layout_rbFill.addWidget(self.rb_secondaryFill)
        layout_rbFill.addWidget(self.rb_successFill)
        layout_rbFill.addWidget(self.rb_infoFill)
        layout_rbFill.addWidget(self.rb_warningFill)
        layout_rbFill.addWidget(self.rb_dangerFill)

        
         
        self.rb_primary.setChecked(True) 
        self.rb_primaryFill.setChecked(True) 

        layout_main.addWidget(frame_rb)
        layout_main.addWidget(frame_rbFill)

        self.setLayout(layout_main)
        
    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        if a0.key() == Qt.Key.Key_Escape: #type: ignore
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(get_style())
    
    window = W_radioButton()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec())