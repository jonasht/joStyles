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
def read_qss():
    with open('./pushButton.qss', 'r') as file:
        return file.read()
    
var_qss = read_qss()

padrao = r'QpushButton#primary(?!-outline)(:[\w-]+)?\s*{[^}]*}'

matches = re.finditer(padrao, var_qss, re.DOTALL)
blocos = [m.group(0) for m in matches]

resultado = "\n\n".join(blocos)
print(resultado)

print()
print()
read_qss()
    