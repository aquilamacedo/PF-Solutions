quest = int(input('Quantos itens deseja colocar no dicionario? '))
valorNumerico = 0
d1 = dict()

lista=[]

count=1

# aqui fiz uma estrutura de laço while para colocar as chaves e os valores das chaves de maneira interativa

while count != quest + 1:
    a = input('Digite a %dº Chave: ' %count)
    b = input('Digite o Valor da %dº Chave: ' %count)

    d1[a] = b # Atribui a lista a Chave e o valor dela

    lista.append(d1) # Adiciono na lista os itens do dicionario, para manipular como pede o enunciado da questao

    d1 = dict()      # aqui zero odicionario para não acumular todos os itens em um elemento na lista
    
    count+=1         # contador para a estrutura while e para marcar qual eh o numero ordinal da chave


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
