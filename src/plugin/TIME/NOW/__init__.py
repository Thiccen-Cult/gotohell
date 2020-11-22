import time
def main(arg, cells, position):
    try:
        cells[position] = int(time.time())
    except Exception as e:
        print("Error: TIME::SLEEP [SECONDS]")
    return {"cells": cells, "position": position}