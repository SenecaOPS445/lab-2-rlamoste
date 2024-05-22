#!/usr/bin/env python3
import sys

arguments = sys.argv
commandname = sys.argv[0]
name = str(sys.argv[1])
age = int(sys.argv[2])

#print(commandname, name, age)
print("Hi",name + ", you are",age ,"years old.")
