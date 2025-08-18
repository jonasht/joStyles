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
)

from PyQt6.QtCore import Qt
from style import *
from PyQt6.QtGui import QColor
from jstyle import Jstyle

class W_TableWidget(QWidget):
    """
    Uma janela de exemplo didática para demonstrar o uso do QTableWidget.
    """
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        # --- 1. Criação do QTableWidget ---
        # QTableWidget é o widget que exibe uma tabela ou grade de itens.
        self.tw = QTableWidget()
        main_layout.addWidget(self.tw)

        # --- 2. Configurando o número de linhas e colunas ---
        # É importante definir isso antes de popular a tabela.
        self.tw.setRowCount(4)
        self.tw.setColumnCount(5)  # Adicionamos uma coluna para o botão de ação


        self.tw.cellClicked.connect(self.on_cell_clicked)
        self.tw.cellDoubleClicked.connect(self.on_cell_double_clicked)

        self.setLayout(main_layout)


        header_labels = ['name', 'one', 'two', 'button', 'buttonTwo']
        self.tw.setHorizontalHeaderLabels(header_labels)


        # ----------------------------------
        item_primary = QTableWidgetItem('primary')
        item_secondary = QTableWidgetItem('secondary')
        item_success = QTableWidgetItem('success')
        item_info = QTableWidgetItem('info')
        
        self.tw.setItem(0, 0, item_primary)
        self.tw.setItem(1, 0, item_secondary)
        self.tw.setItem(2, 0, item_success)
        self.tw.setItem(3, 0, item_info)
        
        
        item_primaryone = QTableWidgetItem('primary one')
        item_secondaryone = QTableWidgetItem('secondary one')
        item_successone = QTableWidgetItem('success one')
        item_infoone = QTableWidgetItem('info one')

        self.tw.setItem(0, 1, item_primaryone)
        self.tw.setItem(1, 1, item_secondaryone)
        self.tw.setItem(2, 1, item_successone)
        self.tw.setItem(3, 1, item_infoone)

        
        self.bt_primary = QPushButton('primary')
        self.bt_secondary = QPushButton('secondary')
        self.bt_success = QPushButton('success')
        self.bt_info = QPushButton('info')
        
        bt_primary2 = QPushButton('primary')
        bt_secondary2 = QPushButton('secondary')
        bt_success2 = QPushButton('success')
        bt_info2 = QPushButton('info')

        self.tw.setCellWidget(0, 3, self.bt_primary)
        self.tw.setCellWidget(1, 3, self.bt_secondary)
        self.tw.setCellWidget(2, 3, self.bt_success)
        self.tw.setCellWidget(3, 3, self.bt_info)

        
        self.tw.setCellWidget(0, 4, bt_primary2)
        self.tw.setCellWidget(1, 4, bt_secondary2)
        self.tw.setCellWidget(2, 4, bt_success2)
        self.tw.setCellWidget(3, 4, bt_info2)


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

        c = Color()
        self.bt_primary.setStyleSheet(Jstyle.BT_PRIMARY)
        self.bt_secondary.setStyleSheet(Jstyle.BT_SECONDARY)
        self.bt_success.setStyleSheet(Jstyle.BT_SUCCESS)
        self.bt_info.setStyleSheet(Jstyle.BT_INFO)
        
        item_primary.setForeground(Jcolor.PRIMARY)
        item_secondary.setForeground(Jcolor.SECONDARY)
        item_success.setForeground(Jcolor.SUCCESS)
        item_info.setForeground(Jcolor.INFO)

        item_primaryone.setBackground(QColor(c.PRIMARY))
        item_secondaryone.setBackground(QColor(c.SECONDARY))
        item_successone.setBackground(QColor(c.SUCCESS))
        item_infoone.setBackground(QColor(c.INFO))
        
        

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

    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_Escape: # type: ignore
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Tenta carregar o estilo customizado do projeto
    app.setStyleSheet(get_style())

    window = W_TableWidget()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec())
