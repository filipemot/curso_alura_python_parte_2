def jogar():
    print('######################')
    print('Bem vindo ao jogo de forca')
    print('######################')

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Qual letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                print("Encontrei a letra {} na posicao {}".format(letra, index))
            index = index + 1

        print("jogando...")

    print("Fim do Jogo")


if __name__ == "__main__":
    jogar()
