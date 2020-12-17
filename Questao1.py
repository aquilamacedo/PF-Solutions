arquivo = input('Digite o nome do arquivo: ')    # ex: arquivo.csv


with open (arquivo, 'r') as dado:
    lista = []
    for valor in dado:
        valor = valor.rstrip('\n')  # Uso o rstrip para tirar os espaçamentos em branco e conseguir trabalhar com as linhas úteis
        x = valor.split(';')        # Aqui  faço a aplicação do split usando como parâmetro de separador o caracter ';'
        x = x[1]                    # Como meu valor de retorno eh uma lista, acesso justamente os nomes, assim como a questão pedia
        lista.append(x)             # Por fim, adiciono todos os nomes do arquivos em uma lista.

    print(lista)
