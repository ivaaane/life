import random, csv, os

class Game:
    def __init__(self, rows, cols, first_amount):
        self.matrix     = self.new_matrix(rows, cols, first_amount)
        self.rows       = rows
        self.cols       = cols
        self.generation = 0
        self.history    = []

    def new_matrix(self, rows, cols, first_amount):
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        thx, thy = cols // 3, rows // 3
        for _ in range(min(first_amount, thx * thy)):
            cell = 1
            x, y = 0, 0
            while cell == 1:
                x        = random.randrange(thx, thx * 2)
                y        = random.randrange(thy, thy * 2)
                cell     = matrix[y][x]
            matrix[y][x] = 1
        return matrix

    def neighbours(self, x, y):
        count = 0
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if i != y or j != x:
                    count += self.matrix[i][j]
        return count

    def new_generation(self):
        gen = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for y in range(1, self.rows - 1):
            for x in range(1, self.cols - 1):
                cell = self.neighbours(x, y)
                if cell == 3                           : gen[y][x] = 1
                if cell == 2 and self.matrix[y][x] == 1: gen[y][x] = 1
        self.matrix = gen
        self.generation += 1
    
    def get_life(self):
        life = 0
        for i in self.matrix:
            life += sum(i)
        return life
    
    def murder(self):
        self.history.append(self.get_life())
        if len(self.history) < 20:
            return
        self.history.pop(0)
        if len(set(self.history)) == 1:
            exit() 
    
    def load_preset(self, file):
        matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        try:
            with open(file, newline='') as csvfile:
                preset     = csv.reader(csvfile, delimiter=',')
                cols, rows = len(next(preset)), sum(1 for _ in preset)
                csvfile.seek(0)
                y = self.rows // 2 + rows // 2
                for i in preset:
                    x = self.cols // 2 - cols // 2
                    for j in i:
                        matrix[y][x] = int(j)
                        x += 1
                    y -= 1
            self.matrix = matrix

        except FileNotFoundError:
            os.system('echo -e "\033[?25h"')
            print("Pattern '" + file + "' doesn't exists!")
            exit(1)
        except IndexError:
            os.system('echo -e "\033[?25h"')
            print("Your terminal is too small to handle this preset!")
            exit(1)
        except UnicodeDecodeError:
            os.system('echo -e "\033[?25h"')
            print("Not a CSV file or invalid format!")
            exit(1)
        except:
            os.system('echo -e "\033[?25h"')
            print("Unrecognized error happpened. Exiting...")
            exit(1)