# added some docstrings here:

def flood_fill(input_board, old, new, x, y):

     # added assert statement here to ensure every row of the board is the same long
    row_length = len(input_board[0])
    assert all(len(row) == row_length for row in input_board)
    
    def fill(x, y):
        
         # this ensures the starting point(x,y) lies within the board boundary
        if 0 <= x < len(input_board) and 0 <= y < len(input_board[0]) and input_board[x][y] == old:

         # this replaces the characters at (x,y) with new characters
            input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]
           
           # this calls the fill function recursively and checks and changes the points around (x,y) 
            fill(x + 1, y)
            fill(x - 1, y)
            fill(x, y + 1)
            fill(x, y - 1)
            
    
    fill(x, y)
    return input_board

# I changed a board to test it and it works!

board = [
    "......#######.........",
    ".....##......##.......",
    ".....##........#......",
    ".....##........###....",
    ".....##...........##..",
    "....###............#..",
    "....################..",
    "......................",
]

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

