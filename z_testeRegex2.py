import re

# Teste de exemplo
var_qss = """
QpushButton#primary {
    color: white;
}

QpushButton#primary:hover {
    background: blue;
}

QpushButton#primary-outline {
    border: 1px solid;
}
"""

padrao = r'QpushButton#primary(?!-outline)(:[\w-]+)?\s*{[^}]*}'

matches = re.finditer(padrao, var_qss, re.DOTALL)
blocos = [m.group(0) for m in matches]

resultado = "\n\n".join(blocos)
# print(resultado)

print()
from PyQt6.QtWidgets import QPushButton

def show_type(widget):
    print(widget.__class__.__name__)


bt = QPushButton()
print(bt.__subclasshook__.__name__)
    