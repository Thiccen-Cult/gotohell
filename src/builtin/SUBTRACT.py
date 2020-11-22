def main(arg, cells, position):
    try:
        cells[position] = int(arg[0]) - int(arg[1])
    except Exception as e:
        print("Error: SUBTRACT [NUMBER 1] [NUMBER 2]")
    return {"cells": cells, "position": position}
