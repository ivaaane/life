import os

class Display:
    def __init__(self, game, args):
        self.game  = game
        self.args  = args
        self.rows  = game.rows
        self.cols  = game.cols
        self.matrix= game.matrix

    def display(self, game, args):
        self.game  = game
        self.args  = args
        self.rows  = game.rows
        self.cols  = game.cols
        self.matrix= game.matrix

        out = ""
        match self.args.mode:
            case 1: out = self.char ('██', '  ')
            case 2: out = self.char ('█', ' ')
            case 3: out = self.char ('  ', '██')
            case 4: out = self.chess()
            case 5: out = self.char ('1', '0')
            case 6: out = self.nb   ()
            case 7: out = self.char ('#', ' ')
            case 8: out = self.char ('@', ' ')
            case 9: out = self.char ('*', ' ')
            case 10:out = self.gay  ()
            case 11:out = self.char (':3', '  ')
            case 12:out = self.char ('🥺', '  ')
            case _: out = self.mini ()
        os.system("clear")
        if self.args.info:
            print("Life:", self.game.get_life(), "\tGeneration:", self.game.generation, end='')
        print(out)

    def char(self, full, empty):
        s = ""
        for y in range(self.rows):
            s += '\n'
            for x in range(self.cols):
                if self.matrix[y][x]: s += full
                else                : s += empty
        return s

    def chess(self):
        s = ""
        for y in range(self.rows):
            s += '\n'
            for x in range(self.cols):
                cell  = "  "          if self.matrix[y][x] == 0 else "\033[1;30m\u25D6\033[1;30m\u25D7"
                color = "\033[1;100m" if (x + y) % 2  == 0 else "\033[1;107m"
                s += f"{color}{cell}\033[0m"
        return s

    def mini(self):
        cells = {
            '00': ' ',
            '01': '▄',
            '10': '▀',
            '11': '█',
        }
        s = ""
        for y in range(0, self.rows, 2):
            s += '\n'
            for x in range(self.cols):
                cell = str(self.matrix[y][x]) + str(self.matrix[min(y + 1, self.rows - 1)][x])
                s += cells[cell]
        return s
    
    def nb(self):
        s = ""
        for y in range(1, self.rows - 1):
            s += '\n'
            for x in range(1, self.cols - 1):
                count = 0
                for i in range(y - 1, y + 2):
                    for j in range(x - 1, x + 2):
                        if i != y or j != x:
                            count += self.matrix[i][j]
                if count: s += str(count)
                else    : s += ' '
        return s

    def gay(self):
        rainbow = [
            '[1;35m',
            '[1;31m',
            '[38;5;214m',
            '[1;33m',
            '[1;32m',
            '[1;34m',
        ]
        s = ""
        for y in range(self.rows):
            s += '\n'
            for x in range(self.cols):
                color = rainbow[y % 6]
                if self.matrix[y][x]: s += f"\033{color}██\033[0m"
                else: s += "  "
        return s
