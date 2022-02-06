import os
import random
import keyboard

score = [0]
peak = 2048

# f = open('MaxScore.txt', 'r+')
# f.write("0")
# MaxScore = []

def highscore():
    # for s in f:
    #     MaxScore.append(int(x) for x in s.split())
    # if score[0] > MaxScore[0]:
    #     # f.truncate(0)
    #     f.write(str(score[0]))
    #     MaxScore.clear()        
    pass

def display(mat, n):
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


def check_game_over(mat, n):
    temp = [[mat[i][j] for j in range(n)] for i in range(n)]
    # print('game over called')
    if (left(temp, n) == False and right(temp, n) == False and top(temp, n) == False and down(temp, n) == False):
        restart('loose')


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


def right(mat, n):
    global score
    changes = False
    for row in range(n):
        for c1 in range(n - 1, 0, -1):
            for c2 in range(c1 - 1, -1, -1):
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


if __name__ == '__main__':
    n = 4
    mat1 = [[0 for i in range(n)] for j in range(n)]
    randnum(mat1, n)
    randnum(mat1, n)
    keyboard.add_hotkey('up', lambda: (top(mat1, n), randnum(mat1, n)))
    keyboard.add_hotkey('down', lambda: (down(mat1, n), randnum(mat1, n)))
    keyboard.add_hotkey('left', lambda: (left(mat1, n), randnum(mat1, n)))
    keyboard.add_hotkey('right', lambda: (right(mat1, n), randnum(mat1, n)))
    keyboard.add_hotkey('3', lambda: (top(mat1, n), randnum(mat1, n)))
    keyboard.add_hotkey('4', lambda: (down(mat1, n), randnum(mat1, n)))
    keyboard.add_hotkey('1', lambda: (left(mat1, n), randnum(mat1, n)))
    keyboard.add_hotkey('2', lambda: (right(mat1, n), randnum(mat1, n)))
    keyboard.wait('space')