import time
def main(arg, cells, position):
    try:
        time.sleep(int(arg[0]))
    except Exception as e:
        print("Error: TIME::SLEEP [SECONDS]")
    return {"cells": cells, "position": position}