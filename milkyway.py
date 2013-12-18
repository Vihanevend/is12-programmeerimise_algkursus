import sys
from random import randint

def milkyway(x, y, txt):
        i = 0
        
        while i < 50:
                x = randint(0, 70)
                y = randint(0, 20)
                
                i = i + 1
                
                sys.stdout.write("\033[" + str(y)+ ";" + str(x) + "H" + txt)
                
milkyway (70, 20, "*")


