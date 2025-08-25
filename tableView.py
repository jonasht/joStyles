import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableView, QVBoxLayout, QHBoxLayout, QFrame
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from style import *

class W_tableView(QWidget):
    def __init__(self):
        super().__init__()

        lay_main = QVBoxLayout()
        # Cria o modelo
        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(['type', 'one', 'two', 'three'])

        
        dados = [
            ['primary', '---', '----', 'primary'],
            ['secondary', '---', '----', 'secondary'],
            ['success', '---', '----', 'success'],
            ['info', '---', '----', 'info'],
            ['warning', '---', '----', 'warning'],
            ['danger', '---', '----', 'danger'],
        ]

        for linha in dados:
            itens = [QStandardItem(str(coluna)) for coluna in linha]
            self.model.appendRow(itens)

        # Cria a tabela
        self.tv = QTableView()
        self.tv.setModel(self.model)
        
        # Ajusta colunas para caber o conteúdo
        self.tv.resizeColumnsToContents()
        self.tv.resizeRowsToContents()

        lay_main.addWidget(self.tv)
        self.setLayout(lay_main)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = W_tableView()
    app.setStyleSheet(get_style())
    window.show()
    
    sys.exit(app.exec())
