import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout, QFrame,
    QRadioButton, QLabel,
)
from style import *


class W_radioButton(QWidget):
    def __init__(self) -> None:
        super().__init__()

        layout_main = QVBoxLayout()

        # QRadioButton
        layout_rb = QHBoxLayout()
        frame_rb = QFrame()
        frame_rb.setLayout(layout_rb)

        self.lb_rb = QLabel('QRadioButton:')
        self.rb_primary = QRadioButton(PRIMARY.capitalize())
        self.rb_success = QRadioButton(SUCCESS.capitalize())
        self.rb_secondary = QRadioButton(SECONDARY.capitalize())
        self.rb_info = QRadioButton(INFO.capitalize())
        self.rb_warning = QRadioButton(WARNING.capitalize())
        self.rb_danger = QRadioButton(DANGER.capitalize())

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

        
        
        self.rb_primary.setChecked(True)  # Começa com uma opção selecionada
        layout_main.addWidget(frame_rb)

        self.setLayout(layout_main)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Carrega o estilo da sua biblioteca joStyles
    app.setStyleSheet(load_style())
    window = W_radioButton()
    window.show()
    sys.exit(app.exec())