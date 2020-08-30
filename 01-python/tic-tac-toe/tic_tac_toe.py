import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

_WINNERS_COMB = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    for combination in _WINNERS_COMB:
      if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != None:
        self.winner = _PLAYER if self.board[combination[0]] == _PLAYER_SYMBOL else _MACHINE
        self.is_game_over = True
        return True
    return self.board.count(None) == 0

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    # TODO: Implement this function to make the machine choose a random cell (use random module)
    # The result of this function should be that self.board now has one more random cell occupied 
    rand = random.choice([x for x in range(len(self.board)) if self.board[x] is None])
    self.board[rand] = _MACHINE_SYMBOL

  def format_board(self):
    x=1
    for i in range(len(self.board)):
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            if i != 1: end+='---------\n'
        char=' '
        value=self.board[i]
        if value in (_MACHINE_SYMBOL, _PLAYER_SYMBOL): char=value
        x+=1
        print(char,end=end)

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    self.format_board()

  def print_result(self):
    # TODO: Implement this function in order to print the result based on the self.winner
    if self.winner is None:
      print("Draw")
    else:
      print("{} is the winner".format(self.winner))
  
