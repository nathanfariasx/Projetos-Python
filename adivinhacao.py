print('Bem-vindo(a) ao Jogo da Adivinhação!\n\n')

import random

secret_number = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print('Defina o nível de didiculdade: (1) Fácil, (2) Médio , (3) Difícil')
nivel = int(input('Digite o nível: '))

if nivel == 1:
  total_de_tentativas = 20
elif nivel == 2:
  total_de_tentativas = 10
elif nivel == 3:
  total_de_tentativas = 5
else:
  print('Digite 1,2 ou 3.')
   

for rodada in range(1, total_de_tentativas+1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input("Digite um número entre 1 e 100: \n"))

    if(chute<1 or chute>100):
      print("você deve digitar um número entre 1 e 100!\n")
      continue

    acertou = secret_number == chute
    maior = chute > secret_number
    menor = chute < secret_number

    if (acertou):
        print(f'Você acertou e fez {pontos} pontos!')
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.\n")
            pontos_perdidos = abs(secret_number - chute)
            pontos -= pontos_perdidos 
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.\n")
            pontos_perdidos = abs(secret_number - chute)
            pontos -= pontos_perdidos 
          
print("Fim do jogo!")
