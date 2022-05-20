import time
import random
from hangman_art import stages,logo,word_list

lives = 6

chosen_word = random.choice(word_list)

print(logo)
print('Palavra:', chosen_word)

# Tracinho do jogo da forca
display_forca = []
for x in range(len(chosen_word)):
    display_forca.append('_')

time.sleep(1)

game_over = False

# Game
while not game_over:
    palavra = input('Chute uma letra: ').lower()
    time.sleep(1)
    
    for i in range(len(chosen_word)):
        if palavra in chosen_word[i]:
            display_forca[i] = palavra

    # Numero de vidas
    if palavra not in chosen_word:
        lives = lives - 1
        print('Wrong')
        print(f'Seu numero de vidas é {lives}')
        if lives == 0:
            print('Voce perdeu')
            game_over = True
    print(stages[lives])
    print(display_forca)

    # End Game
    if '_' not in display_forca:
        print('VOCE GANHOU!!!')
        game_over = True
