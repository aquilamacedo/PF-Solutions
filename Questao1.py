# como a questao nao deu um exempo, tomei a liberdade de criar um, com o nome sendo a chave e a idade o valor dessa chave.

lista = [{'aquila': '19'}, {'davi': '20'}, {'gabriel': '23'}, {'nome': 'idade'}, {'chave': 'valor'}]

qntd = int(input('Deseja verificar quantas chaves? ')) # Aqui eu criei uma entrada interativa, para o cliente colocar quantas chaves ele quer testar.

x = 0
segundaLista = []

while qntd != x:

    # como as chaves vão mudar, crei um laço de repetição while pra ir variando os valores da variavel checker de acordo com o laço for abaixo.
    
    checker = input('Verifique a existencia da chave: ') # aqui outra entrada interativa, que pede a chave para o cliente fazer os testes com as possiveis chaves
    
    # já aqui, criei uma estrutura for, para percorrer os elementos dessa lista, elementos que são do tipo: dicionários. 
    # ou seja, esse laço vai percorrer esses dicionários e tratar os valores das chaves com duas condicionais
    
    for valor in range(0,len(lista)):
        teste = lista[valor]                            # aqui eu acesso o dicionario
        
        if checker in teste:                            # a primeira condicional vai ver se a chave do dicionario condiz com o a variavel checker ou seja, essa condicional está verificando a existência da chave.
        
            saida = teste[checker]                      # aqui eu pego o valor da chave e armazeno na variavel saida
            
            if saida not in segundaLista:               # essa ultima condicional vai garantir que a lista não tenha valores repetidos, ou seja ela vê se já existe esse valor lá dentro, caso exista a condicional não é satisfeita. 
                segundaLista.append(saida)              # por fim, adiciono o valor da variavel saida na segundaLista

    x+=1 # aqui só vai incrementando 1 na variavel "x", até o while finalizar

print(segundaLista)
