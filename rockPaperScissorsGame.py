import random

def play():
    choice_list = ['r','p','s']
    computer_choice = random.choice(choice_list)
    user_choice = input('Please select your choice. Press (R) for rock, (P) for paper, and (S) for scissors\n').lower()
    result = any(u_choice in user_choice for u_choice in choice_list)
    if result == False:
        print('Please select correct option \n')
        return play()
    # If user and computer has the same choice
    elif user_choice == computer_choice:
        return f'Tie! Your choice :{user_choice} ; Computer\'s choice: {computer_choice}'    
    #If user has won
    elif isWin(user_choice,computer_choice):
        return(f"You won! Your choice: {user_choice} ; Computer's choice: {computer_choice}")
    
    return f"You lost :( Your choice :{user_choice} ; Computer's choice: {computer_choice}"

def isWin(player,opponent):
    # s > p ; r > s ; p > r
    if (player == 's' and opponent == 'p') or (player == 'r' and opponent == 's') \
    or (player == 'p' and opponent == 'r'):
        return True

print(play())
