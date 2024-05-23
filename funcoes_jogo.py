import json #dicionario - banco de palavras + a dica
import random #funcao do python pra escolher a palavra aleatoria do dicionario
from boneco import boneco #bonequinho que vai morrer (interface)

#variaveis globais
CATEGORIAS = {1:"personagens", 2:"animais", 3:"comidas", 4:"cep", 5:"filmes"}
LIMITE_FACIL = 10
LIMITE_DIFICIL = 6

#funcao que vai sortear a palavra pro jogo a partir da categoria
def gerar_palavra_oculta(categoria):
    with open('banco_palavras.json', 'r') as f: #abre o banco de palavras e coloca no dic. 
        palavras = json.load(f)

    palavra_dica = random.choice(list(palavras[categoria].items())) #pegua os items, transfora em lista(transformada em tupla) e seleciona aleatoriamente com o .choice
    palavra_resultado = palavra_dica[0] #idx a palavra (chave)
    dica = palavra_dica[1] #idx a dica (valor)
    
    # coloca o '_' pra cada vez que o loop se repete, percorrendo a palavra inteira
    palavra_oculta = ['_' for num in range(0, len(palavra_resultado))]

    return palavra_oculta, palavra_resultado.upper(), dica

#funcao para quando o usuario acertar, substituir na palavra oculta (trocar '_' pela letra)
def substituir_letras(palavra_oculta, palavra_resultado, letra):
    # o enumerate retorna a cada loop, o index e o caractere nesse index e checa se é igual a letra digitada
    posicoes = [idx for idx, ch in enumerate(palavra_resultado) if ch == letra]

    for idx in posicoes: #substitui no idx pela letra (já maiuscula)
        palavra_oculta[idx] = letra

    return palavra_oculta

#onde o usuario coloca a letra
def pedir_letra(palavra_oculta, palavra_resultado, qnt_erros, registro):
    letra = str(input("Digite uma letra: ")).upper()
    if letra.isalpha(): #tratamento de erros -> verifica se é caractere alfabrbbto
        registro.append(letra) #registra na lista de letrinhas usadas
        if letra in palavra_resultado: #se tiver a letra na palavra, chama a funcao para substituir as letras
            palavra_oculta = substituir_letras(palavra_oculta, palavra_resultado, letra)
        else: #aumenta os erros pra ser usado no bonequinho (achar a fase do boneco)
            qnt_erros +=1

        return palavra_oculta, qnt_erros, registro #atualiza e retorna na funcao jogo()
    else:
        print("\nMEU AMIGO TUDO ERRADO NO JOGO, FAZ DE NOVO\n")
        pedir_letra(palavra_oculta, palavra_resultado, qnt_erros, registro)

#se a pessoa quiser chutar a palavra direto        
def chutar_palavra(palavra_resultado):
    palavra_chutada = str(input("Diz entao se tu e o bonzao msm poxa: "))
    
    return palavra_chutada.upper() == palavra_resultado #vê se tá certo e retorna um booleano (T or F)

#funcao principal do jogo
def jogo(categoria_num, dificuldade):
    #inicializa todas as variáveis
    registro = [] 
    qnt_erros = 0 
    pediu_dica = 0
    ganhou = False
    palavra_oculta, palavra_resultado, dica = gerar_palavra_oculta(CATEGORIAS.get(categoria_num)) #pega a palavra aleatoria e coloca nas variaveis

    if dificuldade == 1:
        print("\nfacil dmais\n") #foi um teste que eu decidi deixar pq achei engraçadinho
        print("-----------------------------------------------------------------")
        while qnt_erros <= LIMITE_FACIL: #pode jogar dentro do limite de erros (enquanto o bonequinho nao ta completo)
            print(boneco(dificuldade, qnt_erros))
            print(f'\nAs letras que vc ja usou sao: {registro}\n')
            print(f"\nPalavra:\n {palavra_oculta}\n")
            print("\nSe quiser dica, digite: dica.\n\nSe quiser chuta a palavra, digite: chuta.\n\nSe quiser bota letra, digite: bota.\n")
            escolha = str(input("Digite o que quer fazer: "))
            if escolha == 'dica':
                print("-----------------------------------------------------------------")
                print(f"A dica é: {dica}")
                pediu_dica = 2 #para descontar 2 pontos de quem pedir dicas
                continue #volta pro inicio do loop
            elif escolha == 'chuta': #a pessoa quer adivinhar a palavra final
                if chutar_palavra(palavra_resultado): #chutou a palavra certa? entra na condicao
                    pontuacao = 10 - qnt_erros - pediu_dica
                    ganhou = True
                    print("\puts tu é o bonzão\n")
                    print(f"pontuacao: {pontuacao}")
                    return ganhou, pontuacao, palavra_resultado
                else: #perdeu muito ruim
                    print("\nPANCADA SAIU DA LOUD SUPEEEEEEEEEERA!!!!!!!!!!!!!!!\n")
                    pontuacao = 0
                    return ganhou, pontuacao, palavra_resultado
            elif escolha == 'bota': #chama a funcao pedir_letra, que retorna tudo atualizado (palavra_oculta, qnt_erros, registro)
                palavra_oculta, qnt_erros, registro = pedir_letra(palavra_oculta, palavra_resultado, qnt_erros, registro)

            if ''.join(palavra_oculta) == palavra_resultado: #chutou todas as letras e adivinhou a palavra
                ganhou = True
                pontuacao = 10 - qnt_erros - pediu_dica
                return ganhou, pontuacao, palavra_resultado 
        pontuacao = 0
        return ganhou, pontuacao, palavra_resultado     

    elif dificuldade == 2:
        print("\ndesafios hardcore\n") #foi um teste que eu decidi deixar pq achei engraçadinho
        print("-----------------------------------------------------------------")
        while qnt_erros <= LIMITE_DIFICIL:
            print(boneco(dificuldade, qnt_erros))
            print(f'\nAs letras que vc ja usou sao: {registro}\n')
            print(f"\nPalavra:\n {palavra_oculta}\n")
            print("\nSe quiser dica, digite: dica.\n\nSe quiser chuta a palavra, digite: chuta.\n\nSe quiser bota letra, digite: bota.\n")
            escolha = str(input("Digite o que quer fazer: "))
            if escolha == 'dica':
                print("-----------------------------------------------------------------")
                print(f"\nA dica é: {dica}\n")
                pediu_dica = 2
                continue
            elif escolha == 'chuta':
                if chutar_palavra(palavra_resultado):
                    pontuacao = 10 - qnt_erros - pediu_dica
                    ganhou = True
                    print("\nPorra tu é o bonzão\n")
                    print(f"pontuacao: {pontuacao}\n")
                    return ganhou, pontuacao, palavra_resultado
                else:
                    print("\nPANCADA SAIU DA LOUD SUPEEEEEEEEEERA!!!!!!!!!!!!!!!\n")
                    pontuacao = 0
                    return ganhou, pontuacao, palavra_resultado
            elif escolha == 'bota':
                palavra_oculta, qnt_erros, registro = pedir_letra(palavra_oculta, palavra_resultado, qnt_erros, registro)
                        
            if ''.join(palavra_oculta) == palavra_resultado: #chutou todas as letras e adivinhou a palavra
                ganhou = True
                pontuacao = 10 - qnt_erros - pediu_dica
                return ganhou, pontuacao, palavra_resultado 
        pontuacao = 0
        return ganhou, pontuacao, palavra_resultado 
    else:
        print("\nMEU AMIGO TUDO ERRADO NO JOGO, FAZ DE NOVO\n\n")
