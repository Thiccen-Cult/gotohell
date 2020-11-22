import sys
def main(arg, cells, position):
    try:
        sys.stdout.write(' '.join(arg))
    except Exception as e:
        print(f"Unkown Error [{e}]")
    return {"cells": cells, "position": position}