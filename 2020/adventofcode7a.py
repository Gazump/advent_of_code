# Boshoff
# advent of code 2020 - 7a

lines = open('puzzle_input_7.txt','r').read().splitlines()
bags = []

class Bag():
    def __init__(self,colour):
        self.colour = colour
        self.inner = []

def load_data():
    for line in lines:
        words = line.split(' ')
        bag = Bag(words[0]+words[1])
        for i in range(4,len(words),4):
            if words[i] != 'no':
                inner = Bag(words[i+1]+words[i+2])
                bag.inner.append(inner)
        bags.append(bag)

def contains(this_bag,goal_colour):
    for bag in bags:        
        if bag.colour == this_bag.colour:
            for inner in bag.inner:            
                if inner.colour == goal_colour:
                    return True
                elif contains(inner,goal_colour):
                    return True
            return False
    return False        

def search_bags(bags, goal_colour):
    c = 0
    for bag in bags:
        if contains(bag, goal_colour):
            c += 1
    return c

#MAIN
load_data()
print(search_bags(bags,'shinygold'))
