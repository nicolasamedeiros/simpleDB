import csv

def ler_arquivo():
    with open('database.csv', 'r') as banco:

        tabela = csv.reader(banco, delimiter=',')

        next(tabela)
        contatos = []
        for row in tabela:
            contatos.append(','.join(row))
        return contatos


pergunta = str(input("Digite 1 para ler os contatos, digite 2 para criar um novo contato: "))

if pergunta == "1":
    for contato in ler_arquivo():
        print(contato)

    
    
elif pergunta == "2":
    nome = str(input("Nome: "))
    telefone = str(input("Telefone: "))
    data = int(ler_arquivo()[-1][0]) + 1, nome, telefone 

    with open('database.csv', 'a', newline='') as banco:
        writer = csv.writer(banco)
        writer.writerow(data)
