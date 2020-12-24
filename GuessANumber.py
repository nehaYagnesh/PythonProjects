import random

def guess(highest_number):
    random_number = random.randint(1,highest_number)
    guess_number = 0
    
    while guess_number != random_number:
        try:
            guess_number = int(input(f'Guess a number between 1 and {highest_number}: '))
        except:
            if guess_number >= 0:
                print(f'Please enter a number.')
                continue
            
        if guess_number > highest_number:
                print(f'Please enter a number between 1 and {highest_number}')
        elif guess_number < random_number:
            print('Sorry, guess again. Too low!')
        elif guess_number > random_number:
            print('Sorry, guess again. Too high')
    print(f'Hurray! You guessed the number {guess_number} correctly!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if(low != high):
            guess_number = random.randint(low,high)
        else:
            guess_number = low # It doesn't matter whether it is high or low
        feedback = input(f'Is {guess_number} too high (H), too loo (L), or correct(C)??').lower()
        if feedback == 'h':
            high = guess_number - 1
        elif feedback == 'l':
            low = guess_number + 1
        elif feedback != 'c':
            print('Please enter (H) for too high, (L) for too low or (C) for correct number')
    print(f'Yay!! The computer guessed your number {guess_number} correctly')

#guess(20)
computer_guess(1000)