import sys
class Game:
    def __init__(self):
        self.user1Name = ""
        self.user2Name = ""
        self.board = [
            '_', '_', '_',
            '_', '_', '_',
            '_', '_', '_',
            ]
        self.user1Turn = False
        self.user2Turn = False
        self.position = None
        self.won = None

    def displayBoard(self):
        print(self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print(self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print(self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def userInformation(self):
        self.user1Name = input('Name of the user 1 ? ')
        self.user2Name = input('Name of the user 2 ? ')

    def spacing(self):
        print()

    def goFirst(self):
        answer = input(str(self.user1Name) + " will go first(y/n)? ").lower()
        if answer == 'y':
            self.user1Turn = True
        elif answer == 'n':
            self.user2Turn = True
        else:
            print('Wrong input! please try again !')
            self.goFirst()

    def isFull(self):
        for i in self.board:
            if i == '_': return False
        return True

    def isPositionPacked(self,position):
        return not self.board[position-1] == '_'

    def insert(self):
        def innerMethod1():
            self.spacing()
            name = ''
            if self.user1Turn:
                name = self.user1Name
            elif self.user2Turn:
                name = self.user2Name
            print(name + '\'s turn')
            self.position = int(input('Position (1-9) ? '))
            if self.position not in range(1,10):
                print('Wrong position entry! Please try again!')
                innerMethod1()

        def innerMethod2():
            if self.isPositionPacked(self.position):
                print('Sorry Position ' + str(self.position) + ' is packed! try again!')
                innerMethod1()

        innerMethod1()
        innerMethod2()
        if self.user1Turn:
            self.board[self.position-1] = '*'
            self.user1Turn = False
            self.user2Turn = True
        elif self.user2Turn:
            self.board[self.position-1] = '$'
            self.user2Turn = False
            self.user1Turn = True
        self.displayBoard()

    def checkGame(self):
        self.won = None
        if self.checkRow() or self.checkColumn() or self.checkDiagonal():
            self.spacing()
            if self.won == '*':
                print('Congrats ' + self.user1Name + '. you have won the game')
            elif self.won == '$':
                print('Congrats ' + self.user2Name + '. you have won the game')
            sys.exit(0)

    def checkRow(self):
        if self.board[0] == self.board[1] == self.board[2] == self.board[0] != '_':
            self.won = self.board[0]
            return True
        elif self.board[3] == self.board[4] == self.board[5] == self.board[3] != '_':
            self.won = self.board[3]
            return True
        elif self.board[6] == self.board[7] == self.board[8] == self.board[6] != '_':
            self.won = self.board[6]
            return True
        return False

    def checkColumn(self):
        if self.board[0] == self.board[3] == self.board[6] == self.board[0] != '_':
            self.won = self.board[0]
            return True
        elif self.board[1] == self.board[4] == self.board[7] == self.board[1] != '_':
            self.won = self.board[1]
            return True
        elif self.board[2] == self.board[5] == self.board[8] == self.board[2] != '_':
            self.won = self.board[2]
            return True
        return False

    def checkDiagonal(self):
        if self.board[0] == self.board[4] == self.board[8] == self.board[0] != '_':
            self.won = self.board[0]
            return True
        elif self.board[2] == self.board[4] == self.board[6] == self.board[2] != '_':
            self.won = self.board[2]
            return True
        return False

    def startGame(self):
        self.userInformation()
        self.goFirst()
        self.displayBoard()
        while not self.isFull():
            self.insert()
            self.checkGame()
        self.spacing()
        print('Game Tied')
        
object = Game()
object.startGame()
