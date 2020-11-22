import sys
def main(arg, cells, position):
    before = position
    try:
        position = int(arg[0])
    except Exception as e:
        print(f"Error: MOVETO [CELL NUMBER]")
        return {"cells": cells, "position": before}
    return {"cells": cells, "position": position}
