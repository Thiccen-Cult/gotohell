import sys
def main(arg, cells, position):
    try:
        cells[int(arg[1])] = int(arg[0])
    except Exception as e:
        print(f"Error: COPY [CELL NUMBER] [CELL NUMBER]")
    return {"cells": cells, "position": position}