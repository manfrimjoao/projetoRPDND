#Lê a quantidade de operações a ser realizada
with open('arquivo.txt', 'r') as file:
    nLeituras = int(file.readline().strip())
   
    # Para cada operação, ler qual operação sera feita e os dois conjuntos a serem usados
    for _ in range(nLeituras):
        operacao = file.readline().strip()
        primeiroConjunto = set(file.readline().strip().split(", "))
        segundoConjunto = set(file.readline().strip().split(", "))

        # Lê e executa a operação e atribui o resultado a variavel de resultado
        if operacao == "U":
            res = primeiroConjunto.union(segundoConjunto)
            printOp = "Uniao"
        elif operacao == "I":
            res = primeiroConjunto.intersection(segundoConjunto)
            printOp = "Intersecao"
        elif operacao == "D":
            res = primeiroConjunto.difference(segundoConjunto)
            printOp = "Diferenca"
        elif operacao == "C":
            res = {(x, y) for x in primeiroConjunto for y in segundoConjunto}
            printOp = "Produto cartesiano"
       
        print('Operacao: ',printOp)
        print(primeiroConjunto)
        print(segundoConjunto)
        print(res)