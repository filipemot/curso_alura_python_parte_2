def jogar():
    print('######################')
    print('Bem vindo ao jogo de forca')
    print('######################')

    palavra_secreta = "banana".lower()
    letras_acertadas = ["_" for _ in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while not enforcou and not acertou:
        chute = input("Qual letra?")
        chute = chute.strip().lower()

        index = 0
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += + 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do Jogo")


if __name__ == "__main__":
    jogar()
