import sys
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QApplication,
    QHeaderView,
    QPushButton,
    QMessageBox,
    QHBoxLayout,
)

from PyQt6.QtCore import Qt
from style import *
from PyQt6.QtGui import QColor
from jstyle import JButton, JButton, JLabel

class W_TableWidget(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        layout_btTop = QHBoxLayout()
        
        self.bt_defaultTop = QPushButton('Default')
        self.bt_primaryTop = QPushButton('Primary')
        self.bt_secondaryTop = QPushButton('Secondary')
        self.bt_successTop = QPushButton('Sucess')
        self.bt_infoTop = QPushButton('Info')
        self.bt_warningTop = QPushButton('Warning')
        self.bt_dangerTop = QPushButton('Danger')
        
        self.bt_primaryTop.setObjectName(PRIMARY)
        self.bt_secondaryTop.setObjectName(SECONDARY)
        self.bt_successTop.setObjectName(SUCCESS)
        self.bt_infoTop.setObjectName(INFO)
        self.bt_warningTop.setObjectName(WARNING)
        self.bt_dangerTop.setObjectName(DANGER)

        self.bt_defaultTop.clicked.connect(lambda: self.set_table_style(''))
        self.bt_primaryTop.clicked.connect(lambda: self.set_table_style(PRIMARY))
        self.bt_secondaryTop.clicked.connect(lambda: self.set_table_style(SECONDARY))
        self.bt_successTop.clicked.connect(lambda: self.set_table_style(SUCCESS))
        self.bt_infoTop.clicked.connect(lambda: self.set_table_style(INFO))
        self.bt_warningTop.clicked.connect(lambda: self.set_table_style(WARNING))
        self.bt_dangerTop.clicked.connect(lambda: self.set_table_style(DANGER))

        layout_btTop.addWidget(self.bt_defaultTop)
        layout_btTop.addWidget(self.bt_primaryTop)
        layout_btTop.addWidget(self.bt_secondaryTop)
        layout_btTop.addWidget(self.bt_successTop)
        layout_btTop.addWidget(self.bt_infoTop)
        layout_btTop.addWidget(self.bt_warningTop)
        layout_btTop.addWidget(self.bt_dangerTop)
        main_layout.addLayout(layout_btTop)
        self.tw = QTableWidget()

        main_layout.addWidget(self.tw)

        self.tw.setRowCount(7)
        self.tw.setColumnCount(5) 

        self.tw.cellClicked.connect(self.on_cell_clicked)
        self.tw.cellDoubleClicked.connect(self.on_cell_double_clicked)

        self.setLayout(main_layout)


        header_labels = ['name', 'one', 'two', 'pushButton', 'PushButton Outline', 'PushButton Link']
        self.tw.setHorizontalHeaderLabels(header_labels)


        # ----------------------------------
        item_primary = QTableWidgetItem('primary')
        item_secondary = QTableWidgetItem('secondary')
        item_success = QTableWidgetItem('success')
        item_info = QTableWidgetItem('info')
        item_warning = QTableWidgetItem('warning')
        item_danger = QTableWidgetItem('danger')
        item_space = QTableWidgetItem('---')
        
        self.tw.setItem(0, 0, item_primary)
        self.tw.setItem(1, 0, item_secondary)
        self.tw.setItem(2, 0, item_success)
        self.tw.setItem(3, 0, item_info)
        self.tw.setItem(4, 0, item_warning)
        self.tw.setItem(5, 0, item_danger)
        self.tw.setItem(6, 0, item_space)
        
        item_primaryone = QTableWidgetItem('primary one')
        item_secondaryone = QTableWidgetItem('secondary one')
        item_successone = QTableWidgetItem('success one')
        item_infoone = QTableWidgetItem('info one')
        item_warningone = QTableWidgetItem('warning one')
        item_dangerone = QTableWidgetItem('danger one')

        self.tw.setItem(0, 1, item_primaryone)
        self.tw.setItem(1, 1, item_secondaryone)
        self.tw.setItem(2, 1, item_successone)
        self.tw.setItem(3, 1, item_infoone)
        self.tw.setItem(4, 1, item_warningone)
        self.tw.setItem(5, 1, item_dangerone)


        
        self.bt_primary = QPushButton('primary')
        self.bt_secondary = QPushButton('secondary')
        self.bt_success = QPushButton('success')
        self.bt_info = QPushButton('info')
        bt_warning = QPushButton('warning')
        bt_danger = QPushButton('danger')
        bt_link = QPushButton('link')
        
        bt_primaryOutline = QPushButton('primary outline')
        bt_secondaryOutline = QPushButton('secondary outline')
        bt_successOutline = QPushButton('success outline')
        bt_infoOutline = QPushButton('info outline')
        bt_warningOutline = QPushButton('warning outline')
        bt_dangerOutline = QPushButton('danger outline')

        self.tw.setCellWidget(0, 3, self.bt_primary)
        self.tw.setCellWidget(1, 3, self.bt_secondary)
        self.tw.setCellWidget(2, 3, self.bt_success)
        self.tw.setCellWidget(3, 3, self.bt_info)
        self.tw.setCellWidget(4, 3, bt_warning)
        self.tw.setCellWidget(5, 3, bt_danger)
        self.tw.setCellWidget(6, 3, bt_link)

        
        self.tw.setCellWidget(0, 4, bt_primaryOutline)
        self.tw.setCellWidget(1, 4, bt_secondaryOutline)
        self.tw.setCellWidget(2, 4, bt_successOutline)
        self.tw.setCellWidget(3, 4, bt_infoOutline)
        self.tw.setCellWidget(4, 4, bt_warningOutline)
        self.tw.setCellWidget(5, 4, bt_dangerOutline)
        


        self.tw.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents) # type: ignore
        self.tw.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents) # type: ignore
        self.tw.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents) # type: ignore
        self.tw.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch) # type: ignore
        self.tw.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents) # type: ignore
        self.tw.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch) # type: ignore
        
        self.tw.verticalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents) # type: ignore
        self.tw.verticalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents) # type: ignore
        self.tw.verticalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents) # type: ignore
        self.tw.verticalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents) # type: ignore
        self.tw.verticalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents) # type: ignore
        self.tw.verticalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents) # type: ignore
        
        jc = Jcolor()
        jbt = JButton()
        jlb = JLabel()

        self.bt_primary.setStyleSheet(jbt.primary)
        self.bt_secondary.setStyleSheet(jbt.secondary)
        self.bt_success.setStyleSheet(jbt.success)
        self.bt_info.setStyleSheet(jbt.info)
        bt_warning.setStyleSheet(jbt.warning)
        bt_danger.setStyleSheet(jbt.danger)
        bt_link.setStyleSheet(jbt.link)
        
        bt_primaryOutline.setStyleSheet(jbt.primaryOutline)
        bt_secondaryOutline.setStyleSheet(jbt.secondaryOutline)
        bt_successOutline.setStyleSheet(jbt.successOutline)
        bt_infoOutline.setStyleSheet(jbt.infoOutline)
        bt_warningOutline.setStyleSheet(jbt.warningOutline)
        bt_dangerOutline.setStyleSheet(jbt.dangerOutline)
        
        
        item_primary.setForeground(jc.PRIMARY)
        item_secondary.setForeground(jc.SECONDARY)
        item_success.setForeground(jc.SUCCESS)
        item_info.setForeground(jc.INFO)
        item_warning.setForeground(jc.WARNING)
        item_danger.setForeground(jc.DANGER)

        
        item_primaryone.setBackground(jc.PRIMARY)
        item_secondaryone.setBackground(jc.SECONDARY)
        item_successone.setBackground(jc.SUCCESS)
        item_infoone.setBackground(jc.INFO)
        item_warningone.setBackground(jc.WARNING)
        item_dangerone.setBackground(jc.DANGER)
        
        # self.tw.setObjectName(PRIMARY)

    def on_button_clicked(self, row):
        """Slot que é chamado quando um dos botões na tabela é clicado."""
        name_item = self.table_widget.item(row, 0)
        city_item = self.table_widget.item(row, 1)
        # Verificamos se os itens não são nulos antes de acessar o texto
        if name_item and city_item:
            QMessageBox.information(self, "Botão Clicado", f"Você clicou no botão da linha de '{name_item.text()}' que mora em '{city_item.text()}'.")

    def on_cell_clicked(self, row, column):
        """Slot para o clique em qualquer célula."""
        print(f"Célula clicada: Linha={row}, Coluna={column}")

    def on_cell_double_clicked(self, row, column):
        """Slot para o duplo clique em uma célula."""
        item = self.tw.item(row, column)
        if item:
            QMessageBox.information(self, "Duplo Clique", f"Você deu um duplo clique em '{item.text()}'.")

    def set_table_style(self, style_name):
        """Define o nome do objeto para a tabela e reaplica a folha de estilo."""
        self.tw.setObjectName(style_name)
        self.tw.style().unpolish(self.tw)
        self.tw.style().polish(self.tw)
        self.tw.setAlternatingRowColors(True)

    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_Escape: # type: ignore
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(get_style())

    window = W_TableWidget()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec())
