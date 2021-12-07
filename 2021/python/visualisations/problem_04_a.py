# NMB
# Advent of Code 2021
# Problem 04a

# NOTE: Will not run in IDLE! Please execute in Terminal/CMD to see output.

from rich import print
from time import sleep

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

def printBoards(boards, group, winner, winning_nums):    
    # print boards    
    for j in range(len(boards)//group):
        for r in range(5):
            for i in range(group*j,group*j+group):
            # print rows
                for n in range(5):
                    char = str(boards[i][r][n][0])
                    if len(char) == 1:
                        char = '0'+char
                    if boards[i][r][n][1] == 1:
                        if boards[i] == winner and int(char) in winning_nums:
                            print(char+' ',end='')
                        else:
                            print('[bold red]'+char+' [/bold red]',end='')
                    else:
                        print('[white]'+char+' [/white]',end='')
                print('  ',end='')
            print('')
        print('')    
    sleep(2)
    # end of print boards

# MAIN

lines = open('~/../../input_4.txt','r').read().splitlines()
nums = [int(n) for n in lines[0].split(',')]

boards = []
board = []
for line in lines[2:]:
    if line == '':
        boards.append(board)
        board = []
    else:
        board.append([[int(line[x*2+x:x*2+2+x]),0] for x in range(5)])        

group = 10
winner = board
winning_nums = []
for num in nums:
    c = 0    
    for board in boards:        
        for row in board:
            for n in row:
                if n[0] == num:
                    n[1] = 1
                    win = checkWin(board)
                    if win[0]:
                        winner = board
                        winning_nums = win[1]
                        #print(getScore(board,win[1],num))
                        break                           
            else:                
                continue
            break
        else:
            c += 1
            continue
        break
    else:
        print('BINGO NUMBER: [bold lightblue]'+str(num)+'[/bold lightblue]')
        printBoards(boards,group, winner, winning_nums)
        continue
    break
print('BINGO NUMBER: [bold lightblue]'+str(num)+'[/bold lightblue]')
printBoards(boards,group, winner, winning_nums)


    
        
                        
                        
                        
                        


            
    
        
                        

