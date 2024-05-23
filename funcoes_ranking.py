import json

CAMINHO_JSON = 'ranking.json'

#funcao abre o arq no modo de leitura e transforma o conteudo no dic. python e o retorna
def ler_json(caminho):
    with open(caminho, mode='r') as arquivo:
        dicionario = json.load(arquivo)
    return dicionario

#funcao pega o dic. e insere uma chave nova com um um valor novo (atualiza a chave)
def inserir_rank(usuario_nome, usuario_pontuacao, dicionario):
    dicionario[usuario_nome] = usuario_pontuacao #idx 0 = nome da pessoa / idx 1 = pontuacao
    return dicionario

#abrir o arq. do parametro caminho (modo escrita) e reescrever o arq. com o dic. no parametro
def atualizar_json(caminho, dicionario):
    with open(caminho, mode='w') as arquivo:
        json.dump(dicionario, arquivo, indent=4)

#funcao que vai ser chamada no menu quando alguem vencer o jogo e insere a pessoa no ranking
def atualizar_ranking(usuario_nome, usuario_pontuacao):
    rank_dicionario = ler_json(CAMINHO_JSON)
    rank_dicionario = inserir_rank(usuario_nome, usuario_pontuacao, rank_dicionario)
    atualizar_json(CAMINHO_JSON, rank_dicionario)
    print("\nRanking Atualizado\n")

#funcao aux. usado para ordenar o ranking
def pegar_valor(item):
    return item[1] #pega na tupla o valor 1 pra organizar pelo idx

#lê o json, ordena(decrescente) e imprime
def mostrar_ranking():
    contador = 1 #contador pra colocar os lugares no printf
    rank_dicionario = ler_json(CAMINHO_JSON) #lê e guradando no dic.
    ranking_ordenado = sorted(rank_dicionario.items(), key=pegar_valor, reverse=True) #ordenando na ordem decrescente
    
    print("\nDo miózinho que tá tendo até a escória da sociedade: \n")

    for (nome, pontuacao) in ranking_ordenado:
        print(f'{contador}°: {nome} -> {pontuacao} pontos!\n')
        contador+=1