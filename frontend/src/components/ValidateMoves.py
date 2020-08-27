class Piece:
#     Color: white = 1, black = -1
    color = 1
    row = 0
    column = 0
    hasMoved = False
    def __init__(self, color, row, column):
        self.color = color
        self.row = row
        self.column = column
        hasMoved = False
        
    def move(self, board, targetRow, targetColumn):
        if isValidMove(board, targetRow, targetColumn):
            board[targetRow][targetColumn] = board[row][column]
            board[row][column] = None
            row = targetRow
            column = targetColumn
        
    def isValidMove(self, board, targetRow, targetColumn):
        print("warning: using piece validMove method")
        return True
    
    def getColor(self):
        return self.color
    
    def getHasMoved(self):
        return hasMoved
    
    
class Pawn(Piece):
    def __str__(self):
        return "p" if self.color == 1 else "P"
    def isValidMove(self, board, targetRow, targetColumn):
#         Note: Color will be used to see which direction pawns move
#         Trying to take own piece
        if board[targetRow][targetColumn] != None and board[targetRow][targetColumn].getColor() == self.color:
            return False
        
        delta = [targetRow - self.row, targetColumn - self.column]
        
#         Forward movement
        if delta[1] == 0 and color == delta[0] * -1 and board[targetRow][targetColumn] == None:
            print(color, delta)
            return True
#         2x forward move
        if not self.hasMoved and delta[1] == 0 and 2 * color == delta[0] * -1:
            if board[self.row + color][self.column] == None and board[targetRow][targetColumn] == None:
                return True
#         Pawn taking piece
        if -1 * delta[0] == color and abs(delta[1]) == 1:
            print("Yo")
            if board[targetRow][targetColumn] != None and board[targetRow][targetColumn].getColor() == self.color * -1:
                return True
        
        return False    
class Rook(Piece):
    def __str__(self):
        return "r" if self.color == 1 else "R"
    def isValidMove(self, board, targetRow, targetColumn):
#         Piece trying to move to itself
        if self.row == targetRow and self.column == targetColumn:
            return False
#         Trying to take own piece
        if board[targetRow][targetColumn] != None and board[targetRow][targetColumn].getColor() == self.color:
            return False
        delta = [targetRow - self.row, targetColumn - self.column]
        
        if delta[0] * delta[1] != 0:
            return False
        xStep = 0 if delta[0] == 0 else abs(delta[0]) / delta[0]
        yStep = 0 if delta[1] == 0 else abs(delta[1]) / delta[1]
#         Collision detection
        location = [self.row + xStep, self.column + yStep]
    
        while location[0] != targetRow and location[1] != targetColumn:
            if board[location[0]][location[1]] != None:
                return False
            location[0] += xStep
            location[1] += yStep
        return True
                
class Knight(Piece):
    def __str__(self):
        return "n" if self.color == 1 else "N"
    def isValidMove(self, board, targetRow, targetColumn):
#         Trying to take own piece
        if board[targetRow][targetColumn] != None and board[targetRow][targetColumn].getColor() == self.color:
            return False
        delta = [targetRow - self.row, targetColumn - self.column]
        if delta[0] * delta[1] == 0:
            return False
        return abs(delta[0]) + abs(delta[1]) == 3
    
class Bishop(Piece):
    def __str__(self):
        return "b" if self.color == 1 else "B"
    def isValidMove(self, board, targetRow, targetColumn):
#         Piece trying to move to itself
        if self.row == targetRow and self.column == targetColumn:
            return False
#         Trying to take own piece
        if board[targetRow][targetColumn] != None and board[targetRow][targetColumn].getColor() == self.color:
            return False
        
        delta = [targetRow - self.row, targetColumn - self.column]
        if delta[0] != delta[1]:
            return False
        xStep = int(abs(delta[0]) / delta[0])
        yStep = int(abs(delta[1]) / delta[1])
#         Diagonal collision detection
        location = [self.row + xStep, self.column + yStep]
        
        while location[0] != targetRow and location[1] != targetColumn:
            if board[location[0]][location[1]] != None:
                return False
            location[0] += xStep
            location[1] += yStep
        return True
    
class Queen(Piece):
    def __str__(self):
        return "q" if self.color == 1 else "Q"
    def isValidMove(self, board, targetRow, targetColumn):
#         Piece trying to move to itself
        if self.row == targetRow and self.column == targetColumn:
            return False
#         Trying to take own piece
        if board[targetRow][targetColumn] != None and board[targetRow][targetColumn].getColor() == self.color:
            return False
        
        delta = [targetRow - self.row, targetColumn - self.column]
        if delta[0] != delta[1] and delta[0] * delta[1] != 0:
            return False
        xStep = 0 if delta[0] == 0 else int(abs(delta[0]) / delta[0])
        yStep = 0 if delta[1] == 0 else int(abs(delta[1]) / delta[1])
        location = [self.row + xStep, self.column + yStep]
        
        while location[0] != targetRow and location[1] != targetColumn:
            if board[location[0]][location[1]] != None:
                return False
            location[0] += xStep
            location[1] += yStep
        return True

    
class King(Piece):
    def __str__(self):
        return "k" if self.color == 1 else "K"
    def isValidMove(self, board, targetRow, targetColumn):
#         Trying to take own piece
        if board[targetRow][targetColumn] != None and board[targetRow][targetColumn].getColor() == self.color:
            return False
        delta = [targetRow - self.row, targetColumn - self.column]
        return abs(delta[0]) <= 1 and abs(delta[1]) <= 1

def tile64ToXY(tile):
    col = (tile - 1) % 8
    row = 7 - int((tile - 1) / 8)
    return [row, col]
    
def isWinner(board):
    isBlackKing = False
    isWhiteKing = False
    for row in range(8):
        for col in range(8):
            if isinstance(board[row][col], King):
                if board[row][col].getColor() == 1:
                    print("White")
                    isWhiteKing = True
                else:
                    print("Black")
                    isBlackKing = True
    if not isWhiteKing:
        return -1
    if not isBlackKing:
        return 1
    return 0