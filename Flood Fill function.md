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
    # Check if the coordinates are within the board boundaries
    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]):
        return input_board

    # Check if the current cell has the old value
    if input_board[x][y] == old:
        # Replace the old value with the new value
        input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]

        # Recursively fill in neighboring cells
        flood_fill(input_board, old, new, x + 1, y)
        flood_fill(input_board, old, new, x - 1, y)
        flood_fill(input_board, old, new, x, y + 1)
        flood_fill(input_board, old, new, x, y - 1)

    return input_board

# Test cases
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

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=5)

for a in modified_board:
    print(a)

print(len(board))
print(len(board[0]))
