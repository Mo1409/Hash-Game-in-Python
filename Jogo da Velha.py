matriz = [["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"]]
jogada = 1
empate = 0
for i in range(3):
    print(" ".join(matriz[i]))
while jogada < 2 and empate < 9:

    linha = int(input("Digite a linha: "))
    coluna = int(input("Digite a coluna: "))
    if linha > 2 or linha < 0 or coluna > 2 or coluna < 0 or matriz[linha][coluna] != '-':
        print('Posição inválida, tente novamente!')

    else:
        empate += 1
        if jogada == 1:
            matriz[linha][coluna] = "X"
        else:
            matriz[linha][coluna] = "O"
        jogada = jogada * -1
    for i in range(3):
        print(" ".join(matriz[i]))
    for n in range(3):
        if matriz[0][n] == matriz[1][n] and matriz[2][n] == matriz[0][n] and matriz[0][n] != '-':
            print(f'Parabéns o {"".join(matriz[0][n])} ganhou!')
            jogada = 2
        if matriz[n][0] == matriz[n][1] and matriz[n][2] == matriz[n][0] and matriz[n][0] != '-':
            print(f'Parabéns o {"".join(matriz[0][n])} ganhou!')
            jogada = 2
        if matriz[0][0] == matriz[1][1] and matriz[2][2] == matriz[1][1] and matriz[1][1] != '-':
            print(f'Parabens o {"".join(matriz[0][n])} ganhou!')
            jogada = 2
        if matriz[0][2] == matriz[1][1] and matriz[2][0] == matriz[1][1] and matriz[1][1] != '-':
            print(f'Parabéns o {"".join(matriz[0][n])} ganhou!')
            jogada = 2
if empate > 9:
    print('Empate!')