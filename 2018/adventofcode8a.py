# NMB
# AoC 2018
# Problem 8a

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

def printNode(node):
    if node[1] == '0':
        return node[0]+str(node[4])
    else:
        output = node[0]+'-'+str(node[4]) + '\n'
        for child in node[3]:
            output += '\t'
            output += printNode(child)+'\n'
        return output

def sumMeta(node):    
    if node[1] == '0':
        return sum([int(x) for x in node[4]])
    else:
        total = 0
        for child in node[3]:
            total += sumMeta(child)
        return total + sum([int(x) for x in node[4]])        
    
numbers = open('puzzle_input_8.txt','r').read().split(' ')
head = []
labels = ord('A')
i = 0
while i < len(numbers):
    head = makeNode(i,i+1)
    i = head[0]
    node = head[1]
print(sumMeta(head[1]))
