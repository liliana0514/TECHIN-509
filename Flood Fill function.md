def flood_fill(input_board, old, new, x, y):
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str]): The input board
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    def fill(x, y):
        # Check if the coordinates are within bounds and if the cell has the old value
        if 0 <= x < len(input_board) and 0 <= y < len(input_board[0]) and input_board[x][y] == old:
            # Replace the old value with the new value
            input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]
            # Recursively fill neighboring cells
            fill(x + 1, y)
            fill(x - 1, y)
            fill(x, y + 1)
            fill(x, y - 1)

    fill(x, y)
    return input_board

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


modified_board = flood_fill(input_board=board, old=".", new="~", x=2, y=21)

for a in modified_board:
    print(a)
