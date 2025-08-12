from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QFrame, QVBoxLayout, QHBoxLayout,
    QLabel
)
from PyQt6.QtCore import Qt

import sys
from style import *


class W_Frame(QWidget):
    def __init__(self) -> None:
        super().__init__()
        def fmt_cons(cons):
            return (cons.upper()).replace('-', '_')
        layout_main = QVBoxLayout()

        # frames
        layout_frame = QHBoxLayout()
        frame_frame = QFrame()
        frame_frame.setLayout(layout_frame)
        self.lb_frame = QLabel('Frame:')
        layout_frame.addWidget(self.lb_frame)

        # frame primary
        layout_primary = QVBoxLayout()
        frame_primary = QFrame()
        frame_primary.setLayout(layout_primary)
        frame_primary.setFixedSize(200, 200)
        frame_primary.setObjectName(PRIMARY)
        self.lb_primary = QLabel(fmt_cons(PRIMARY))
        layout_primary.addWidget(self.lb_primary)
        
        # frame secondary  
        layout_secondary = QHBoxLayout()
        frame_secondary = QFrame()
        frame_secondary.setLayout(layout_secondary)
        frame_secondary.setFixedSize(200, 200)
        frame_secondary.setObjectName(SECONDARY)
        self.lb_secondary = QLabel(fmt_cons(SECONDARY))
        layout_secondary.addWidget(self.lb_secondary)

        # frame success
        layout_success = QHBoxLayout()
        frame_success = QFrame()
        frame_success.setLayout(layout_success)
        frame_success.setFixedSize(200, 200)
        frame_success.setObjectName(SUCCESS)
        self.lb_success = QLabel(fmt_cons(SUCCESS))
        layout_success.addWidget(self.lb_success)

        # frame info
        layout_info = QHBoxLayout()
        frame_info = QFrame()
        frame_info.setLayout(layout_info)
        frame_info.setFixedSize(200, 200)
        frame_info.setObjectName(INFO)
        self.lb_info = QLabel(fmt_cons(INFO))
        layout_info.addWidget(self.lb_info)

        # frame warning 
        layout_warning = QHBoxLayout()
        frame_warning = QFrame()
        frame_warning.setLayout(layout_warning)
        frame_warning.setFixedSize(200, 200)
        frame_warning.setObjectName(WARNING)
        self.lb_warning = QLabel(fmt_cons(WARNING))
        layout_warning.addWidget(self.lb_warning)

        # frame danger
        layout_danger = QHBoxLayout()
        frame_danger = QFrame()
        frame_danger.setLayout(layout_danger)
        frame_danger.setFixedSize(200, 200)
        frame_danger.setObjectName(DANGER)
        self.lb_danger = QLabel(fmt_cons(DANGER))
        layout_danger.addWidget(self.lb_danger)
        
        # frame fill --------------------------------------
        layout_frameFill = QHBoxLayout()
        frame_frameFill = QFrame()
        frame_frameFill.setLayout(layout_frameFill)
        self.lb_frameFill = QLabel('FrameFill:')
        layout_frameFill.addWidget(self.lb_frameFill)
        # frame primary fill
        layout_primaryFill = QHBoxLayout()
        frame_primaryFill = QFrame()
        frame_primaryFill.setLayout(layout_primaryFill)
        frame_primaryFill.setFixedSize(200, 200)
        frame_primaryFill.setObjectName(PRIMARY_FILL)
        self.lb_primaryFill = QLabel(fmt_cons(PRIMARY_FILL))
        layout_primaryFill.addWidget(self.lb_primaryFill)

        # frame secondary fill
        layout_secondaryFill = QHBoxLayout()
        frame_secondaryFill = QFrame()
        frame_secondaryFill.setLayout(layout_secondaryFill)
        frame_secondaryFill.setFixedSize(200, 200)
        frame_secondaryFill.setObjectName(SECONDARY_FILL)
        self.lb_secondaryFill = QLabel(fmt_cons(SECONDARY_FILL))
        layout_secondaryFill.addWidget(self.lb_secondaryFill)

        # frame success fill
        layout_successFill = QHBoxLayout()
        frame_successFill = QFrame()
        frame_successFill.setLayout(layout_successFill)
        frame_successFill.setFixedSize(200, 200)
        frame_successFill.setObjectName(SUCCESS_FILL)  
        self.lb_successFill = QLabel(fmt_cons(SUCCESS_FILL))
        layout_successFill.addWidget(self.lb_successFill)
        
        # frame info fill
        layout_infoFill = QHBoxLayout()
        frame_infoFill = QFrame()
        frame_infoFill.setLayout(layout_infoFill)
        frame_infoFill.setFixedSize(200, 200)
        frame_infoFill.setObjectName(INFO_FILL) 
        self.lb_infoFill = QLabel(fmt_cons(INFO_FILL))
        layout_infoFill.addWidget(self.lb_infoFill)

        # frame warning
        layout_warningFill = QHBoxLayout()
        frame_warningFill = QFrame()
        frame_warningFill.setLayout(layout_warningFill)
        frame_warningFill.setFixedSize(200, 200)
        frame_warningFill.setObjectName(WARNING_FILL) 
        self.lb_warningFill = QLabel(fmt_cons(WARNING_FILL))
        layout_warningFill.addWidget(self.lb_warningFill)
        
        # frame danger
        layout_dangerFill = QHBoxLayout()
        frame_dangerFill = QFrame()
        frame_dangerFill.setLayout(layout_dangerFill)
        frame_dangerFill.setFixedSize(200, 200)
        frame_dangerFill.setObjectName(DANGER_FILL)
        self.lb_dangerFill = QLabel(fmt_cons(DANGER_FILL))
        layout_dangerFill.addWidget(self.lb_dangerFill)
        
        # add widget frame
        layout_frame.addWidget(frame_primary)
        layout_frame.addWidget(frame_secondary)
        layout_frame.addWidget(frame_success)
        layout_frame.addWidget(frame_info)
        layout_frame.addWidget(frame_warning)
        layout_frame.addWidget(frame_danger)
        
        # add widget frame fill
        layout_frameFill.addWidget(frame_primaryFill)
        layout_frameFill.addWidget(frame_secondaryFill)
        layout_frameFill.addWidget(frame_successFill)
        layout_frameFill.addWidget(frame_infoFill)
        layout_frameFill.addWidget(frame_warningFill)
        layout_frameFill.addWidget(frame_dangerFill)
        

        layout_main.addWidget(frame_frame)
        layout_main.addWidget(frame_frameFill)


        self.setLayout(layout_main)
        

    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_Escape: # type: ignore
            self.close()
            
              
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(load_style())

    window = W_Frame()
    window.show()

    sys.exit(app.exec())


        