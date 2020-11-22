import time
def main(arg, cells, position):
    try:
        print(time.ctime(int(arg[0])), end="")
    except Exception as e:
        print("Error: TIME::PRINT [TIMESTAMP]")
    return {"cells": cells, "position": position}