import re

class BingoBoard:
    size = 5
    number_in_board = dict()
    already_won = list()
    def __init__(self, vals):
        self.board_row = [[0 for i in range(self.size)] for j in range(self.size)]
        self.board_col = [[0 for i in range(self.size)] for j in range(self.size)]
        self.board_val = vals #flat map
        self.board_dict = {val: (int(idx / self.size), idx % self.size) for idx, val in enumerate(vals)}
        self.populate_number_in_board()

    def populate_number_in_board(self):
        for num in self.board_val:
            if num in BingoBoard.number_in_board:
                BingoBoard.number_in_board[num].append(self)
            else:
                BingoBoard.number_in_board[num] = [self]

    def mark_selected_number(self, selected_number):
        if self in BingoBoard.already_won:
            return False
        x, y = self.board_dict[selected_number]
        self.board_row[x][y] = 1
        self.board_col[y][x] = 1
        if sum(self.board_row[x]) == self.size or sum(self.board_col[y]) == self.size:
            BingoBoard.already_won.append(self)
            return True
        return False

    def get_unmarked_numbers(self):
        unmarked_numbers = []
        for x, row in enumerate(self.board_row):
            for y, element in enumerate(row):
                if element == 0:
                    idx = (x * self.size) + y
                    unmarked_numbers.append(self.board_val[idx])

        return unmarked_numbers

input_file = 'day004.txt'

file_content = open(input_file, 'r').readlines()

bingo_seq_num = file_content.pop(0)
bingo_seq_num = [int(num) for num in bingo_seq_num.split(',')]
boards = []
board = []


for line in file_content:
    line = line.strip()

    if bool(re.search(r'\d', line)):
        line = line.split(' ')
        row = [int(val) for val in line if val != '']
        board.extend(row)

    if len(board) == 25:
        boards.append(BingoBoard(board))
        board = []

def play_bingo():
    for selected_num in bingo_seq_num:
        if selected_num not in BingoBoard.number_in_board:
            continue
        for board in BingoBoard.number_in_board[selected_num]:
            bingo = board.mark_selected_number(selected_num)
            if bingo:
                return selected_num, board

def play_bingo_till_last():
    last_won_selected_num = None
    last_won_board = None
    for selected_num in bingo_seq_num:
        if selected_num not in BingoBoard.number_in_board:
            continue
        for board in BingoBoard.number_in_board[selected_num]:
            bingo = board.mark_selected_number(selected_num)
            if bingo:
                last_won_selected_num = selected_num
                last_won_board = board

    return last_won_selected_num, last_won_board

# Part 1
selected_num, board = play_bingo()
unmarked_numbers = board.get_unmarked_numbers()
print(sum(unmarked_numbers) * selected_num)

# Part 2
l_selected_num, l_board = play_bingo_till_last()
unmarked_numbers = l_board.get_unmarked_numbers()
print(sum(unmarked_numbers) * l_selected_num)