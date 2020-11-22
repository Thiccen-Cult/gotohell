import sys
def main(arg, cells, position):
    try:
        sys.stdout.write(chr(cells[position]))
    except Exception as e:
        print(f"Unkown Error [{e}]")
    return {"cells": cells, "position": position}