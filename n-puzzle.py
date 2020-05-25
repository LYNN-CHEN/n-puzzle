import random
from numpy import *

#Introduction for the game
print('-'*50)
print ('Welcome to 8 puzzle game.\nYou are supposed to move up, down, left, right to solve the puzzle.\nPlease follow the instruction to start the game.\n*Notice that 0 in the following puzzle represent the blank.')
print('-'*50)

#User Interaction
#Choose 8, 15 or quit the game
try:
    gameType = int(input('Please enter 1 for 8-puzzle, 2 for 15-puzzle or 3 to end the game:'))
    if gameType == 1 or gameType == 2:
        pass
    else:
        print("quit the game")
        exit()
except:
    print("invalid, quit the game")
    exit()

try:
    #Enter the direction
    left = str(input('Enter the one letter used for left directions:'))
    right = str(input('Enter the one letter used for right directions:'))
    up = str(input('Enter the one letter used for up directions:'))
    down = str(input('Enter the one letter used for down directions:'))
    if len(left)==1 and len(right)==1 and len(up)==1 and len(down) ==1:
        pass 
    else:
        ('please only enter one letter. quit.')
        exit()
except:
    print('Please follow the instructions!')


#Body Part (functions)
#define a function to get the position of 0
def findZero(n):
    for row in range(0,n):
        for column in range (0,n):
            if gameType == 1:
                if arrayForEight[row][column] == 0:
                    return row,column
            else:
                if arrayForFifteen[row][column] == 0:
                    return row,column


#define the moving function
#moving directions for 8
def moveUpForEight(zeroRow,zeroColumn):  
    if zeroRow != 0:
        arrayForEight[zeroRow][zeroColumn] = arrayForEight[zeroRow-1][zeroColumn]
        arrayForEight[zeroRow-1][zeroColumn] = 0
    return arrayForEight
def moveDownForEight(zeroRow,zeroColumn):    
    if zeroRow != 2:
        arrayForEight[zeroRow][zeroColumn] = arrayForEight[zeroRow+1][zeroColumn]
        arrayForEight[zeroRow+1][zeroColumn] = 0
    return arrayForEight
def moveLeftForEight(zeroRow,zeroColumn):
    if zeroColumn != 0:
        arrayForEight[zeroRow][zeroColumn] = arrayForEight[zeroRow][zeroColumn-1]
        arrayForEight[zeroRow][zeroColumn-1] = 0
    return arrayForEight
def moveRightForEight(zeroRow,zeroColumn,):
    if zeroColumn != 2:
        arrayForEight[zeroRow][zeroColumn] = arrayForEight[zeroRow][zeroColumn+1]
        arrayForEight[zeroRow][zeroColumn+1] = 0
    return arrayForEight
#move function for 8
def moveForEight(direction):
    if direction == left:
        arrayForEight = moveLeftForEight(zeroRow,zeroColumn)
        return arrayForEight
    elif direction == right:
        arrayForEight = moveRightForEight(zeroRow,zeroColumn)
        return arrayForEight
    elif direction == up:
        arrayForEight = moveUpForEight(zeroRow,zeroColumn)
        return arrayForEight
    elif direction == down:
        arrayForEight = moveDownForEight(zeroRow,zeroColumn)
        return arrayForEight
    else: return False
#moving directions for 15
def moveUpForFifteen(zeroRow,zeroColumn):  
    if zeroRow != 0:
        arrayForFifteen[zeroRow][zeroColumn] = arrayForFifteen[zeroRow-1][zeroColumn]
        arrayForFifteen[zeroRow-1][zeroColumn] = 0
    return arrayForFifteen
def moveDownForFifteen(zeroRow,zeroColumn):    
    if zeroRow != 3:
        arrayForFifteen[zeroRow][zeroColumn] = arrayForFifteen[zeroRow+1][zeroColumn]
        arrayForFifteen[zeroRow+1][zeroColumn] = 0
    return arrayForFifteen
def moveLeftForFifteen(zeroRow,zeroColumn):
    if zeroColumn != 0:
        arrayForFifteen[zeroRow][zeroColumn] = arrayForFifteen[zeroRow][zeroColumn-1]
        arrayForFifteen[zeroRow][zeroColumn-1] = 0
    return arrayForFifteen
def moveRightForFifteen(zeroRow,zeroColumn,):
    if zeroColumn != 3:
        arrayForFifteen[zeroRow][zeroColumn] = arrayForFifteen[zeroRow][zeroColumn+1]
        arrayForFifteen[zeroRow][zeroColumn+1] = 0
    return arrayForFifteen
#move function for 15
def moveForFifteen(direction):
    if direction == left:
        arrayForFifteen = moveLeftForFifteen(zeroRow,zeroColumn)
        return arrayForFifteen
    elif direction == right:
        arrayForFifteen = moveRightForFifteen(zeroRow,zeroColumn)
        return arrayForFifteen
    elif direction == up:
        arrayForFifteen = moveUpForFifteen(zeroRow,zeroColumn)
        return arrayForFifteen
    elif direction == down:
        arrayForFifteen = moveDownForFifteen(zeroRow,zeroColumn)
        return arrayForFifteen
    else: return False

#define the check result function
#check function for 8 puzzle
def checkForEight(arrayForEight):
    m = 0
    for i in range(3):
        for j in range(3):
            if arrayForEight[i][j] == originalArrayForEight[i][j]:
                m +=1
    if m == 9:
        return True
    else: return False
#check function for 15 puzzle    
def checkForFifteen(arrayForFifteen):
    m = 0
    for i in range(4):
        for j in range(4):
            if arrayForFifteen[i][j] == originalArrayForFifteen[i][j]:
                m +=1
    if m == 16:
        return True
    else: return False

#check and print available directions
def checkDirection(zeroRow,zeroColumn,directionAvailable,n):
    if zeroColumn != 0:
        directionAvailable.append(left)
    if zeroColumn != n-1:      #after correctness. before: n
        directionAvailable.append(right)
    if zeroRow != 0:
        directionAvailable.append(up)
    if zeroRow != n-1:
        directionAvailable.append(down)
    return directionAvailable

def printAvailable(directionAvailable,printList):
    print('The available directions are: ')
    if left in directionAvailable:
        printList.append('left -'+left)
    if right in directionAvailable:
        printList.append('right -'+right)
    if up in directionAvailable:
        printList.append('up -'+up)
    if down in directionAvailable:
        printList.append('down -'+down)
    print (printList)


#Initialization
#initial array
arrayForEight = array([[1,2,3],[4,5,6],[7,8,0]])    #8-puzzle
arrayForFifteen = array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])    #15-puzzle
originalArrayForEight = array([[1,2,3],[4,5,6],[7,8,0]])
originalArrayForFifteen = array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])

directions = [left,right,up,down]       #random direction from this list
countStep = 0       #count the steps
directionAvailable = []     #check the available directions
printList=[]

#Main
#if it is an eight-puzzle
if gameType == 1: 
    n=3
    i=0  
    while i <= 100:        #randomly move 0 for 100 times to create a solvable puzzle
        positionZero = findZero(n)      #get the position of zero
        zeroRow = positionZero[0]
        zeroColumn = positionZero[1]
        randomDirection = random.choice(directions)     #get a random direction
        arrayForEight = moveForEight(randomDirection)       #move 0 
        i +=1
    while checkForEight(arrayForEight)==False:
        positionZero = findZero(n)      #get the position of 0
        zeroRow = positionZero[0]
        zeroColumn = positionZero[1]
        print(arrayForEight)        #update the current array
        directionAvailable = checkDirection(zeroRow,zeroColumn,directionAvailable,n)        #find out the available directions
        printAvailable(directionAvailable,printList)
        direction = str(input('\nplease enter the moving direction:'))      #ask user to input the direction
        if direction in directionAvailable:
            arrayForEight = moveForEight(direction)
            countStep +=1
        else:
            print('Please enter an available direction')
        printList=[]        #empty the list for the next check
        directionAvailable = []     #empty the list for the next check 
    print(arrayForEight)
    print('Congratulations! You use',countStep, 'steps to solve the problem')
#if it is a 15-puzzle
else:
    n=4
    i=0  
    while i <= 100:        
        positionZero = findZero(n)
        zeroRow = positionZero[0]
        zeroColumn = positionZero[1]
        randomDirection = random.choice(directions)
        arrayForFifteen = moveForFifteen(randomDirection)
        i +=1   
    while checkForFifteen(arrayForFifteen)==False:
        positionZero = findZero(n)
        zeroRow = positionZero[0]
        zeroColumn = positionZero[1]
        print(arrayForFifteen)        
        directionAvailable = checkDirection(zeroRow,zeroColumn,directionAvailable,n)
        printAvailable(directionAvailable,printList)        
        direction = str(input('\nplease enter the moving direction:'))
        if direction in directionAvailable:
            arrayForFifteen = moveForFifteen(direction)
            countStep +=1
        else:
            print('Please enter an available direction')
        printList=[]        #empty the list for the next check
        directionAvailable = []     #empty the list for the next check 
    print(arrayForFifteen)
    print('Congratulations! You use',countStep, 'steps to solve the problem')