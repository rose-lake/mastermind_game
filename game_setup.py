import random

class Game:

    MAX_TURNS = 10

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
        for index, color in enumerate(move):
            print('** checking color ' + color)
            if color in self.sequence:
                print('** color ' + color + ' in sequence')
                if color == self.sequence[index]:
                    self.exact_match += 1
                    print('** exact match on index ' + str(index))
                else:
                    self.inexact_match += 1
                    print('** inexact match')
        
        check_result = f'{ "B" * self.exact_match }{"W" * self.inexact_match}'

        # check_result.append('B' * exact_match)        
        print(check_result)

        # return check_result

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
            move = input('What is your guess? (Select 4 colors, R | O | Y | G | B | P, separated by spaces):\n')
            move_list = move.upper().split(' ')
            if len(move_list) is 4:
                self.turn += 1
                guess_is_not_valid = False

        self.check_move(move_list)

    def run_game(self):
        print(self.sequence)

        while True:
            self.take_move()
            if self.has_won():
                print('Congratulations! You won!')
                break
            if self.turn is self.MAX_TURNS:
                print(f'Sorry, game over. The correct sequence was {self.sequence}')
                break
