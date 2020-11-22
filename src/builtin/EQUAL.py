import sys
def main(arg, cells, position):
    try:
        if str(arg[0]) == str(arg[1]).replace(" ", ""):
            cells[position] = 1
        else:
            cells[position] = 0
    except Exception as e:
        print("Error: EQUAL [VALUE] [VALUE]")
    return {"cells": cells, "position": position}