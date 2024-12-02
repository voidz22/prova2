class Cavalo:
    def __init__(self, cor, idade, correr):
        self.cor = cor
        self.idade = idade
        self.correr = correr
    
    def correrr(self):
        print(f"O cavalo de {self.correr} 7 KM ")
lista = ["Ismael Laurentino", "Raul lucena"] 
  
ponei = Cavalo (cor = "preto", idade = "80 Anos", correr= "correu")
print("Seja bem vindo ao nosso código! o código foi feito por:")

for i in lista:
    print(i)

escolha = input("Digite 1 para o cavalo correr digite 2 pra mostrar a ficha do cavalo ")

if escolha == "1":
    ponei.correrr()

elif  escolha == "2":
    print(f"O cavalo tem {ponei.idade} e sua cor é {ponei.cor} ")

    