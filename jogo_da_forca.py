#jogo da forca em python

import random 
#palavras para o jogo da forca

palavras = ["python", "programacao", "desenvolvimento", "jogo"]

#selecionando uma palavra aleatória
palavra_secreta = random.choice(palavras)
#variável para armazenar as letras adivinhadas
letras_adivinhadas = []
#variável para contar o número de tentativas
tentativas = 6 
#loop principal do jogo
while tentativas > 0:
    #exibindo a palavra com letras adivinhadas e sublinhados para as letras não adivinhadas
    palavra_exibida = ""
    for letra in palavra_secreta:
        if letra in letras_adivinhadas:
            palavra_exibida += letra + " "
        else:
            palavra_exibida += "_ "
    print(palavra_exibida)

    #solicitando ao usuário uma letra
    letra_usuario = input("Digite uma letra: ").lower()

    #verificando se a letra já foi adivinhada
    if letra_usuario in letras_adivinhadas:
        print("Você já adivinhou essa letra. Tente outra.")
        continue

    #adicionando a letra à lista de letras adivinhadas
    letras_adivinhadas.append(letra_usuario)

    #verificando se a letra está na palavra secreta
    if letra_usuario in palavra_secreta:
        print("Boa! Você acertou uma letra.")
    else:
        tentativas -= 1
        print(f"Letra incorreta. Você tem {tentativas} tentativas restantes.")

    #verificando se o jogador ganhou
    if all(letra in letras_adivinhadas for letra in palavra_secreta):
        print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
        break
else:    print(f"Game Over! A palavra secreta era: {palavra_secreta}")  

