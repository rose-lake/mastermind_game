import random

class Game:

    MAX_TURNS = 10
    COLOR_CODES = {
        'R': '\u001b[41m',
        'O': '\u001b[101m',
        'Y': '\u001b[103m',
        'G': '\u001b[42m',
        'B': '\u001b[44m',
        'P': '\u001b[105m',
    }
    TEXT_RESET = '\u001b[0m'
    UNICODE_BOX = '\u2588'
    BLACK_TEXT = '\u001b[30m'

    def __init__(self):
        self.sequence = self.generate_secret()
        self.turn = 0
        self.inexact_match = 0
        self.exact_match = 0


    def generate_secret(self):
        colors = ['R', 'O', 'Y', 'G', 'B', 'P']
        sequence = []

        while len(sequence) < 4:
            color_index = random.randint(0, 5)
            sequence.append(colors[color_index])

        return sequence

    def check_move(self, move):
        # move is a list of 4 characters :: R | O | Y | G | B | P
        # returns a list of UP TO 4 characters :: B for exact match | W for inexact match

        temp_secret = self.sequence.copy()
        exact_match_colors = []

        for index, color in enumerate(move):

            if color in temp_secret:
                if color == temp_secret[index]:
                    self.exact_match += 1
                    exact_match_colors.append(color)
        [temp_secret.remove(color) for color in exact_match_colors]
        [move.remove(color) for color in exact_match_colors]

        # by this point, all exact matches are removed from both temp_secret and move
        # now, check for inexact matches.
        for color in move:
            if color in temp_secret:
                self.inexact_match += 1
                temp_secret.remove(color)

        check_result = f'You have {self.exact_match} exact matches, and {self.inexact_match} inexact matches!'
        print(check_result)

    def has_won(self):
        if self.exact_match is 4:
            return True

        # reset our counters, as they are PER MOVE
        self.exact_match = 0
        self.inexact_match = 0
        return False

    def take_move(self):
        guess_is_not_valid = True

        while guess_is_not_valid:
            move = input('What is your guess? (Select 4 colors, '
                            + f'{self.COLOR_CODES["R"]}{self.BLACK_TEXT}R{self.TEXT_RESET}'
                            + ' | '
                            + f'{self.COLOR_CODES["O"]}{self.BLACK_TEXT}O{self.TEXT_RESET}'
                            + ' | '
                            + f'{self.COLOR_CODES["Y"]}{self.BLACK_TEXT}Y{self.TEXT_RESET}'
                            + ' | '
                            + f'{self.COLOR_CODES["G"]}{self.BLACK_TEXT}G{self.TEXT_RESET}'
                            + ' | '
                            + f'{self.COLOR_CODES["B"]}{self.BLACK_TEXT}B{self.TEXT_RESET}'
                            + ' | '
                            + f'{self.COLOR_CODES["P"]}{self.BLACK_TEXT}P{self.TEXT_RESET}'
                            + ', separated by spaces):\n')
            move_list = move.upper().strip().split(' ')
            if len(move_list) is 4:
                self.turn += 1
                guess_is_not_valid = False

        self.check_move(move_list)

    def display_final_sequence(self):
        render_string = ''
        for color in self.sequence:
            render_string += f'{self.COLOR_CODES[color]}{self.BLACK_TEXT}{color}{self.TEXT_RESET} '
        return f'{render_string}'

    def run_game(self):
        # for game testing purposes!!
        # print(self.sequence)
        print('Welcome to MASTERMIND! Created by Sara and Ksenia :)')
        while True:
            self.take_move()
            if self.has_won():
                print('Congratulations! You won! '
                      + f'{self.display_final_sequence()} !')
                break
            if self.turn is self.MAX_TURNS:
                print(f'Sorry, game over. The correct sequence was {self.display_final_sequence()}')
                break
            print(f'You have {(self.MAX_TURNS - self.turn)} moves left!')
