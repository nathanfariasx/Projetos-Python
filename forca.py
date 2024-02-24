def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


import random

print('******Bem-vindo(a) ao Jogo da Forca******\n')

arquivo = open("palavras.txt","r")
palavras = []

for linha in arquivo:
  linha = linha.strip()
  palavras.append(linha)

arquivo.close()

numero = random.randrange(0, len(palavras))
secret_word = palavras[numero].upper()


correct_letter = ['_' for letra in secret_word]

enforcou = False
acertou = False
erros = 0

print(correct_letter)

while not enforcou and not acertou:
  chute = input('\nDigite uma letra: ')
  chute = chute.strip().upper()

  if chute in secret_word:
     index = 0
     for letter in secret_word:
        if chute == letter:
            correct_letter[index] = letter
        index += 1
  else:
      erros += 1
      desenha_forca(erros)
    
  enforcou = erros == 7
  acertou = '_' not in correct_letter
  print(correct_letter)
  
if(acertou):
   print("Voce ganhou!")
else:
   print("Você perdeu!")


