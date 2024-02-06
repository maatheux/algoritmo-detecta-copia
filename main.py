import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos
     fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado com COH-PIAH:")
    print()

    wal = float(input("Insira o tamanho médio de palavra (Média simples do número de caracteres por palavra): "))
    ttr = float(input("Insira a relação Type-Token (Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras): "))
    hlr = float(input("Insira a Razão Hapax Legomana (Número de palavras utilizadas uma única vez dividido pelo número total de palavras): "))
    sal = float(input("Insira o tamanho médio de sentença (Média simples do número de caracteres por sentença): "))
    sac = float(input("Insira a complexidade média da sentença (Média simples do número de frases por sentença): "))
    pal = float(input("Insira o tamanho medio de frase (Média simples do número de caracteres por frase): "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        print()
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    frases = re.split(r'[,:;.!?]+', sentenca)
    if frases[-1] == '':
        del frases[-1]
    return frases

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.
    '''
    #Diferença de tamanho médio de palavra:
    tmd = abs(as_a[0] - as_b[0])
    #Diferença de Relação Type-Token:
    rtt = abs(as_a[1] - as_b[1])
    #Diferença de Razão Hapax Legomana:
    rhl = abs(as_a[2] - as_b[2])
    #Diferença de tamanho médio de sentença:
    tms = abs(as_a[3] - as_b[3])
    #Diferença de complexidade de sentença:
    cs = abs(as_a[4] - as_b[4])
    #Diferença de tamanho médio de frase:
    tmf = abs(as_a[5] - as_b[5])

    grau_similaridade = (tmd + rtt + rhl + tms + cs + tmf) / 6

    return grau_similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_palavra = []
    lista_frase = separa_frases(texto)
    for a in lista_frase:
        lista_palavra += separa_palavras(a)

    
    #tamanho médio da palavra:
    aux = 0
    caracter = 0
    while aux < len(lista_palavra):
        caracter += len(lista_palavra[aux])
        aux += 1
    tmp = caracter / len(lista_palavra)


    #Relação Type-Token:
    rtt = n_palavras_diferentes(lista_palavra) / len(lista_palavra)

    
    #Razão Hapax Legomana:
    rhl = n_palavras_unicas(lista_palavra) / len(lista_palavra)

    
    #tamanho médio de sentença:
    lista_sentenca = separa_sentencas(texto)
    aux1 = 0
    caracter1 = 0
    while aux1 < len(lista_sentenca):
        caracter1 += len(lista_sentenca[aux1])
        aux1 += 1
    tms = caracter1 / len(lista_sentenca)

    
    #complexidade de sentença:
    cs = len(separa_frases(texto)) / len(separa_sentencas(texto))

    
    #tamanho médio de frase:
    caracter2 = 0
    aux2 = 0
    while aux2 < len(lista_frase):
        caracter2 += len(lista_frase[aux2])
        aux2 += 1
    tmf = caracter2 / len(lista_frase)

    
    return [tmp, rtt, rhl, tms, cs, tmf]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do
     texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    menor = 9999999
    aux = 0
    for i in range(1, len(textos) + 1):
        ass_text = calcula_assinatura(textos[i - 1])
        grau_simil = compara_assinatura(ass_text, ass_cp)
        if grau_simil < menor:
            menor = grau_simil
            aux = i
    return aux

if __name__ == "__main__":
    ass_cp = le_assinatura()
    print()
    textos = le_textos()
    print()
    print(f"O Autor do texto {avalia_textos(textos, ass_cp)} está infectado com COH-PIAH")


