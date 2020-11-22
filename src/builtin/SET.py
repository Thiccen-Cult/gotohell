import sys
def main(arg, cells, position):
    try:
        cells[int(arg[0])] = int(arg[1])
    except Exception as e:
        print(f"Error: SET [CELL NUMBER] [VALUE]")
    return {"cells": cells, "position": position}