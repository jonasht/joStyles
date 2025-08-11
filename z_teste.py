# Função lambda que multiplica um número por 2
# func_lambda = lambda x: 'success'+ str(i) for i in range(10))

# Lista de números
# numbers = range(10)
# 
# result = list(map(func_lambda, numbers))
# print(result)  # Saída: [2, 4, 6, 8, 10]


variavel = list(map(lambda x: 'thing'+str(x) if x != 0 else 'success', (range(10))))

print(variavel)