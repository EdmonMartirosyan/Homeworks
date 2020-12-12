# 1

# class User:
#     def __init__(self, name):
#         self.name = name
#     def send_message(self, user, message):
#         return f"you sent {message} to {user} user"
#     def post(self, message):
#         return "you posted"
#     def info(self):
#         return ""
#     def describe(self):
#         return self.name
#
#
# class Person(User):
#     def __init__(self, name, birthday):
#         super().__init__(name)
#         self.birthday = birthday
#     def info(self,):
#         return f"Your birthday is {self.birthday}"
#     def subscribe(self,user):
#         return f"You subscribed {user} user"
#
#
# class Community(User):
#     def __init__(self,name, description):
#         super().__init__(name)
#         self.description = description
#     def info(self):
#         return self.description


# 2

class TicTacToe:
    def __init__(self):
        self.new_game()
    def new_game(self):
        self.board = [[], [], []]
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                self.board[i].append("-")
    def get_field(self):
        print(self.board)
    def check_field(self):
        vertical_x = []
        vertical_o = []
        diagonal_x1 = 0
        diagonal_x2 = 0
        diagonal_o1 = 0
        diagonal_o2 = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "x":
                    vertical_x.append(j)
                    if self.board[i].count("x") == 3 or vertical_x.count(j) == 3:
                        return "x"
                    if i == j:
                        diagonal_x1 += 1
                    if i+j == 2:
                        diagonal_x2 += 1
                elif self.board[i][j] == "o":
                    vertical_o.append(j)
                    if self.board[i].count("o") == 3 or vertical_o.count(j) == 3:
                        return "o"
                    if i == j:
                        diagonal_o1 += 1
                    if i + j == 2:
                        diagonal_o2 += 1
        if diagonal_x1 == 3 or diagonal_x2 == 3:
            return "x"
        elif diagonal_o1 == 3 or diagonal_o2 == 3:
            return "o"
        for i in range(3):
            if "-" in self.board[i]:
                return None
        return "D"
    count = 0
    def make_move(self, row, col):
        global count
        if self.board[row-1][col-1] == "x" or self.board[row-1][col-1] == "o":
            print(f"Cell {row}, {col} is already filled")
        if TicTacToe.count < 9 and TicTacToe.count % 2 == 0:
            self.board[row-1][col-1] = "x"
            TicTacToe.count += 1
        elif TicTacToe.count < 9 and TicTacToe.count % 2 == 1:
            self.board[row-1][col-1] = "o"
            TicTacToe.count += 1
        if self.check_field() == "x":
            print("X-player won!", "Game over", sep="\n")
        elif self.check_field() == "0":
            print("O-player won!", "Game over", sep="\n")
        elif self.check_field() == "D":
            print("Draw", "Game over", sep="\n")
        else:
            print("Continue playing")

a = TicTacToe()
a.make_move(1, 1)
a.make_move(2, 1)
a.make_move(2, 2)
a.make_move(3, 3)
a.make_move(1, 3)
a.make_move(1, 2)
a.make_move(3, 2)
a.make_move(3, 1)
a.make_move(2, 3)
a.get_field()