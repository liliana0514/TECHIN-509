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

    # Implement your code here.


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

modified_board = flood_fill(input_board=board, old=".", new="~", x=1, y=1)

for a in modified_board:
    print(a)

# Expected output:
#~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~##########~~~~~~
#~~~~~~#........#~~~~~~
#~~~~~~#........#~~~~~~
#~~~~~~#........#####~~
#~~~~###............#~~
#~~~~#............###~~
#~~~~##############~~~~
