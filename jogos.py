import forca
import adivinhacao
def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        forca.jogar()

if __name__ == "__main__":
    escolhe_jogo()