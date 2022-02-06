# **FrontEnd and Dashboard Developer**

## **2048 Game**

### **Language Used** : Python

### **Description** :
This game is simple replica of 2048 game. It is console based game developed in python.

### **Design Principles Used** :
1. **Data Structure** :
    1. List : Used to create a matrix of 4x4.
    2. File : Used to store the High Score in JASON format.

2. **Algorithm** :
    1. **Random Number Generator** : Randomly generates a number between 2 and 4. Also to select a random position in the matrix.

    2. **Check for the winning condition** : Checks if any of the cell contains number 2048.

    3. **Check for the losing condition** : Checks if the matrix is full and there is no place to move/shift the tiles.

    4. **Move the tiles** : Shifts the tiles in the matrix in the direction of the user input.

3. **User Interface** :
    1. **User Input** : User can input the direction of the tiles to be shifted.

    > Left : '1' or 'Left Arrow'  

    > Right : '2' or 'Right Arrow'

    > Up : '3' or 'Up Arrow'

    > Down : '4' or 'Down Arrow'

### **Thoughts / Probable solutions / Problems faced while designing the solution**

The original 2048 game is UI based game, so instead of using UI I decided to build console based game. Although it's Console based game but it was not easy to implement.

**Probable Solution** : By using the random number generator and checking for the winning condition, I was able to implement the game. Also to shift the tiles in the direction of the user input I have write four functions for left, right, top and down movement.

**Problems faced while designing the solution** :

While designing this game I faced the following problems :

1. While checking the Game Over condition there was a change in the original matrix, so to overcome that I have used a copy of the original matrix.

2. While shifting the tiles in the direction of the user input, if there is non-zero value between any two similar values in a same row/column the values were getting combined, this issue was solved by changing the conditions for swapping.

3. When the user entered choice to move tiles (s)he had to press the enter key after giving the input. So for that I have used *keyboard* module to get the input from the user without having to press enter.

***
### **Code Walkthrough** :

> import os

*import os* is used to clear the screen. by using function.
- > os.system('cls')

> import random

*import random* is used to generate random numbers from *list [2,4]* and also to select randon position in matrix.

> import keyboard

*import keyboard* is used to get the input from the user without having to press enter.

for this I have used following function.
> keyboard.add_hotkey('name_of_key', lambda: function_to_be_called())

To take the input to move the tiles.

> keyboard.wait('name_of_key')

To *exit* from the game.

> def display(mat, n)

this function is used to display the matrix and latest score.

    def display(mat, n)
        global peak
        os.system("clear")
        print(' *****2048****')
        flag = True
        win = False
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 0:
                    flag = False
                if mat[i][j] == peak:
                    win = True
                if mat[i][j] == 0:
                    print('_',end='     ')
                else:
                    print(mat[i][j], end=' ' * (6 - len(str(mat[i][j]))))
            print('\n')
        print('SCORE is:', score[0])
        if win:
            restart('win')
        if flag:
            check_game_over(mat, n)

> def check_game_over(mat, n)

This function is used to check if the game is over or not.

    def check_game_over(mat, n):
        temp = [[mat[i][j] for j in range(n)] for i in range(n)]
        if (left(temp, n) == False and right(temp, n) == False and top(temp, n) == False and down(temp, n) == False):
            restart('loose')

> def restart(param)

This function is used to restart the game 

    def restart(param):
        if param == 'loose':
            print('Better luck next time....')
        if param == 'win':
            print('Congratulations!!!! you win 2048')
        print('Enter y to restart, n to close')
        ip = input()
        if ip == 'n':
            exit()
        global mat
        mat = [[0, 0, 0, 0] for i in range(4)]
        print(mat)
        randnum(mat, 4)

> def randnum(mat, n)

This function is used to generate random number from a list [2,4] and also to select random position in matrix


    def randnum(mat, n):
        lst = []
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 0:
                    lst.append([i, j])
        if len(lst) == 0:
            display(mat, n)
            check_game_over(mat, n)
            return
        else:
            row, col = lst[random.randint(0, len(lst) - 1)]
            mat[row][col] = random.choice([2, 4])
        display(mat, n)

> def left(mat, n)

This function is used to move the tiles to left side of the matrix

    def left(mat, n):
        global score
        changes = False
        for row in range(n):
            for c1 in range(n):
                for c2 in range(c1 + 1, n):
                    if mat[row][c1] != mat[row][c2] and mat[row][c1] != 0 and mat[row][c2] != 0:
                        break
                    if mat[row][c1] == mat[row][c2] and mat[row][c1] != 0:
                        mat[row][c1] *= 2
                        mat[row][c2] = 0
                        score[0] += mat[row][c1]
                        highscore()
                        changes = True
                        break
                    elif mat[row][c1] == 0 and mat[row][c2] != 0:
                        mat[row][c1] = mat[row][c2]
                        mat[row][c2] = 0
                        changes = True
        return changes

> def top(mat, n)

This function is used to move the tiles in upword side of the matrix

    def top(mat, n):
        global score
        changes = False
        for col in range(n):
            for r1 in range(n - 1):
                for r2 in range(r1 + 1, n):
                    if mat[r1][col] != mat[r2][col] and mat[r1][col] != 0 and mat[r2][col] != 0:
                        break
                    if mat[r1][col] == mat[r2][col] and mat[r2][col] != 0:
                        mat[r1][col] *= 2
                        mat[r2][col] = 0
                        score[0] += mat[r1][col]
                        highscore()
                        changes = True
                        break
                    elif mat[r1][col] == 0 and mat[r2][col] != 0:
                        mat[r1][col] = mat[r2][col]
                        mat[r2][col] = 0
                        changes = True
        return changes

> def down(mat, n)

This function is used to move the tiles to down side of the matrix

    def down(mat, n):
        global score
        changes = False
        for col in range(n):
            for r1 in range(n - 1, -1, -1):
                for r2 in range(r1 - 1, -1, -1):
                    if mat[r1][col] != mat[r2][col] and mat[r1][col] != 0 and mat[r2][col] != 0:
                        break
                    if mat[r1][col] == mat[r2][col] and mat[r2][col] != 0:
                        mat[r1][col] *= 2
                        mat[r2][col] = 0
                        score[0] += mat[r1][col]
                        highscore()
                        changes = True
                        break
                    elif mat[r1][col] == 0 and mat[r2][col] != 0:
                        mat[r1][col] = mat[r2][col]
                        mat[r2][col] = 0
                        changes = True
        return changes

> def right(mat, n)

This function is used to move the tiles to right side of the matrix

    def right(mat,n,check=False):
        global score
        changes=False
        for row in range(n):
            for c1 in range(n-1,0,-1):
                for c2 in range(c1-1,-1,-1):
                    if mat[row][c1]!=mat[row][c2] and mat[row][c1]!=0 and mat[row][c2]!=0:
                        break
                    if mat[row][c1]==mat[row][c2] and mat[row][c1]!=0:
                        mat[row][c1]*=2
                        mat[row][c2]=0
                        if not check:
                            score[0]+=mat[row][c1]
                        changes=True
                        break
                    elif mat[row][c1]==0 and mat[row][c2]!=0:
                        mat[row][c1]=mat[row][c2]
                        mat[row][c2]=0
                        changes=True
        return changes

> def main()

The *main()* function act as driver code. In this method all functions are called.

    def main():
        n=4
        global score
        score[0]=0
        mat1=[[0 for i in range(n)]for j in range(n)]
        # mat1=[[1,2,3,4],[4,3,2,1],[1,2,3,4],[4,3,2,1]]
        randnum(mat1,n)
        randnum(mat1,n)
        keyboard.add_hotkey('up',lambda: (top(mat1,n),randnum(mat1,n)) )
        keyboard.add_hotkey('down',lambda: (down(mat1,n),randnum(mat1,n)))
        keyboard.add_hotkey('left',lambda: (left(mat1,n),randnum(mat1,n)))
        keyboard.add_hotkey('right',lambda: (right(mat1,n),randnum(mat1,n)))
        keyboard.add_hotkey('3',lambda: (top(mat1,n),randnum(mat1,n)) )
        keyboard.add_hotkey('4',lambda: (down(mat1,n),randnum(mat1,n)))
        keyboard.add_hotkey('1',lambda: (left(mat1,n),randnum(mat1,n)))
        keyboard.add_hotkey('2',lambda: (right(mat1,n),randnum(mat1,n)))
        keyboard.wait('space')

### **Scope of making this an 8x8 from 4x4** :

This game can be converted into 8x8 grid from 4x4 grid by changing the value of *variable n* and also by changing the *variable peak* we can also change the end number from 2048 to 4096.

## **CONTRIBUTERS** :

[Tushar Gaikwad](https://github.com/devSython)

## **Repository Link** :
    
[GitHub / 2048](https://github.com/devSython/2048)
