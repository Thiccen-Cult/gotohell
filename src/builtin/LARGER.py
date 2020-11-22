import sys
def main(arg, cells, position):
    try:
        if int(arg[0]) > int(arg[1].replace(" ", "")):
            cells[position] = 1
        else:
            cells[position] = 0
    except Exception as e:
        print("Error: LARGER [VALUE] [VALUE]")
    return {"cells": cells, "position": position}