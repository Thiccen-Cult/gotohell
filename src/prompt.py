import main, sys
program = []
def prompt() -> None:
    global program
    NUM = 0
    PREFIX = f"{NUM} -> "
    while True:
        input_ = input(PREFIX)
        if input_:
            if input_.lower() == "run":
                GT = main.GotoHell('\n'.join(program))
                GT.split()
                GT.run(0)
            elif input_.lower().split(" ")[0] == "save":
                open(input_.split(" ")[1], "w+").write('\n'.join(program))
            elif input_.lower() == "new":
                NUM = 0
                program = []
            elif input_.lower() == "exit":
                sys.exit()
            else:
                NUM += 1
                program.append(f"#{NUM-1} {input_}") 
            PREFIX = f"{NUM} -> "


if __name__ == "__main__":
    prompt()