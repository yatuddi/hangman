#importar todas as funcoes escritas para o jogo
from funcoes_jogo import jogo
from funcoes_ranking import mostrar_ranking, atualizar_ranking
from regras import instrucoes

#definir a funcao do menu de entrada p/ o jogo
def menu():
    print(
        '''#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

                            Jogo da Forca!                          
                                                            
                        1] Iniciar o Jogo
                            
                        2] Ranking
                            
                        3] Instruções
                                
                        4] Sair    

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        '''
    )
    #executar a escolha do usuário
    escolha = int(input("Insira o número do que quer fazer: "))

    if escolha == 1:
        menu_jogo()
        menu()
    elif escolha == 2:
        mostrar_ranking()
        menu()
    elif escolha == 3:
        instrucoes()
        menu()
    elif escolha == 4:
        print("\nXAU\n")
        exit()
    else:
        print("MEU AMIGO TUDO ERRADO, FAZ DE NOVO")
        menu()  #tratamento de erro -> executa o menu de novo caso o usuario digite algo que o programa nao aceita

def menu_jogo():
    print(
        '''#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

                            Vamos jogar!                          
                                                            
                        Escolha sua categoria:

                        1] Personagens

                        2] Animais

                        3] Comidas

                        4] Cidades e Países

                        5] Filmes

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        ''')
    
    categoria = int(input("Digite aqui sua categoria de jogo: "))

    #tratamento de erros -> so aceita numeros nas categorias
    if categoria >= 1 and categoria <= 5:
        pass
    else:
        print("MEU AMIGO TUDO ERRADO, FAZ DE NOVO")
        menu_jogo()

    print(
        '''#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

                            Vamos jogar!                          
                                                            
                        Escolha sua dificuldade:

                        1] Fácil (10 chances de erro)
                                
                        2] Difícil (6 chances de erro)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        ''')
    dificuldade = int(input("Digite aqui sua dificuldade de jogo: "))

    if dificuldade >= 1 and dificuldade <= 2:
        pass
    else:
        print("MEU AMIGO TUDO ERRADO, FAZ DE NOVO")

    #receber o que a funcao do jogo retornou nessas variáveis
    usuario_ganhou, usuario_pontuacao, resposta = jogo(categoria, dificuldade)

    #passar o nome do usuário e a pontuacao para o dicionário
    if usuario_ganhou:
        print("\narabéns moparcero ce é mt baum\n")
        usuario_nome = input("\ndiz seu nome aí pro hall da fama dos miózin que tão tendo: ")
        atualizar_ranking(usuario_nome, usuario_pontuacao)

    #perdedores nao vao pro ranking pq a pontuacao é 0
    else:
        print(f'\nperdedores nao vao pro hall da fama.\n MELHORE.\nA RESPOSTA CERTA ERA ESSA SEU ESTÚPIDO NOJENTO: {resposta}')
        menu()

#rodar so as funcoes quando chamadas nesse arquivo
if __name__ == '__main__':
    menu()