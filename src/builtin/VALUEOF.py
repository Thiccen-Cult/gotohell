import sys
def main(arg, cells, position):
    try:
        sys.stdout.write(str(cells[int(arg[0])]))
    except Exception as e:
        print("Error: VALUEOF [CELL NUMBER]")
    return {"cells": cells, "position": position}