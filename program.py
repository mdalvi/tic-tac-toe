import random


def replay():
    # usage of startswith method on input()
    return input('Do you wish to play again? Yes or No: ').upper().startswith('Y')


def choose_first():
    return random.randint(0, 1)


def check_winner(board):
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combos:
        if (board[combo[0]] == board[combo[1]] and board[combo[0]] == board[combo[2]] and board[combo[1]] == board[
            combo[2]] and (board[combo[0]] != ' ' and board[combo[1]] != ' ' and board[combo[2]] != ' ')):
            return True
    return False


def validate_user_input(board):
    while True:
        user_input = input('Please enter the input location: ')
        if len(user_input) != 1 or not user_input.isdigit():
            print('Unexpected input. Please enter valid location between 0 to 8.')
            continue

        user_input = int(user_input)
        if user_input < 0 or user_input > 8:
            print('Unexpected input. Please enter valid location between 0 to 8.')
            continue

        if board[user_input] != ' ':
            print('Unexpected input. Please enter value of playable <blank> location.')
            continue
        return user_input


def start_game():
    while True:
        moves = 0
        actions = ('X', 'O')  # this is a tuple, immutable (since only two actions exist)
        board = list(range(9))
        display_board(board)
        board = [' '] * 9
        action_flag = choose_first()
        print('{0} starts the game.'.format(actions[action_flag]))
        while True:
            print('{0} is playing...'.format(actions[action_flag]))
            # validate input data
            user_input = validate_user_input(board)
            board[user_input] = actions[action_flag]
            if check_winner(board):
                display_board(board)
                print('{0} wins the game. Game over.'.format(actions[action_flag]))
                break
            action_flag += 1
            if (action_flag > 1):
                action_flag = 0
            moves += 1
            display_board(board)
            if moves == 9:
                print("It's a tie. Game over.")
                break
        if not replay():
            break


def display_board(board):
    print('-------------')
    print('| {0} | {1} | {2} |'.format(board[0], board[1], board[2]))
    print('| {0} | {1} | {2} |'.format(board[3], board[4], board[5]))
    print('| {0} | {1} | {2} |'.format(board[6], board[7], board[8]))
    print('-------------')


print('Welcome To Simple Tic-Tac-Toe')
print('Author: milind.dalvi@turingequations.com')
start_game()
