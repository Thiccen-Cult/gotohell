import sys
def main(arg, cells, position):
    try:
        loop = -1
        for i in arg:
            loop += 1
            arg[loop] = int(arg[loop])
        cells[position] = sum(arg)
    except Exception as e:
        print(f"Error: SUM *[NUMBER]")
    return {"cells": cells, "position": position}