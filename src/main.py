import sys, os, windows, unix
lines = {}
cells = {0: 0}
pos = 0
class GotoHell:
    def __init__(self, program: str) -> None:
        global lines, cells, pos
        self.program = program
        self.cells = cells
        self.lines = lines
        self.pos = pos
        self.os = "unix"
    def split(self) -> None:
        try:
            for i in self.program.split("\n"):
                if len(i.split()) > 0:
                    if not (i.split()[0].startswith("#")):
                        pass
                    elif i.split()[0].startswith("#"):
                        self.lines[int(i.split()[0].replace("#", ""))] = ' '.join(i.split()[1:])
        except Exception as e:
            pass

    def run(self, line: int) -> None:
        try:
            program = self.lines[line].split(".")
        except Exception as e:
            print(e)
        for i in program:
            try:
                method = i.split()[0]
                arguments = ' '.join(i.split()[1:]).split(",")
            except Exception as e:
                pass
            
            loop = -1
            for i in arguments:
                loop += 1
                arguments[loop] = arguments[loop].replace(" ", "")
                if arguments[loop].startswith("'") or arguments[loop].startswith("\""):
                    arguments[loop] = ''.join(arguments[loop][1:])
                    arr = []
                    for i in arguments[loop]:
                        arr += [ord(i)]
                    arguments[loop] = sum(arr)

                if "!" in arguments[loop]:
                    arguments[loop] = arguments[loop].replace("!", str(self.cells[self.pos]))
                if "?" in arguments[loop]:
                    arguments[loop] = arguments[loop].replace("?", str(self.pos))
                elif arguments[loop].startswith("@"):
                    arguments[loop] = self.cells[int(arguments[loop].replace("@",""))]    

                elif "->" in arguments[loop]:
                    _num = arguments[loop].split("->")
                    arguments = []
                    for i in range(int(_num[0]), int(_num[1])+1):
                        arguments.append(str(i))
                
                else:
                    pass
            if method == "GOTO":
                try:
                    self.run(int(arguments[0]))
                except RecursionError as e:
                    print("\n\nProgram ran into a recursion error. Stopping.")
                    sys.exit()
                except Exception as e:
                    print("Error: GOTO [LINE NUMBER]")

            elif method == "IF":
                try:
                    if self.cells[int(arguments[0])]:
                        self.run(int(arguments[1]))
                    else: 
                        self.run(int(arguments[2]))

                except RecursionError as e:
                    print("\n\nProgram ran into a recursion error. Stopping.")
                    sys.exit()
                except Exception as e:
                    print("Error: IF [CELL NUMBER] [LINE NUMBER] [LINE NUMBER]")

            elif method == "WHILE":
                try:
                    while self.cells[int(arguments[0])]:
                        self.run(int(arguments[1]))
                except RecursionError as e:
                    print("\n\nProgram ran into a recursion error. Stopping.")
                    sys.exit()
                except Exception as e:
                    print("Error: WHILE [CELL NUMBER] [LINE NUMBER]")

            elif method == "INPUT":
                if self.os == "unix":
                    self.cells[self.pos] = ord(unix._input())
                if self.os == "windows":
                    self.cells[self.pos] = ord(windows._input())
            elif method == "INTEGERINPUT":
                try:
                    if self.os == "unix":
                        self.cells[self.pos] = int(unix._input())
                    if self.os == "windows":
                        self.cells[self.pos] = int(windows._input())
                except Exception as e:
                    self.cells[self.pos] = 10
            else:
                try:
                    method = method.replace("::", ".")
                    builtin = __import__(f"builtin.{method}", fromlist=[method])
                    returned = builtin.main(arguments, self.cells, self.pos)
                    self.cells = returned["cells"]
                    self.pos = returned["position"]
                except Exception as e:
                    try:
                        method = method.replace("::", ".")
                        builtin = __import__(f"plugin.{method}", fromlist=[method])
                        returned = builtin.main(arguments, self.cells, self.pos)
                        self.cells = returned["cells"]
                        self.pos = returned["position"]
                    except Exception as e:
                        pass

if __name__ == '__main__':
    GT = GotoHell(open(sys.argv[1], "r").read())
    GT.split()
    GT.run(0)