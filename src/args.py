import getopt, sys, os

class Args:
    def __init__(self):
        self.rows = 30
        self.cols = 30
        self.init = 20
        self.speed= 1
        self.mode = 0
        self.kill = False
        self.info = False
        self.term = False
        self.local= False
        self.load = None

        arglist = sys.argv[1:]
        options = "r:c:i:s:d:p:l:f:kxth"
        long    = ["rows=", "columns=", "initial_life=", "size=", "delay=", "print=", "load=", "file=", "kill", "data", "termsize", "help"]

        try:
            args, _ = getopt.getopt(arglist, options, long)
            for i, v in args:
                if v: v = v
                if i in ("-r", "--rows")        : self.rows = int(v)
                if i in ("-c", "--columns")     : self.cols = int(v)
                if i in ("-i", "--initial_life"): self.init = int(v)
                if i in ("-d", "--delay")       : self.speed= int(v)
                if i in ("-p", "--print")       : self.mode = int(v)
                if i in ("-l", "--load")        : self.load = v
                if i in ("-s", "--size")        : self.cols, self.rows = int(v), int(v)
                if i in ("-f", "--file")        : self.local, self.load = True, v
                if i in ("-t", "--termsize")    : self.term = True
                if i in ("-k", "--kill")        : self.kill = True
                if i in ("-x", "--data")        : self.info = True
                if i in ("-h", "--help")        : self.print_help()

            if self.term:
                self.cols, self.rows = os.get_terminal_size()
                self.rows -= 2
                if self.mode == 0:                   self.rows *=  2
                elif not self.mode in (2,5,6,7,8,9): self.cols //= 2

        except getopt.error as error:
            os.system('echo -e "\033[?25h"')
            print(str(error))
            exit(1)
 
    def print_help(self):
        print(
"""Simulate Conway's Game of Life.

Usage: life [OPTIONS]
Example: life -kxs50 -i40

Options:
    -c, --columns\tColumns of the board. Default is 30.
    -d, --delay\t\tDelay time between generations in miliseconds. Default is 1.
    -f, --file\t\tLoad local CSV file as preset.
    -i, --initial_life\tHow much life appears in the first generation. Default is 20.
    -k, --kill\t\tIf the game enters a loop, exit.
    -l, --load\t\tLoad preset as initial configuration.
    -p, --print\t\tPrinting mode (0-12). Default is 0.
    -r, --rows\t\tRows of the board. Default is 30.
    -s, --size\t\tSize of the board in rows and columns.
    -t, --termsize\tAdjust the size to the terminal dimensions.
    -x, --data\t\tDisplay the amount of life and number of the generation.
    -h, --help\t\tShow this message!
  
Print modes:
    0\tTiny
    1\tSquares
    2\tHalf-width squares
    3\tReversed squares
    4\tChess
    5\tBinary
    6\tNon-binary
    7\tASCII (#)
    8\tASCII (@)
    9\tASCII (*)
    10\tGay
    11\tmeow :3
    12\t🥺

Default presets:
    glider    pentonimo   diehard acorn   snake   infinity1   infinity2
    gun       cloverleaf  ants    loss    amogus""")
        exit()
