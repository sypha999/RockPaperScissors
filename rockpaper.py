import random


def rps():
    # default list for cpu_choice
    possible_options = ['R', 'P', 'S']
    cpu_choice = random.choice(possible_options)
    # starting a loop to get user input
    while True:
        user_choice = input('\nChoose \'R\' for rock \'P\' for paper and \'S\' for scissors\n').upper()
        if (user_choice != "R") and (user_choice != 'P') and (user_choice != 'S'):
            print('\nInvalid Input Comrade\n')
        else:

            break
    if cpu_choice == user_choice:
        print('\nIt\'s a tie, restarting game\n')
        rps()
    elif cpu_choice == 'R' and user_choice == 'P':
        print('\nPlayer(Paper):CPU(Rock)\n')
        print('\nPaper beats Rock\n')
        print('\nPlayer wins\n')
    elif cpu_choice == 'P' and user_choice == 'R':
        print('\nPlayer(Rock):CPU(Paper)\n')
        print('\nPaper beats Rock\n')
        print('\nCPU wins\n')
    elif cpu_choice == 'R' and user_choice == 'S':
        print('\nPlayer(Scissors):CPU(Rock)\n')
        print('\nRock beats Scissors\n')
        print('\nCPU wins\n')
    elif cpu_choice == 'S' and user_choice == 'R':
        print('\nPlayer(Rock):CPU(Scissors)\n')
        print('\nRock beats Scissors\n')
        print('\nPlayer wins\n')
    elif cpu_choice == 'P' and user_choice == 'S':
        print('\nPlayer(Scissors):CPU(Paper)\n')
        print('\nScissors beats Paper\n')
        print('\nPlayer wins\n')
    elif cpu_choice == 'S' and user_choice == 'P':
        print('\nPlayer(Paper):CPU(Scissors)\n')
        print('\nScissors beats Paper\n')
        print('\nCPU wins\n')