#!/usr/bin/env python3

#Author: Renante Lamoste
#Author ID: rlamoste
#Date Created: 2024/05/22

import sys
args = sys.argv
commandname = sys.argv[0]

if len(sys.argv) != 2:
    print("Usage:", commandname, "timer")
    

timer = int(sys.argv[1])   
while timer != 0:
    print(timer)
    timer = timer - 1

print('blast off!')
