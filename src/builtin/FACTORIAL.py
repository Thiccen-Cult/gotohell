import sys
def main(arg, cells, position):
    try:
        loop = -1
        num = 1
        for i in arg:
            num *= int(i)
        cells[position] = num
    except Exception as e:
        print(f"Error: FACTORIAL *[NUMBER]")
    return {"cells": cells, "position": position}