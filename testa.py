import csv

def carregar_acessos():
    X = []
    Y = []

    arquivo = open('acesso.csv','r')
    leitor = csv.reader(arquivo)

    next(leitor)

    for home,como_funciona,contato,comprou in leitor:

        dados = [int(home), int(como_funciona),int(contato)]	

        X.append(dados)
        Y.append(int(comprou))

    return X, Y