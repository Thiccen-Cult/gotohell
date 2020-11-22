import sys
def main(arg, cells, position):
    try:
        sys.stdout.write(str(position))
    except Exception as e:
        print("Error: VALUEOF [CELL NUMBER]")
    return {"cells": cells, "position": position}