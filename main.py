import random
#
# with open('arquivo_dicionario.txt', 'r') as f:
#     dicionario = set(f.read().split())
#
# with open('arquivo_texto.txt', 'r') as f:
#     texto = f.read().split()
#
# for palavra in texto:
#     if palavra.lower() not in dicionario:
#         print(f"A palavra '{palavra}' não está no dicionário.")




# CODIGO POR W4LKER
# CUIABA, MAIO DE 2023
# LICENÇA MIT


# QUANTIDADE DE LETRAS A SEREM DISTRIBUIDAS E AS LETRAS BRANCAS CORINGA REPRESENTADAS POR ASTERISCO
distribuicao_letras = {
    "A": 14, "B": 3, "C": 4, "Ç": 2, "D": 5, "E": 11, "F": 2, "G": 2, "H": 2, "I": 10, "J": 2, "L": 5, "M": 6, "N": 4, "O": 10, "P": 4, "Q":1, "R": 6, "S": 8, "T": 7, "U": 2, "V": 2, "X": 1, "Z": 1, "*": 3}


# distribuicao do valor em pontos das letras individuais


pontuacao_letras = {
    "A": 1, "B": 3, "C": 2, "Ç": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 5, "L": 2, "M": 1, "N": 3, "O": 1, "P": 2, "Q": 6, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "X": 8, "Z": 8
}

# funcoes basicas do jogo
# funcao que dispoe a mao inicial de sete letras do jogo


def mao_inicial():
    mao = []
    for i in range(7):
        letra = random.choice(list(distribuicao_letras.keys()))
        if distribuicao_letras[letra] > 0:
            distribuicao_letras[letra] -= 1
            mao.append(letra)
    return mao



# def mao_inicial():
#     mao = []
#     while len(mao) < 7:
#         letra = random.choice(list(distribuicao_letras.keys()))
#         if distribuicao_letras[letra] > 0:
#             distribuicao_letras[letra] -= 1
#             mao.append(letra)
#         return mao

# funcao que calcula a pontuacao da palavra

def calcula_pontos(palavra):
    placar = 0
    for letra in palavra:
        placar += pontuacao_letras[letra]
        return placar

# loop de jogo até o jogador decidir quitar com Q


while True:
    mao_jogador = mao_inicial()
    print("Sua Mão de 7 letras:", mao_jogador)
    palavra = input("Entre com uma palavra (ou apert 'q'para quitar):").upper()
    if palavra == "Q":
        break

# checando se as letras da palavra escolhida estao presentes na mão do hogador

    copia_mao = mao_jogador.copy()
    palavra_valida = True
    for letra in palavra:
        if letra in copia_mao:
            copia_mao.remove(letra)
        else:
            palavra_valida = False
            break
    if not palavra_valida:
        print("Palavra inválida. Tente novamente.")

    placar = calcula_pontos(palavra)
    print("Placar:", placar)

    # # atualiza a mao do johador com novas letras
    # novas_letras = mao_inicial()
    # mao_jogador += novas_letras
    # print("Nova mão:", mao_jogador)
