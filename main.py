import os
from time import sleep
from src.game import Game
from src.args import Args
from src.display import Display

args = Args()
game = Game(args.rows, args.cols, args.init)
display = Display(game, args)

if args.load:
    if args.local:
        game.load_preset(args.load)
    else:
        game.load_preset(os.path.dirname(__file__) + "/presets/" + args.load + ".csv")
os.system('echo -e "\033[?25l"')

while True:
    try:
        display.display(game, args)
        sleep(args.speed / 10)
        game.new_generation()
        if args.kill:
            game.murder()

    except KeyboardInterrupt:
        os.system('echo -e "\033[?25h"')
        exit()
