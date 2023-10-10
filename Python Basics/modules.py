import random

file_in_mile = 5280
meters_in_km = 1000
fruits = ["apple", "mango", "orange"]

def get_file_ext(filename) :
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1,num)