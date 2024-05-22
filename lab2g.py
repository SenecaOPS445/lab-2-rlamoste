#!/usr/bin/env python3

#Author: Renante Lamoste
#Author ID: rlamoste
#Date Created: 2024/05/22

import sys
arguments = sys.argv
commandname = sys.argv[0]

if len(sys.argv) == 1:
    timer = 3
elif len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    print("Usage:", sys.argv[0], "[timer]")
    sys.exit(1)

while timer > 0:
    print(timer)
    timer -= 1

print('blast off!')
