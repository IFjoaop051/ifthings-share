import platform
from sys import exit
from random import random
from subprocess import run as _exec

class Matrix:
    def __init__(self, value = None, rows: int = 2, cols: int = 2):
        self._arr = []
        self._rows = rows
        self._cols = cols

        for _ in range(0, rows):
            self._arr.append([None for __ in range(cols)])

        if value and not value is None:
            self.fill(value)

    def fill(self, value) -> None:
        for i in range(0, len(self._arr)):
                for j in range(0, len(self._arr[i])):
                    self._arr[i][j] = value

    def reset(self):
        self._arr = []

        for _ in range(0, self._rows):
            self._arr.append([None for __ in range(self._cols)])

    def remake(self, value):
        self.reset()
        self.fill(value)

    def dump(self) -> None:
        for i in range(0, len(self._arr)):
            print(f' {i + 1} ', end='')

            for j in range(0, len(self._arr[i])):
                print(f' {self._arr[i][j]}', end=(' |' if j < len(self._arr[i]) - 1 else ''))

            print('\n', end='')

            if i < len(self._arr) - 1:
                print('--+---' * len(self._arr[i]))

        print('\n')

    def map(self, func) -> None:
        for i in range(0, len(self._arr)):
            for j in range(0, len(self._arr[i])):
                self._arr[i][j] = func(self._arr[i][j], i, j)

    def copy(self):
        return self._arr.copy()

    @property
    def array(self) -> list[list]:
        return self._arr
    
    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols
    

READ_AS_INT = lambda prompt: int(input(prompt))

def main() -> None:
    GAME_BOARD = Matrix(rows=3, cols=3)
    GAME_BOARD.fill(' ')
    
    def _clear_window() -> None:
        _exec('cls' if platform.system() == 'Windows' else 'clear', shell=True)

        print('Jogo da Velha\n')
        print('Jogador 1: X')
        print('Jogador 2: O\n\n')

    def _print_board() -> None:
        print('    1 | 2 | 3\n', end='')
        GAME_BOARD.dump()

    print('Jogo da Velha\n')
    print('Jogador 1: X')
    print('Jogador 2: O\n\n')

    first_player_moves_count = second_player_moves_count = 0
    round = 'x' if random() > 0.5 else 'o'

    def _process_game_end() -> None:
        _clear_window()
        _print_board()

        print("Deu velha!")
        exit()
    
    def _check_winner() -> None:
        WINNING_COMBINATIONS = [
            # horizontal
            [0, 0], [0, 1], [0, 2],
            [1, 0], [1, 1], [1, 2],
            [2, 0], [2, 1], [2, 2],

            # vertical
            [0, 0], [1, 0], [2, 0],
            [0, 1], [1, 1], [2, 1],
            [0, 2], [1, 2], [2, 2],

            # diagonal
            [0, 0], [1, 1], [2, 2],
            [0, 2], [1, 1], [2, 0],
        ]

        for i in range(0, len(WINNING_COMBINATIONS), 3):
            [row1, col1] = WINNING_COMBINATIONS[i]
            [row2, col2] = WINNING_COMBINATIONS[i + 1]
            [row3, col3] = WINNING_COMBINATIONS[i + 2]

            if GAME_BOARD.array[row1][col1] == GAME_BOARD.array[row2][col2] == GAME_BOARD.array[row3][col3]:
                _clear_window()
                _print_board()

                print(f'Jogador {1 if round == "o" else 2} venceu!')
                exit()

    while True:
        _print_board()
        
        [row, col] = [
            READ_AS_INT(f'Jogador {1 if round == "x" else 2} [digite o número da linha]: ') - 1,
            READ_AS_INT(f'Jogador {1 if round == "x" else 2} [digite o número da coluna]: ') - 1,
        ]

        if not GAME_BOARD.array[row][col] in ['x', 'o', 'X', 'O']:
            GAME_BOARD.array[row][col] = round.upper()

            if round == 'x':
                first_player_moves_count += 1
            else:
                second_player_moves_count += 1

            round = 'o' if round == 'x' else 'x'

        _clear_window()
        _print_board()

        if first_player_moves_count >= 3 or second_player_moves_count >= 3:
            _check_winner()

        if (first_player_moves_count + second_player_moves_count) >= 9:
            _process_game_end()

if __name__ == '__main__':
    main()
