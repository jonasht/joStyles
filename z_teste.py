import re

# Lê o conteúdo do arquivo
with open("styleSheet.css", "r", encoding="utf-8") as file:
    texto = file.read()

# Remove tudo entre /* e */ (comentários multilinha)
# re.DOTALL faz o "." pegar também quebras de linha
texto_sem_comentarios = re.sub(r"/\*([\s\S]*?)\*/", "", texto, flags=re.DOTALL)

# Escreve de volta no mesmo arquivo
with open("styleSheet.css", "w", encoding="utf-8") as file:
    file.write(texto_sem_comentarios)
