import time, random
def main(arg, cells, position):
    try:
        cells[position] = random.randrange(0, int(time.time()))
    except Exception as e:
        print(f"Unkown error. [{e}]")
    return {"cells": cells, "position": position}