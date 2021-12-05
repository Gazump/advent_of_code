# NMB
# Advent of Code 2021
# Problem 04a

def getScore(board, nums, num):
    score = 0
    for row in board:
        for n in row:
            if n[1] == 0:
                score += n[0]
    score *= num
    return score        

def checkWin(board):
    for row in board:
        if sum([row[i][1] for i in range(5)]) == 5:        
            return [True,[row[i][0] for i in range(5)]]
    for c in range(len(board)):
        if sum([board[i][c][1] for i in range(5)]) == 5:        
            return [True,[board[i][c][0] for i in range(5)]]
    return [False,[]]

# MAIN

lines = open('input_4.txt','r').read().splitlines()
nums = [int(n) for n in lines[0].split(',')]

boards = []
board = []
for line in lines[2:]:
    if line == '':
        boards.append(board)
        board = []
    else:
        board.append([[int(line[x*2+x:x*2+2+x]),0] for x in range(5)])        

for num in nums:
    for board in boards:
        for row in board:
            for n in row:
                if n[0] == num:
                    n[1] = 1
                    win = checkWin(board)
                    if win[0]:
                        print(getScore(board,win[1],num))
                        break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break
    
        
                        
                        
                        
                        


            
    
        
                        

