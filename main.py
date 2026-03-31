import math # usado para infinito 
import random # usado para sortear quem começa o jogo


# verifica se um jogador venceu o jogo
def verificar_vencedor(board, jogador):

    # todas as combinações possíveis de vitória
    vitorias = [
        [0,1,2],  # linha superior
        [3,4,5],  # linha do meio
        [6,7,8],  # linha inferior
        [0,3,6],  # coluna esquerda
        [1,4,7],  # coluna do meio
        [2,5,8],  # coluna direita
        [0,4,8],  # diagonal principal
        [2,4,6]   # diagonal secundária
    ]

    # verifica se alguma das combinações possui o mesmo símbolo
    return any(all(board[i] == jogador for i in combo) for combo in vitorias)


# verifica se o tabuleiro está cheio (empate)
def esta_cheio(board):
    return ' ' not in board


# mostra o tabuleiro no console
def exibir_tabuleiro(board):

    # percorre o tabuleiro de 3 em 3 posições (3 colunas)
    for i in range(0, 9, 3):
        linha = []

        # percorre cada posição da linha
        for j in range(3):
            pos = i + j

            # se estiver vazio, mostra o número da posição
            if board[pos] == ' ':
                linha.append(str(pos))

            # se já estiver ocupado, mostra X ou O
            else:
                linha.append(board[pos])

        # imprime a linha do tabuleiro
        print(f" {linha[0]} | {linha[1]} | {linha[2]} ")

        # imprime separador entre as linhas
        if i < 6:
            print("-----------")


# algoritmo Minimax
# decide qual jogada é a melhor considerando todas as possibilidades
def minimax(board, is_maximizing, ai_sym, user_sym):

    # verifica se a IA venceu
    if verificar_vencedor(board, ai_sym):
        return 10

    # verifica se o humano venceu
    if verificar_vencedor(board, user_sym):
        return -10

    # verifica empate
    if esta_cheio(board):
        return 0

    # turno da IA (MAX)
    # IA tenta maximizar a pontuação
    if is_maximizing:

        melhor_score = -math.inf   # começa com o menor valor possível

        # testa todas as posições do tabuleiro
        for i in range(9):

            # se a posição estiver vazia
            if board[i] == ' ':

                # simula a jogada da IA
                board[i] = ai_sym

                # chama minimax novamente (agora é turno do humano)
                score = minimax(board, False, ai_sym, user_sym)

                # desfaz a jogada 
                board[i] = ' '

                # escolhe o maior valor
                melhor_score = max(score, melhor_score)
        return melhor_score


    # turno do humano (MIN)
    # humano tenta minimizar a pontuação da IA
    else:

        pior_score = math.inf   # começa com o maior valor possível
        for i in range(9):
            if board[i] == ' ':

                # simula jogada do humano
                board[i] = user_sym

                # chama minimax novamente (agora é turno da IA)
                score = minimax(board, True, ai_sym, user_sym)

                # desfaz jogada
                board[i] = ' '

                # escolhe o menor valor
                pior_score = min(score, pior_score)
        return pior_score


# escolhe a melhor jogada possível para a IA
def escolha_da_ia(board, ai_sym, user_sym):

    melhor_valor = -math.inf
    jogada_escolhida = -1

    # testa todas as posições disponíveis
    for i in range(9):
        if board[i] == ' ':
            # simula a jogada da IA
            board[i] = ai_sym

            # calcula o valor da jogada usando minimax
            valor_da_jogada = minimax(board, False, ai_sym, user_sym)

            # desfaz a jogada
            board[i] = ' '

            # verifica se essa jogada é melhor que as anteriores
            if valor_da_jogada > melhor_valor:
                melhor_valor = valor_da_jogada
                jogada_escolhida = i
    return jogada_escolhida


# função principal do jogo
def jogar():

    # cria tabuleiro vazio
    tabuleiro = [' ' for _ in range(9)]

    # usuário escolhe símbolo
    user_sym = input("Escolha seu símbolo (X ou O): ").strip().upper()

    # garante que o usuário escolha X ou O
    while user_sym not in ['X', 'O']:
        user_sym = input("Inválido. Escolha X ou O: ").strip().upper()


    # define símbolo da IA
    ai_sym = 'O' if user_sym == 'X' else 'X'


    # sorteia quem começa
    turno = random.choice(['Humano', 'IA'])

    print(f"Você é '{user_sym}'. A IA é '{ai_sym}'.")
    print(f"Quem começa: {turno}\n")


    # loop principal do jogo
    while True:

        # mostra o tabuleiro atualizado
        exibir_tabuleiro(tabuleiro)


        # turno do jogador humano
        if turno == 'Humano':

            try:
                # usuário escolhe posição
                jogada = int(input("Escolha uma posição (0-8): "))

                # verifica se o número é válido
                if jogada < 0 or jogada > 8:
                    print("Entrada inválida. Use números de 0 a 8.")
                    continue

                # verifica se a posição está ocupada
                if tabuleiro[jogada] != ' ':
                    print("Posição já ocupada!")
                    continue

                # registra jogada do humano
                tabuleiro[jogada] = user_sym

                # verifica vitória do humano
                if verificar_vencedor(tabuleiro, user_sym):
                    exibir_tabuleiro(tabuleiro)
                    print("Você venceu!")
                    break

                # passa turno para IA
                turno = 'IA'

            except (ValueError, IndexError):
                print("Entrada inválida. Use números de 0 a 8.")
                continue

        # turno da IA
        else:
            print("\nIA pensando...")

            # IA escolhe melhor jogada
            index_ia = escolha_da_ia(tabuleiro, ai_sym, user_sym)

            # registra jogada da IA
            tabuleiro[index_ia] = ai_sym

            # verifica vitória da IA
            if verificar_vencedor(tabuleiro, ai_sym):
                exibir_tabuleiro(tabuleiro)
                print("A IA venceu!")
                break

            # passa turno para humano
            turno = 'Humano'

        # verifica empate
        if esta_cheio(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

# executa o jogo
if __name__ == "__main__":
    jogar()
