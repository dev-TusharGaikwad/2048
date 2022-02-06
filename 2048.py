import os
import random
import keyboard
import json
score=[0]
peak=2048
def display(mat,n):
    global peak,score
    os.system('clear')
    print(' *****2048****')
    flag=True
    win=False
    for i in range(n):
        for j in range(n):
            if mat[i][j]==0:
                flag=False
            if mat[i][j]==peak:
                win=True
            if mat[i][j]==0:
                print('_',end='     ')
            else:
                print(mat[i][j],end=' '*(6-len(str(mat[i][j]))))
        print('\n')
    try:
        highscore=json.load(open('highscore.json'))
    except:
        f=open('highscore.json','w')
        json.dump(0,f)
        highscore=0
    if score[0]>highscore:
        highscore=score[0]
        with open("highscore.json", "w") as write_file:
            json.dump(score[0], write_file)
    print('SCORE is:',score[0],'HighScore is:',highscore)
    if win:
        restart('win')
    if flag:
        check_game_over(mat,n)
    
def check_game_over(mat,n):
    temp=[[mat[i][j] for j in range(n)]for i in range(n)]
    # print('game over called')
    if(left(temp,n,check=True)==False and right(temp,n,check=True)==False and top(temp,n,check=True)==False and down(temp,n,check=True)==False):
        restart('loose')
def restart(param):
    if param=='loose':
        print('Better luck next time....')
    if param=='win':
        print('Congratulations!!!! you win 2048')
    print('Enter y to restart, n to close')
    ip=input()
    if ip=='n':
        exit()
    os.system('python 2048.py')


def randnum(mat,n):
    lst=[]
    for i in range(n):
        for j in range(n):
            if mat[i][j]==0:
                lst.append([i,j])
    if len(lst)==0:
        display(mat,n)
        check_game_over(mat,n)
        return
    else:
        row,col=lst[random.randint(0,len(lst)-1)]
        mat[row][col]=random.choice([2,4])
    display(mat,n)

def left(mat,n,check=False):
    global score
    changes=False
    for row in range(n):
        for c1 in range(n):
            for c2 in range(c1+1,n):
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
def top(mat,n,check=False):
    global score
    changes=False
    for col in range(n):
        for r1 in range(n-1):
            for r2 in range(r1+1,n):
                if mat[r1][col]!=mat[r2][col] and mat[r1][col]!=0 and mat[r2][col]!=0:
                    break
                if mat[r1][col]==mat[r2][col] and mat[r2][col]!=0:
                    mat[r1][col]*=2
                    mat[r2][col]=0
                    if not check:
                        score[0]+=mat[r1][col]
                    changes=True
                    break
                elif mat[r1][col]==0 and mat[r2][col]!=0:
                    mat[r1][col]=mat[r2][col]
                    mat[r2][col]=0
                    changes=True
    return changes
def down(mat,n,check=False):
    global score
    changes=False
    for col in range(n):
        for r1 in range(n-1,-1,-1):
            for r2 in range(r1-1,-1,-1):
                if mat[r1][col]!=mat[r2][col] and mat[r1][col]!=0 and mat[r2][col]!=0:
                    break
                if mat[r1][col]==mat[r2][col] and mat[r2][col]!=0:
                    mat[r1][col]*=2
                    mat[r2][col]=0
                    if not check:
                        score[0]+=mat[r1][col]
                    changes=True
                    break
                elif mat[r1][col]==0 and mat[r2][col]!=0:
                    mat[r1][col]=mat[r2][col]
                    mat[r2][col]=0
                    changes=True
    return changes
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
if __name__=='__main__':
    main()
