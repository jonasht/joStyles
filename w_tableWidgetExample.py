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


class W_TableWidget(QWidget):
    """
    Uma janela de exemplo didática para demonstrar o uso do QTableWidget.
    """
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        # --- 1. Criação do QTableWidget ---
        # QTableWidget é o widget que exibe uma tabela ou grade de itens.
        self.table_widget = QTableWidget()
        main_layout.addWidget(self.table_widget)

        # --- 2. Configurando o número de linhas e colunas ---
        # É importante definir isso antes de popular a tabela.
        self.table_widget.setRowCount(4)
        self.table_widget.setColumnCount(3)  # Adicionamos uma coluna para o botão de ação

        # --- 3. Configurando os cabeçalhos (headers) ---
        self.setup_headers()

        # --- 4. Populando a tabela com dados ---
        self.populate_table()

        # --- 5. Ajustando o comportamento do tamanho das colunas ---
        self.setup_column_sizes()

        # --- 6. Conectando sinais a slots (eventos) ---
        # O sinal cellClicked é emitido quando uma célula é clicada.
        self.table_widget.cellClicked.connect(self.on_cell_clicked)
        # O sinal cellDoubleClicked é emitido com um duplo clique.
        self.table_widget.cellDoubleClicked.connect(self.on_cell_double_clicked)

        self.setLayout(main_layout)

    def setup_headers(self):
        """Configura os textos dos cabeçalhos horizontal e vertical."""
        # Define os títulos para as colunas (cabeçalho horizontal).
        header_labels = ["Nome do Usuário", "Cidade de Origem", "Ação"]
        self.table_widget.setHorizontalHeaderLabels(header_labels)
        self.table_widget.setObjectName(DANGER)
        # Você também pode definir cabeçalhos para as linhas (cabeçalho vertical).
        # Ex: self.table_widget.setVerticalHeaderLabels(["ID 1", "ID 2", "ID 3", "ID 4"])

    def populate_table(self):
        """Preenche a tabela com QTableWidgetItem e outros widgets (QPushButton)."""
        # Vamos popular a tabela manualmente, linha por linha, para fins didáticos.

        # --- Linha 0 ---
        # Coluna 0 (Nome)
        self.table_widget.setItem(0, 0, QTableWidgetItem("Aloysius"))
        # Coluna 1 (Cidade)
        item_cidade_0 = QTableWidgetItem("Indore")
        item_cidade_0.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_widget.setItem(0, 1, item_cidade_0)
        # Coluna 2 (Ação com Botão)
        button_0 = QPushButton("Ver Detalhes de Aloysius")
        button_0.clicked.connect(lambda: self.on_button_clicked(0))
        self.table_widget.setCellWidget(0, 2, button_0)

        # --- Linha 1 ---
        self.table_widget.setItem(1, 0, QTableWidgetItem("Alan"))
        item_cidade_1 = QTableWidgetItem("Bhopal")
        item_cidade_1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_widget.setItem(1, 1, item_cidade_1)
        button_1 = QPushButton("Ver Detalhes de Alan")
        button_1.clicked.connect(lambda: self.on_button_clicked(1))
        self.table_widget.setCellWidget(1, 2, button_1)

        # --- Linha 2 ---
        self.table_widget.setItem(2, 0, QTableWidgetItem("Arnavi"))
        item_cidade_2 = QTableWidgetItem("Mandsaur")
        item_cidade_2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_widget.setItem(2, 1, item_cidade_2)
        button_2 = QPushButton("Ver Detalhes de Arnavi")
        button_2.clicked.connect(lambda: self.on_button_clicked(2))
        self.table_widget.setCellWidget(2, 2, button_2)

        # --- Linha 3 ---
        self.table_widget.setItem(3, 0, QTableWidgetItem("Beatriz"))
        item_cidade_3 = QTableWidgetItem("São Paulo")
        item_cidade_3.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table_widget.setItem(3, 1, item_cidade_3)
        button_3 = QPushButton("Ver Detalhes de Beatriz")
        button_3.clicked.connect(lambda: self.on_button_clicked(3))
        self.table_widget.setCellWidget(3, 2, button_3)

    def setup_column_sizes(self):
        """Ajusta como as colunas se redimensionam para se ajustar ao conteúdo ou espaço."""
        header = self.table_widget.horizontalHeader()
        # Ajusta a coluna 0 (Nome) para se redimensionar com base no seu conteúdo.
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        # Ajusta a coluna 1 (Cidade) para se redimensionar com base no seu conteúdo.
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        # Faz com que a coluna 2 (Ação) se estique para preencher o espaço restante.
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

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
        item = self.table_widget.item(row, column)
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
    window.show()
    sys.exit(app.exec())
