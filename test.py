import pygame
import random

num = random.randint(0,1)

for i in range(10):
    if num:
        print('1: ')
        print(str(num))

    else:
        print('0: ')
        print(str(num))
