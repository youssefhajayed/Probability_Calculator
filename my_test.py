import prob_calculator
from unittest import main

Hat1 = prob_calculator.Hat(green=1, blue=2)
print(len(Hat1.contents))
print(Hat1.draw(3))
print(len(Hat1.contents))