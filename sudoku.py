#sudoku


def find_empty_one(arr):
    #to find empty cells which are marked -1
    for i in range(9):
        for j in range(9):
            if arr[i][j] ==-1:
                return i,j
    
    return None, None
    
    
    

def if_valid(arr,x,y,guess):
    # to check if valid in rows and colomns
    for j in range(9):
        if j != y:
            if arr[x][j] == guess:
                return False
    
    for i in range(9):
        if i != x:
            if arr[i][y] == guess:
                return False
    
    for i in range((x//3)*3,((x//3)+1)*3):
        for j in range((y//3)*3,((y//3)+1)*3):
            if i!= x or j!= y:
                if arr[i][j] == guess:
                    return False
    
    return True

            
            
    
    
def solvesudo(sudoku):
    
    r,c = find_empty_one(sudoku) #choose an empty cell 
    
    if r is None:
        return True
    
    
    
    for i in range(1,10):
        #place a number between 1 to 9  and check if it is valid or not 
        if if_valid(sudoku,r,c,i):
            #if valid place the number in that cell
            sudoku[r][c] = i
            
            if solvesudo(sudoku): #nd recursively call the function 
                return True
        #if not is valid or not returnd true then we backtrack nd use diffrent number
        sudoku[r][c] = -1
    
    
    return False
    
    
#example   
arr = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]]

solvesudo(arr)

print(arr)
    
   
    
