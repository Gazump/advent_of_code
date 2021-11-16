# NMB
# AoC 2018
# Problem 8b

def makeNode(n,m):
    global labels
    node = []
    if numbers[n] == '0':
        meta = numbers[n+2:n+2+int(numbers[m])]                
        node = [chr(labels),numbers[n],numbers[m],[],meta]
        labels += 1
        return [2+int(numbers[m]),node]
    else:
        children = []
        offset = 0
        for i in range(int(numbers[n])):
            new_node = makeNode(n+2+offset,n+3+offset)
            offset += new_node[0]
            children.append(new_node[1])        
        meta = numbers[n+2+offset:n+2+offset+int(numbers[m])]
        node = [chr(labels),numbers[n],numbers[m],children,meta]
        labels += 1
        return[2 + int(numbers[m]) + offset, node]

def findValue(node):
    if node[1] == '0':
        return sum([int(x) for x in node[4]])
    else:
        total = 0
        for i in node[4]:
            if int(i) <= int(node[1]):
                new = findValue(node[3][int(i)-1])
                total += new                
        return total
    
numbers = open('puzzle_input_8.txt','r').read().split(' ')
head = []
labels = ord('A')

i = 0

while i < len(numbers):
    head = makeNode(i,i+1)
    i = head[0]

print(findValue(head[1]))
    

    
    
    
        







    
    

        
    
        




