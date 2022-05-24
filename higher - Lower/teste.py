import random
import time
from art import data,logo, vs

def format_data(account):
    # Format account data into printable format
    nome = account['name']
    descrição = account['description']
    lugar = account['country']
    return f'{nome}, a {descrição}, from {lugar} '

def checkAnswer(guess, seguidores_A,seguidores_B):
    if seguidores_A > seguidores_B:
        return guess == 'A'
    else:
        return guess == 'B'
            
game_continue = True
score = 0
print(logo)
account_b = random.choice(data)
            
# Make game repeatable.
while game_continue:
    # Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f'Compare A: {format_data(account_a)} ')
    print(vs)
    print(f'Contra B: {format_data(account_b)} ')

    # Ask user for a guess.
    time.sleep(2)
    guess = input('QUEM VOCE ACHA QUE É MAIS FAMOSO? [A/B]').upper()

    # Check if user is correct.
    seguidores_A = account_a['follower_count']
    seguidores_B = account_b['follower_count']

    is_correct = checkAnswer(guess, seguidores_A,seguidores_B)            
    
    # Feedback.
    if is_correct:
        score = score + 1
        print('================================')
        print(f'\n\nVOCE ACERTOU! Seu score atual é {score} ')
    else:
        game_continue = False
        print(f'\nVoce errou, seu score foi {score} ')




# Make B become the next A.

# Add art.

# Clear screen between rounds.