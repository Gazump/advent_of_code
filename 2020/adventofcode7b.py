# Boshoff
# advent of code 2020 - 7b

lines = open('puzzle_input_7.txt','r').read().splitlines()
bags = []

class Bag():
    def __init__(self,colour,count):
        self.colour = colour
        self.inner = []
        self.count = count

def load_data():
    for line in lines:
        words = line.split(' ')
        bag = Bag(words[0]+words[1],1)
        for i in range(4,len(words),4):
            if words[i] != 'no':
                inner = Bag(words[i+1]+words[i+2],int(words[i]))
                bag.inner.append(inner)
        bags.append(bag)

def bag_count(this_bag):
    for bag in bags:
        # count this bag and it's inners
        if bag.colour == this_bag.colour:
            total = 0
            for inn in bag.inner:
                total += inn.count + inn.count * bag_count(inn)
            return total
        
#MAIN
load_data()
print(bag_count(Bag('shinygold',1)))











