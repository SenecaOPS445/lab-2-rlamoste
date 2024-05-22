#!/usr/bin/env python3
import sys

arguments = sys.argv
commandname = sys.argv[0]


if len(sys.argv) != 3:
    print("Usage:", commandname, "name age")
    sys.exit()

name = arguments[1]
age = arguments[2]

print("Hi",name + ", you are",age ,"years old.")

