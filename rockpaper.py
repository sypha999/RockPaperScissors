import random


def rps():
    # default list for cpu_choice
    possible_options = ['R', 'P', 'S']
    cpu_choice = random.choice(possible_options)
    # starting a loop to get user input
    while True:
        user_choice = input('Choose \'R\' for rock \'P\' for paper and \'S\' for scissors\n').upper()
        if (user_choice != "R") and (user_choice != 'P') and (user_choice != 'S'):
            print('Invalid Input Comrade\n')
        else:

            break
    if cpu_choice == user_choice:
        print('It\'s a tie, restarting game\n')
        rps()
    elif cpu_choice == 'R' and user_choice == 'P':
        print('Player(Paper):CPU(Rock)\n')
        print('Paper beats Rock\n')
        print('Player wins\n')
    elif cpu_choice == 'P' and user_choice == 'R':
        print('Player(Rock):CPU(Paper)\n')
        print('Paper beats Rock\n')
        print('CPU wins\n')
    elif cpu_choice == 'R' and user_choice == 'S':
        print('Player(Scissors):CPU(Rock)\n')
        print('Rock beats Scissors\n')
        print('CPU wins\n')
    elif cpu_choice == 'S' and user_choice == 'R':
        print('Player(Rock):CPU(Scissors)\n')
        print('Rock beats Scissors\n')
        print('Player wins\n')
    elif cpu_choice == 'P' and user_choice == 'S':
        print('Player(Scissors):CPU(Paper)\n')
        print('Scissors beats Paper\n')
        print('Player wins\n')
    elif cpu_choice == 'S' and user_choice == 'P':
        print('Player(Paper):CPU(Scissors)\n')
        print('Scissors beats Paper\n')
        print('CPU wins\n')
