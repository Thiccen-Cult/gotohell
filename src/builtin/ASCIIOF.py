import sys
def main(arg, cells, position):
    try:
        sys.stdout.write(chr(cells[int(arg[0])]))
    except Exception as e:
        print("Error: ASCIIOF [CELL NUMBER]")
    return {"cells": cells, "position": position}