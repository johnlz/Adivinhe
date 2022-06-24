# Instalando dependências
 
from random import randint

print(' Adivinhe o Número ! ')

# Configuração

random = randint(0, 20)  # definindo o número aleatório de 0 a 20
chute = 0;  # definindo os chutes
chances = 6; # definindo a quantidade de chances

# inicio do Game

while chute != random:
    chute = input('Chute um número entre 0 a 20: ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1  # a cada vez que o usuário erra ele perde uma chance
        if chute == random:
            print('')
            print('Parabéns, você acertou! O número era {} e você ainda tinha {} chances.'.format(random, chances)) # mensagem de vitória
            print('')
            break;
        else:
            print('')
            if chute > random:
                print('Você errou! Dica: É um número menor.')
            else:
                print('Você errou! Dica: É um número maior.')
            print('Você ainda possui {} chances.'.format(chances))
            print('')
        if chances == 0: # quando o contador de chances chega a zero automáticamente você está derrotado
            print('')
            print('Suas chances acabaram, você perdeu!') # mensagem após chegar ao final das suas tentativas
            print('')
            break;

# Fim do Game

print(' Fim do Game ')

