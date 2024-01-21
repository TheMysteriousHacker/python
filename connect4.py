from time import *
from tkinter import *
import os
import tkinter.messagebox as box
from random import *
import sys
import winsound
import webbrowser
import subprocess

winbf = Tk()
winbf.iconbitmap(default='c4.ico')
winbf.title('Connect Four - By Uzair Arif')
winbf.resizable(0,0)
win = Frame(winbf)

#Connect Four
num = open('num.txt','r')
numread = num.read()
imgsetting = int(numread)
num.close()
o = 0
ai = 0
t = '1'
draw = 0
aimovenow = False
img = PhotoImage(file ='connect title.gif')
dot = PhotoImage(file='dot.gif')
board =[['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','','']]
def start():
    global status
    global starttimer
    status = Label(win, text='Please Wait...', font=('Calibri', 10 ,'italic'))
    for x in range(0,6):
        for y in range(0,7):
            board[x][y]=''
    status.grid(column=1,row=7,pady=(0,30))
    starttimer= time()
    win.after(1000,bconf)
def bconf():
    global t
    global aimovenow
    status.destroy()
    gameb.configure(text='Start New Game',state='normal')
    def later():
        t ='1'
        txt.configure(text="Your Turn")
        cnormal()
    if aimovenow == True:
        txt.configure(text= "Computer Turn")
        randc = randint(0,6)
        board[5][randc] = '2'
        global starttimer
        starttimer = time()
        win.after(500,later)
    conf()
def cnormal():
    c1.configure(state='normal')
    c2.configure(state='normal')
    c3.configure(state='normal')
    c4.configure(state='normal')
    c5.configure(state='normal')
    c6.configure(state='normal')
    c7.configure(state='normal')
def first():
    global t
    global txt
    global ai
    def first2():
        global starttimer
        starttimer = time()
        txtchg()
        cnormal()
    def first3():
        randc = randint(0,6)
        board[5][randc] = '2'
        conf()
        win.after(500,first2)
    if ai ==2:
        txt.configure(text= "Computer Turn")
        win.after(500, first3)
    else:
        win.after(500, first2)
def startanother():
    gameb.configure(text='Start New Game',state='disabled')
    global t
    global ai
    global draw
    global aimovenow
    draw = 0
    c1.configure(state='disabled')
    c2.configure(state='disabled')
    c3.configure(state='disabled')
    c4.configure(state='disabled')
    c5.configure(state='disabled')
    c6.configure(state='disabled')
    c7.configure(state='disabled')
    if ai != 0:
        sel = open('ai.txt','r')
        sel2 = sel.read()
        sel.close()
        if sel2 == '1':
            ai = 2
        else:
            ai = 1
    def normalize():
        t ='1'
        if ai == 0:
            txt.configure(text="Player "+ t +" Turn")
        else:
            txt.configure(text="Your Turn")
        cnormal()
    if ai == 2:
        ai = 1
        aimovenow = True
    else:
        aimovenow = False
        win.after(1000, normalize)
    start()
def txtchg():
    gameb.configure(text='Start New Game',state='normal', command=startanother)
    if ai == 0:
        txt.configure(text= "Player "+ t +" Turn")
    if ai == 1 or ai ==2:
        if t == '1':
            txt.configure(text= "Your Turn")
        else:
            txt.configure(text= "Computer Turn")
def playerchg():
    global t
    if ai == 0:
        if t == '1':
            t = '2'
        else:
            t = '1'
    else:
        if t == '1':
            t = '2'
            aimove()
        else:
            t = '1'

#Declaring Winner
def dec():
    global starttimer
    if draw == 1:
        txt.configure(text="Looks Like\nNo One Won")
        box.showinfo('Winner','Its A Draw...')
    else:
        global t
        txt.configure(text="Player "+ t +" Is\nThe Winner!!!")
        if t == '2':
            if ai == 1 or ai ==2:
                box.showinfo('Winner','Computer Won!')
            else:
                box.showinfo('Winner','Player 2 Has Won!')
        else:
            if ai == 1 or ai == 2:
                endtimer = time()
                totaltime = str(round(endtimer-starttimer))
                tcheck = int(totaltime)
                if os.path.isfile("best.txt"):
                    bestf = open('best.txt','r')
                    bestnum = bestf.read()
                    bestf.close()
                    if tcheck < int(bestnum):
                        bestnum = str(tcheck)
                        bestf = open('best.txt','w')
                        bestf.write(bestnum)
                        bestf.close()
                    box.showinfo('Winner','Player 1 Has Won!\nYou took ' + totaltime +' seconds; best: '+ bestnum +' seconds')
                else:
                    bestnum = str(tcheck)
                    bestf = open('best.txt','w')
                    bestf.write(bestnum)
                    bestf.close()
                    box.showinfo('Winner','Player 1 Has Won!\nYou took ' + totaltime +' seconds')

            else:
                box.showinfo('Winner','Player 1 Has Won!')
    c1.configure(state='disabled')
    c2.configure(state='disabled')
    c3.configure(state='disabled')
    c4.configure(state='disabled')
    c5.configure(state='disabled')
    c6.configure(state='disabled')
    c7.configure(state='disabled')
    def change():
        c1.configure(state='disabled')
        c2.configure(state='disabled')
        c3.configure(state='disabled')
        c4.configure(state='disabled')
        c5.configure(state='disabled')
        c6.configure(state='disabled')
        c7.configure(state='disabled')
        global t
        t = '1'
        def change2():
            global ai
            txt.configure(text="Player "+ t +" Turn")
            if ai == 2:
                    randc = randint(0,6)
                    board[5][randc] = '2'
            gameb.configure(text='Start New Game',state='normal')
            cnormal()
            bconf()
        global status
        gameb.configure(text='Start New Game',state='disabled')
        status = Label(win, text='Please Wait...', font=('Calibri', 10 ,'italic'))
        for x in range(0,6):
            for y in range(0,7):
                board[x][y]=''
        status.grid(column=1,row=7, pady=(0,30))
        win.after(1000,change2)
        global o
        o = 0
    gameb.configure(text='Start New Game',state='normal', command=change)
    
def check():
    global o
    global t
    for y in range(0,7):
        if board[0][y] != '':
            if y == 0:
                c1.configure(state='disabled')
            if y == 1:
                c2.configure(state='disabled')
            if y == 2:
                c3.configure(state='disabled')
            if y == 3:
                c4.configure(state='disabled')
            if y == 4:
                c5.configure(state='disabled')
            if y == 5:
                c6.configure(state='disabled')
            if y == 6:
                c7.configure(state='disabled')
    for r in range(5,-1,-1):
      for c in range(0,4):
        if o == 0:
          if board[r][c] == t:
            if board[r][c+1] == t:
                if board[r][c+2] == t:
                    if board[r][c+3] == t:
                        dec()
                        o = 1
    for r in range(0,3):
      for c in range(0,7):
        if o ==0:
          if board[r][c] == t:
            if board[r+1][c] == t:
                if board[r+2][c] == t:
                    if board[r+3][c] == t:
                        dec()
                        o = 1
    for r in range(0,3):
      for c in range(0,4):
        if o == 0:
          if board[r][c] == t:
            if board[r+1][c+1] == t:
                if board[r+2][c+2] == t:
                    if board[r+3][c+3] == t:
                        dec()
                        o = 1
    for r in range(0,3):
      for c in range(6,2,-1):
        if o == 0:
          if board[r][c] == t:
            if board[r+1][c-1] == t:
                if board[r+2][c-2] == t:
                    if board[r+3][c-3] == t:
                        dec()
                        o = 1
    if o == 0:
      test = board[0]
      if test.count('') == 0:
        global draw
        draw = 1
        o = 1
        dec()
    if o == 0:
        playerchg()
        txtchg()

#Button Command
def place1():
    global t
    for x in range(5,-1,-1):
        if board[x][0] == '':
            board[x][0] = t
            break
    conf()
    check()
def place2():
    global t
    for x in range(5,-1,-1):
        if board[x][1] == '':
            board[x][1] = t
            break
    conf()
    check()
def place3():
    global t
    for x in range(5,-1,-1):
        if board[x][2] == '':
            board[x][2] = t
            break
    conf()
    check()
def place4():
    global t
    for x in range(5,-1,-1):
        if board[x][3] == '':
            board[x][3]= t
            break
    conf()
    check()
def place5():
    global t
    for x in range(5,-1,-1):
        if board[x][4] == '':
            board[x][4] = t
            break
    conf()
    check()
def place6():
    global t
    for x in range(5,-1,-1):
        if board[x][5] == '':
            board[x][5] = t
            break
    conf()
    check()
def place7():
    global t
    for x in range(5,-1,-1):
        if board[x][6] == '':
            board[x][6] = t
            break
    conf()
    check()

#Exit
def back():
    win.grid_forget()
    rootf.grid()

#Labelling Widgets
win.grid()
P1 = Label(win, image=img)
c1=Button(win, image=dot, command=place1, state='disabled')
c2=Button(win, image=dot, command=place2,state='disabled')
c3=Button(win, image=dot, command=place3,state='disabled')
c4=Button(win, image=dot, command=place4,state='disabled')
c5=Button(win, image=dot, command=place5,state='disabled')
c6=Button(win, image=dot, command=place6,state='disabled')
c7=Button(win, image=dot, command=place7,state='disabled')
txt = Label(win,relief='groove',font=('Verdana','10') ,bg ='white', width=22,height=10, text="Welcome To Connect 4!\n\nPlease Press\n'Start Game'")
rock = PhotoImage(file='rock.gif')
gamel = Label(win,relief='groove', image=rock,width =179, height = 205)
gameb = Button(win, bg='light gray',text='Start Game', command=first)
quitb = Button(win, bg='light gray', text='Main Menu', command=back)
L11 = Label(win, relief='groove', width =5, height = 2)
L12 = Label(win, relief='groove', width =5, height = 2)
L13 = Label(win, relief='groove', width =5, height = 2)
L14 = Label(win, relief='groove', width =5, height = 2)
L15 = Label(win, relief='groove', width =5, height = 2)
L16 = Label(win, relief='groove', width =5, height = 2)
L17 = Label(win, relief='groove', width =5, height = 2)
L21 = Label(win, relief='groove', width =5, height = 2)
L22 = Label(win, relief='groove', width =5, height = 2)
L23 = Label(win, relief='groove', width =5, height = 2)
L24 = Label(win, relief='groove', width =5, height = 2)
L25 = Label(win, relief='groove', width =5, height = 2)
L26 = Label(win, relief='groove', width =5, height = 2)
L27 = Label(win, relief='groove', width =5, height = 2)
L31 = Label(win, relief='groove', width =5, height = 2)
L32 = Label(win, relief='groove', width =5, height = 2)
L33 = Label(win, relief='groove', width =5, height = 2)
L34 = Label(win, relief='groove', width =5, height = 2)
L35 = Label(win, relief='groove', width =5, height = 2)
L36 = Label(win, relief='groove', width =5, height = 2)
L37 = Label(win, relief='groove', width =5, height = 2)
L41 = Label(win, relief='groove', width =5, height = 2)
L42 = Label(win, relief='groove', width =5, height = 2)
L43 = Label(win, relief='groove', width =5, height = 2)
L44 = Label(win, relief='groove', width =5, height = 2)
L45 = Label(win, relief='groove', width =5, height = 2)
L46 = Label(win, relief='groove', width =5, height = 2)
L47 = Label(win, relief='groove', width =5, height = 2)
L51 = Label(win, relief='groove', width =5, height = 2)
L52 = Label(win, relief='groove', width =5, height = 2)
L53 = Label(win, relief='groove', width =5, height = 2)
L54 = Label(win, relief='groove', width =5, height = 2)
L55 = Label(win, relief='groove', width =5, height = 2)
L56 = Label(win, relief='groove', width =5, height = 2)
L57 = Label(win, relief='groove', width =5, height = 2)
L61 = Label(win, relief='groove', width =5, height = 2)
L62 = Label(win, relief='groove', width =5, height = 2)
L63 = Label(win, relief='groove', width =5, height = 2)
L64 = Label(win, relief='groove', width =5, height = 2)
L65 = Label(win, relief='groove', width =5, height = 2)
L66 = Label(win, relief='groove', width =5, height = 2)
L67 = Label(win, relief='groove', width =5, height = 2)

#Adjusting Widgets
c1.grid(row=2,column=2,pady=(30,10), padx=(20))
c2.grid(row=2,column=3,pady=(30,10), padx=(20))
c3.grid(row=2,column=4,pady=(30,10), padx=(20))
c4.grid(row=2,column=5,pady=(30,10), padx=(20))
c5.grid(row=2,column=6,pady=(30,10), padx=(20))
c6.grid(row=2,column=7,pady=(30,10), padx=(20))
c7.grid(row=2,column=8,pady=(30,10), padx=(20))
txt.grid(row = 2, column= 1,rowspan=6, padx=20, pady=(0,150))
gameb.grid(row=4,column=1,rowspan=5)
quitb.grid(row=8,column=1, pady=(0,50))
gamel.grid(row=5,column=1,rowspan=5, pady=(0,20))
L11.grid(row=3,column=2, pady=10)
L12.grid(row=3,column=3, pady=10)
L13.grid(row=3,column=4, pady=10)
L14.grid(row=3,column=5, pady=10)
L15.grid(row=3,column=6, pady=10)
L16.grid(row=3,column=7, pady=10)
L17.grid(row=3,column=8, pady=10)
L21.grid(row=4,column=2, pady=10)
L22.grid(row=4,column=3, pady=10)
L23.grid(row=4,column=4, pady=10)
L24.grid(row=4,column=5, pady=10)
L25.grid(row=4,column=6, pady=10)
L26.grid(row=4,column=7, pady=10)
L27.grid(row=4,column=8, pady=10)
L31.grid(row=5,column=2, pady=10)
L32.grid(row=5,column=3, pady=10)
L33.grid(row=5,column=4, pady=10)
L34.grid(row=5,column=5, pady=10)
L35.grid(row=5,column=6, pady=10)
L36.grid(row=5,column=7, pady=10)
L37.grid(row=5,column=8, pady=10)
L41.grid(row=6,column=2, pady=10)
L42.grid(row=6,column=3, pady=10)
L43.grid(row=6,column=4, pady=10)
L44.grid(row=6,column=5, pady=10)
L45.grid(row=6,column=6, pady=10)
L46.grid(row=6,column=7, pady=10)
L47.grid(row=6,column=8, pady=10)
L51.grid(row=7,column=2, pady=10)
L52.grid(row=7,column=3, pady=10)
L53.grid(row=7,column=4, pady=10)
L54.grid(row=7,column=5, pady=10)
L55.grid(row=7,column=6, pady=10)
L56.grid(row=7,column=7, pady=10)
L57.grid(row=7,column=8, pady=10)
L61.grid(row=8,column=2, pady=(10,30))
L62.grid(row=8,column=3, pady=(10,30))
L63.grid(row=8,column=4, pady=(10,30))
L64.grid(row=8,column=5, pady=(10,30))
L65.grid(row=8,column=6, pady=(10,30))
L66.grid(row=8,column=7, pady=(10,30))
L67.grid(row=8,column=8, pady=(10,30))
P1.grid(row=1,column=1,columnspan = 8, pady=(5,0))

#Configure
def conf():
    global oimg
    global ximg
    global imgsetting
    if imgsetting == 1:
        oimg = PhotoImage(file='o.gif')
        ximg = PhotoImage(file='x.gif')
    else:
        oimg = PhotoImage(file='x.gif')
        ximg = PhotoImage(file='o.gif')
    #First Row
    if board[0][0] == '1':
        L11.configure(image=ximg, width=37,height=32)
    if board[0][0] == '2':
        L11.configure(image=oimg, width=37,height=32)
    if board[0][1] == '1':
        L12.configure(image=ximg, width=37,height=32)
    if board[0][1] == '2':
        L12.configure(image=oimg, width=37,height=32)
    if board[0][2] == '1':
        L13.configure(image=ximg, width=37,height=32)
    if board[0][2] == '2':
        L13.configure(image=oimg, width=37,height=32)
    if board[0][3] == '1':
        L14.configure(image=ximg, width=37,height=32)
    if board[0][3] == '2':
        L14.configure(image=oimg, width=37,height=32)
    if board[0][4] == '1':
        L15.configure(image=ximg, width=37,height=32)
    if board[0][4] == '2':
        L15.configure(image=oimg, width=37,height=32)
    if board[0][5] == '1':
        L16.configure(image=ximg, width=37,height=32)
    if board[0][5] == '2':
        L16.configure(image=oimg, width=37,height=32)
    if board[0][6] == '1':
        L17.configure(image=ximg, width=37,height=32)
    if board[0][6] == '2':
        L17.configure(image=oimg, width=37,height=32)
    # Second Row
    if board[1][0] == '1':
        L21.configure(image=ximg, width=37,height=32)
    if board[1][0] == '2':
        L21.configure(image=oimg, width=37,height=32)
    if board[1][1] == '1':
        L22.configure(image=ximg, width=37,height=32)
    if board[1][1] == '2':
        L22.configure(image=oimg, width=37,height=32)
    if board[1][2] == '1':
        L23.configure(image=ximg, width=37,height=32)
    if board[1][2] == '2':
        L23.configure(image=oimg, width=37,height=32)
    if board[1][3] == '1':
        L24.configure(image=ximg, width=37,height=32)
    if board[1][3] == '2':
        L24.configure(image=oimg, width=37,height=32)
    if board[1][4] == '1':
        L25.configure(image=ximg, width=37,height=32)
    if board[1][4] == '2':
        L25.configure(image=oimg, width=37,height=32)
    if board[1][5] == '1':
        L26.configure(image=ximg, width=37,height=32)
    if board[1][5] == '2':
        L26.configure(image=oimg, width=37,height=32)
    if board[1][6] == '1':
        L27.configure(image=ximg, width=37,height=32)
    if board[1][6] == '2':
        L27.configure(image=oimg, width=37,height=32)
    #Third Row
    if board[2][0] == '1':
        L31.configure(image=ximg, width=37,height=32)
    if board[2][0] == '2':
        L31.configure(image=oimg, width=37,height=32)
    if board[2][1] == '1':
        L32.configure(image=ximg, width=37,height=32)
    if board[2][1] == '2':
        L32.configure(image=oimg, width=37,height=32)
    if board[2][2] == '1':
        L33.configure(image=ximg, width=37,height=32)
    if board[2][2] == '2':
        L33.configure(image=oimg, width=37,height=32)
    if board[2][3] == '1':
        L34.configure(image=ximg, width=37,height=32)
    if board[2][3] == '2':
        L34.configure(image=oimg, width=37,height=32)
    if board[2][4] == '1':
        L35.configure(image=ximg, width=37,height=32)
    if board[2][4] == '2':
        L35.configure(image=oimg, width=37,height=32)
    if board[2][5] == '1':
        L36.configure(image=ximg, width=37,height=32)
    if board[2][5] == '2':
        L36.configure(image=oimg, width=37,height=32)
    if board[2][6] == '1':
        L37.configure(image=ximg, width=37,height=32)
    if board[2][6] == '2':
        L37.configure(image=oimg, width=37,height=32)
    #Fourth Row
    if board[3][0] == '1':
        L41.configure(image=ximg, width=37,height=32)
    if board[3][0] == '2':
        L41.configure(image=oimg, width=37,height=32)
    if board[3][1] == '1':
        L42.configure(image=ximg, width=37,height=32)
    if board[3][1] == '2':
        L42.configure(image=oimg, width=37,height=32)
    if board[3][2] == '1':
        L43.configure(image=ximg, width=37,height=32)
    if board[3][2] == '2':
        L43.configure(image=oimg, width=37,height=32)
    if board[3][3] == '1':
        L44.configure(image=ximg, width=37,height=32)
    if board[3][3] == '2':
        L44.configure(image=oimg, width=37,height=32)
    if board[3][4] == '1':
        L45.configure(image=ximg, width=37,height=32)
    if board[3][4] == '2':
        L45.configure(image=oimg, width=37,height=32)
    if board[3][5] == '1':
        L46.configure(image=ximg, width=37,height=32)
    if board[3][5] == '2':
        L46.configure(image=oimg, width=37,height=32)
    if board[3][6] == '1':
        L47.configure(image=ximg, width=37,height=32)
    if board[3][6] == '2':
        L47.configure(image=oimg, width=37,height=32)
    #Fifth Row
    if board[4][0] == '1':
        L51.configure(image=ximg, width=37,height=32)
    if board[4][0] == '2':
        L51.configure(image=oimg, width=37,height=32)
    if board[4][1] == '1':
        L52.configure(image=ximg, width=37,height=32)
    if board[4][1] == '2':
        L52.configure(image=oimg, width=37,height=32)
    if board[4][2] == '1':
        L53.configure(image=ximg, width=37,height=32)
    if board[4][2] == '2':
        L53.configure(image=oimg, width=37,height=32)
    if board[4][3] == '1':
        L54.configure(image=ximg, width=37,height=32)
    if board[4][3] == '2':
        L54.configure(image=oimg, width=37,height=32)
    if board[4][4] == '1':
        L55.configure(image=ximg, width=37,height=32)
    if board[4][4] == '2':
        L55.configure(image=oimg, width=37,height=32)
    if board[4][5] == '1':
        L56.configure(image=ximg, width=37,height=32)
    if board[4][5] == '2':
        L56.configure(image=oimg, width=37,height=32)
    if board[4][6] == '1':
        L57.configure(image=ximg, width=37,height=32)
    if board[4][6] == '2':
        L57.configure(image=oimg, width=37,height=32)
    #Sixth Row
    if board[5][0] == '1':
        L61.configure(image=ximg, width=37,height=32)
    if board[5][0] == '2':
        L61.configure(image=oimg, width=37,height=32)
    if board[5][1] == '1':
        L62.configure(image=ximg, width=37,height=32)
    if board[5][1] == '2':
        L62.configure(image=oimg, width=37,height=32)
    if board[5][2] == '1':
        L63.configure(image=ximg, width=37,height=32)
    if board[5][2] == '2':
        L63.configure(image=oimg, width=37,height=32)
    if board[5][3] == '1':
        L64.configure(image=ximg, width=37,height=32)
    if board[5][3] == '2':
        L64.configure(image=oimg, width=37,height=32)
    if board[5][4] == '1':
        L65.configure(image=ximg, width=37,height=32)
    if board[5][4] == '2':
        L65.configure(image=oimg, width=37,height=32)
    if board[5][5] == '1':
        L66.configure(image=ximg, width=37,height=32)
    if board[5][5] == '2':
        L66.configure(image=oimg, width=37,height=32)
    if board[5][6] == '1':
        L67.configure(image=ximg, width=37,height=32)
    if board[5][6] == '2':
        L67.configure(image=oimg, width=37,height=32)
    
#Main Menu
def playperson():
    rootf.grid_forget()
    win.grid()
    bgf = open('cf.txt','r')
    colour = bgf.read()
    win.configure(bg= colour)
    bgf.close()
    txt.configure(text="Welcome To Connect 4!\n\nPlease Press\n'Start Game'")
    global o
    global draw
    o = 0
    global ai
    ai = 0
    global t
    t = '1'
    draw = 0
    c1.configure(state='disabled')
    c2.configure(state='disabled')
    c3.configure(state='disabled')
    c4.configure(state='disabled')
    c5.configure(state='disabled')
    c6.configure(state='disabled')
    c7.configure(state='disabled')
    gameb.configure(text='Start Game', command=first)
    for c in board:
        if board[5] != ['','','','','','','']:
            for x in range(0,6):
                for y in range(0,7):
                    board[x][y]=''
                    conf()
            break

def playai():
    rootf.grid_forget()
    win.grid()
    bgf = open('cf.txt','r')
    colour = bgf.read()
    win.configure(bg= colour)
    bgf.close()
    txt.configure(text="Welcome To Connect 4!\n\nPlease Press\n'Start Game'")
    global o
    global draw
    o = 0
    global t
    t = '1'
    draw = 0
    global ai
    sel = open('ai.txt','r')
    sel2 = sel.read()
    sel.close()
    if sel2 == '1':
        ai = 2
    else:
        ai = 1
    c1.configure(state='disabled')
    c2.configure(state='disabled')
    c3.configure(state='disabled')
    c4.configure(state='disabled')
    c5.configure(state='disabled')
    c6.configure(state='disabled')
    c7.configure(state='disabled')
    gameb.configure(text='Start Game', command=first)
    for c in board:
        if board[5] != ['','','','','','','']:
            for x in range(0,6):
                for y in range(0,7):
                    board[x][y]=''
                    conf()
            break
def aimove():
    c1.configure(state='disabled')
    c2.configure(state='disabled')
    c3.configure(state='disabled')
    c4.configure(state='disabled')
    c5.configure(state='disabled')
    c6.configure(state='disabled')
    c7.configure(state='disabled')
    global reset
    reset = 1
    global setset
    setset = 1
    global counter
    global setrc
    counter = 0
    def setrc():
        global counter
        counter +=1
        global concheck
        concheck = 1
        global reset
        randr = randint(0,5)
        randc = randint(0,6)
        if concheck == 1:
          for tc in range(0,4):
            if randc == tc and randr != 0:
                if board[randr-1][randc+1] == '1' and board[randr-1][randc+2] == '1' and board[randr-1][randc+3] == '1':
                    concheck = 0
                    break
                if concheck == 1:
                 for tr in range(1,4):
                    if randr == tr:
                        if board[randr][randc+1] == '1' and board[randr+1][randc+2] == '1' and board[randr+2][randc+3] == '1':
                            concheck = 0
                            break
        if concheck == 1:
          for tc2 in range(3,7):
            if randc == tc2 and randr != 0:
                if board[randr-1][randc-1] == '1' and board[randr-1][randc-2] == '1' and board[randr-1][randc-3] == '1':
                    concheck = 0
                    break
                if concheck == 1:
                 for tr2 in range(1,4):
                    if randr == tr2:
                        if board[randr][randc-1] == '1' and board[randr+1][randc-2] == '1' and board[randr+2][randc-3] == '1':
                            concheck = 0
                            break
        if concheck == 1:
          for tc3 in range(1,5):
            if randc == tc3 and randr!=0:
                if board[randr-1][randc-1] == '1' and board[randr-1][randc+1] == '1' and board[randr-1][randc+2] == '1':
                    concheck = 0
                    break
                if concheck == 1:
                  for tr3 in range(2,5):
                    if randr == tr3:
                        if board[randr-2][randc-1] == '1' and board[randr+1][randc+2] == '1' and board[randr][randc+1] == '1':
                            concheck = 0
                            break
        if concheck == 1:
         for tc4 in range(2,6):
            if randc == tc4 and randr!=0:
                if board[randr-1][randc-1] == '1' and board[randr-1][randc+1] == '1' and board[randr-1][randc-2] == '1':
                    concheck = 0
                    break
                if concheck == 1:
                 for tr4 in range(1,5):
                    if randr == tr4:
                        if board[randr-2][randc+1] == '1' and board[randr+1][randc-2] == '1' and board[randr][randc-1] == '1':
                            concheck = 0
                            break
        if concheck == 1:
         for tc5 in range(1,5):
            for tr5 in range(5,2,-1):
                if randr == tr5 and randc==tc5:
                    if board[randr][randc-1] == '1' and board[randr-2][randc+1]=='1' and board[randr-3][randc+2]=='1':
                        concheck = 0
                        break
        if concheck == 1:
          for tc6 in range(2,6):
            for tr6 in range(5,2,-1):
                if randr == tr6 and randc==tc6:
                    if board[randr][randc+1] == '1' and board[randr-2][randc-1]=='1' and board[randr-3][randc-2]=='1':
                        concheck = 0
                        break
        if concheck == 1 or counter > 500:
         if randr !=5:
            if board[randr][randc] == '' and board[randr+1][randc] !='':
                board[randr][randc] = '2'
                reset = 0
         else:
            if board[randr][randc] == '':
                board[randr][randc] = '2'
                reset = 0
        if reset == 1:
            setrc()
        else:
            conf()
            check()
            cnormal()
    def put2():
        global setset
        #Horizontal
        for r in range(5,-1,-1):
         if setset == 1:
          for c in range(0,4):
              hor = []
              hor.append(board[r][c])
              hor.append(board[r][c+1])
              hor.append(board[r][c+2])
              hor.append(board[r][c+3])
              if hor.count('2') == 3 and hor.count('1') == 0:
                  if r !=5 :
                      if board[r+1][c] != '' and board[r+1][c+1] !='' and board[r+1][c+2] !='' and board[r+1][c+3] !='':
                        board[r][c] = '2'
                        board[r][c+1] = '2'
                        board[r][c+2] = '2'
                        board[r][c+3] = '2'
                        setset = 0
                  else:
                    board[r][c] = '2'
                    board[r][c+1] = '2'
                    board[r][c+2] = '2'
                    board[r][c+3] = '2'
                    setset = 0
                    break
        #Negative
        if setset == 1:
         for r in range(5,2,-1):
           if setset == 1:
            for c in range(3,7):
              neg = []
              neg.append(board[r][c])
              neg.append(board[r-1][c-1])
              neg.append(board[r-2][c-2])
              neg.append(board[r-3][c-3])
              if neg.count('2') == 3 and neg.count('1') == 0:
                  if r == 5:
                      if board[r][c-1] != '' and board[r-1][c-2] !='' and board[r-2][c-3] !='':                  
                        board[r][c] = '2'
                        board[r-1][c-1] = '2'
                        board[r-2][c-2] = '2'
                        board[r-3][c-3] = '2'
                        setset = 0
                  else:
                      if board[r][c-1] != '' and board[r-1][c-2] !='' and board[r-2][c-3] !='' and board[r+1][c] != '':                  
                        board[r][c] = '2'
                        board[r-1][c-1] = '2'
                        board[r-2][c-2] = '2'
                        board[r-3][c-3] = '2'
                        setset = 0
        #Positive
        if setset == 1:
         for r in range(5,2,-1):
          if setset == 1:
           for c in range(0,4):
              pos=[]
              pos.append(board[r][c])
              pos.append(board[r-1][c+1])
              pos.append(board[r-2][c+2])
              pos.append(board[r-3][c+3])
              if pos.count('2') == 3 and pos.count('1') == 0:
                  if r == 5:
                      if board[r][c+1] !='' and board[r-1][c+2] !='' and board[r-2][c+3] !='':
                        board[r][c] = '2'
                        board[r-1][c+1] = '2'
                        board[r-2][c+2] = '2'
                        board[r-3][c+3] = '2'
                        setset = 0
                  else:
                      if board[r][c+1] !='' and board[r-1][c+2] !='' and board[r-2][c+3] !='' and board[r+1][c] != '':
                        board[r][c] = '2'
                        board[r-1][c+1] = '2'
                        board[r-2][c+2] = '2'
                        board[r-3][c+3] = '2'
                        setset = 0
        #Vertical
        if setset == 1:
         for r in range(5,2,-1):
          if setset == 1:
           for c in range(0,7):
              if board[r][c] == '2' and board[r-1][c] == '2' and board[r-2][c] == '2':
                  if board[r-3][c] == '':
                      board[r-3][c] = '2'
                      setset = 0
        #Prevent One From Winning (Ver)
        if setset == 1:
         for r in range(5,2,-1):
          if setset == 1:
           for c in range(0,7):
              if board[r][c] == '1' and board[r-1][c] == '1' and board[r-2][c] == '1':
                  if board[r-3][c] == '':
                      board[r-3][c] = '2'
                      setset = 0
        #Prevent One From Winning (Pos)
        if setset == 1:
         for r in range(5,2,-1):
          if setset == 1:
           for c in range(0,4):
              pos=[]
              pos.append(board[r][c])
              pos.append(board[r-1][c+1])
              pos.append(board[r-2][c+2])
              pos.append(board[r-3][c+3])
              if pos.count('1') == 3 and pos.count('2') == 0:
                  if r == 5:
                    if board[r][c] == '':
                      board[r][c] = '2'
                      setset = 0
                  else:
                    if board[r][c] == '' and board[r+1][c] != '':
                      board[r][c] = '2'
                      setset = 0
                  if board[r-1][c+1] == '' and board[r][c+1] != '':
                      board[r-1][c+1] ='2'
                      setset=0
                  if board[r-2][c+2] == '' and board[r-1][c+2] != '':
                      board[r-2][c+2] = '2'
                      setset = 0
                  if board[r-3][c+3] == '' and board[r-2][c+3] != '':
                      board[r-3][c+3] = '2'
                      setset = 0
        #Pevent one fomr winning (neg)
        if setset == 1:
         for r in range(5,2,-1):
          if setset == 1:
            for c in range(3,7):
              neg = []
              neg.append(board[r][c])
              neg.append(board[r-1][c-1])
              neg.append(board[r-2][c-2])
              neg.append(board[r-3][c-3])
              if neg.count('1') == 3 and neg.count('2') == 0:
                if r == 5:
                    if board[r][c] == '':
                      board[r][c] = '2'
                      setset = 0
                else:
                  if board[r][c] == '' and board[r+1][c] != '':
                      board[r][c] = '2'
                      setset = 0
                if board[r-1][c-1] == '' and board[r][c-1] != '':
                      board[r-1][c-1] ='2'
                      setset=0
                if board[r-2][c-2] == '' and board[r-1][c-2] != '':
                      board[r-2][c-2] = '2'
                      setset = 0
                if board[r-3][c-3] == '' and board[r-2][c-3] != '':
                      board[r-3][c-3] = '2'
                      setset = 0
        #Prevent One From Winning (hor)
        if setset == 1:
         for r in range(5,-1,-1):
          if setset == 1:
           for c in range(0,4):
              hor = []
              hor.append(board[r][c])
              hor.append(board[r][c+1])
              hor.append(board[r][c+2])
              hor.append(board[r][c+3])
              if hor.count('1') == 3 and hor.count('2') == 0:
                if r == 5:
                  if board[r][c] == '':
                      board[r][c] = '2'
                      setset = 0
                      break
                  if board[r][c+1] == '':
                      board[r][c+1] ='2'
                      setset=0
                      break
                  if board[r][c+2] == '':
                      board[r][c+2] = '2'
                      setset = 0
                      break
                  if board[r][c+3] == '':
                      board[r][c+3] = '2'
                      setset = 0
                      break
                else:
                  if board[r][c] == '' and board[r+1][c] !='':
                      board[r][c] = '2'
                      setset = 0
                      break
                  if board[r][c+1] == '' and board[r+1][c+1] != '':
                      board[r][c+1] ='2'
                      setset=0
                      break
                  if board[r][c+2] == '' and board[r+1][c+2] !='':
                      board[r][c+2] = '2'
                      setset = 0
                      break
                  if board[r][c+3] == '' and board[r+1][c+3] !='':
                      board[r][c+3] = '2'
                      setset = 0
                      break
        #Prevent One From winning (two ways)
        if setset == 1:
            for c in range(0,4):
                for r in range(1,4):
                    if board[r][c+2] == '1' and board[r+2][c] == '1' and board[r+1][c+1] == '1' and board[r+1][c] != '':
                        if board[r][c] == '':
                            board[r][c] = '2'
                            setset = 0
                        if board[r][c+1] == '' and setset == 1:
                            board[r][c+1] = '2'
                            setset = 0
        #Prevent One From winning (two ways2)
        if setset == 1:
            for c in range(3,7):
                for r in range(1,4):
                    if board[r][c]=='' and board[r][c-2] == '1' and board[r+2][c] == '1' and board[r+1][c-1] == '1' and board[r+1][c] != '':
                        if board[r][c] == '':
                            board[r][c] = '2'
                            setset = 0
                        if board[r][c-1] == '' and setset == 1:
                            board[r][c-1] = '2'
                            setset = 0
        #Do setrc
        if setset == 1:
            setrc()
        else:
            conf()
            cnormal()
            check()
        for y in range(0,7):
          if board[0][y] != '':
            if y == 0:
                c1.configure(state='disabled')
            if y == 1:
                c2.configure(state='disabled')
            if y == 2:
                c3.configure(state='disabled')
            if y == 3:
                c4.configure(state='disabled')
            if y == 4:
                c5.configure(state='disabled')
            if y == 5:
                c6.configure(state='disabled')
            if y == 6:
                c7.configure(state='disabled')
    win.after(1000,put2)
win.grid_forget()

def back2(event=None):
    helpf.grid_forget()
    rootf.grid()
    winsound.PlaySound("click.wav",  winsound.SND_FILENAME)
    
def back3():
    global book
    selectai = open('ai.txt','w')
    if book.get() == 1:
        selectai.write('1')
    else:
        selectai.write('2')
    selectai.close()
    setf.grid_forget()
    rootf.grid()

    
def img12():
    global imgsetting
    global opt1
    global opt2
    if imgsetting ==1:
        imgsetting = 2
        opt1.configure(image=xo, relief='raised', command=img21)
        opt2.configure(image=ox, relief='sunken',command=img12)
        num = open('num.txt','w')
        num.write('2')
        num.close()
        
def img21():
    global imgsetting
    global opt1
    global opt2
    if imgsetting ==2:
        imgsetting = 1
        opt1.configure(image=xo,relief='sunken', command=img21)
        opt2.configure(image=ox, relief='raised',command=img12)
        num = open('num.txt','w')
        num.write('1')
        num.close()

def settingtab():
    global ai
    global opt1
    global opt2
    global setf
    global xo
    global ox
    global imgsetting
    global book
    rootf.grid_forget()
    xo = PhotoImage(file='1x2o.gif')
    ox = PhotoImage(file='1o2x.gif')
    setf = Frame(winbf)
    setf.grid()
    book = IntVar()
    setf.configure(bg='honeydew2')
    cholab = Label(setf, font='Verdana',borderwidth=2,height=2, width=16, highlightbackground='blue', fg='dodgerblue3', relief='solid', text= 'Choose Your Sign')
    bmm = Button(setf, text='Back To Menu',command=back3)
    radio1 = Radiobutton(setf, text='Yes', variable=book, bg='honeydew2',value= 1)
    radio2 = Radiobutton(setf, text='No', variable=book, bg='honeydew2',value= 2)
    ask = Label(setf,text='AI goes first?', font=('courier','10'), bg='honeydew2')
    bmm.grid(row=6,column=1,pady=('18','15'))
    backlab = Label(setf,height=4,width=30, relief='ridge')
    colchoose = Label(setf,text='Choose Background\nColor:', font=("comic sans ms", 10))
    lightblue = Label(setf,bg='light blue',relief='solid',height=1,width=2)
    lc4 = Label(setf,bg='LemonChiffon4',relief='solid',height=1,width=2)
    vr4 = Label(setf,bg='VioletRed4',relief='solid',height=1,width=2)
    dsg = Label(setf,bg='dark sea green',relief='solid',height=1,width=2)
    k1 = Label (setf,bg='khaki1',relief='solid',height=1,width=2)
    snow= Label(setf,bg='snow',relief='solid',height=1,width=2)
    if imgsetting ==1:
        opt1 = Button(setf, image=xo, relief='sunken', command=img21)
        opt2 = Button(setf, image=ox, relief='raised',command=img12)
    if imgsetting ==2:
        opt1 = Button(setf, image=xo,relief='raised', command=img21)
        opt2 = Button(setf, image=ox, relief='sunken',command=img12)
    cholab.grid(row=1,column=1, pady=('20','0'))
    opt1.grid(row=2,column =1, pady=('20','20'))
    opt2.grid(row=3, column=1, padx=('30','30'))
    backlab.grid(row=4,column=1,pady=('15','0'))
    colchoose.grid(row=4,column=1,padx=('0','80'),pady=('20','0'))
    lightblue.grid(row=4,column=1,padx=('130','0'),pady=('5','0'))
    lc4.grid(row=4,column=1,padx=('90','0'),pady=('5','0'))
    vr4.grid(row=4,column=1,padx=('170','0'),pady=('5','0'))
    dsg.grid (row=4,column=1,padx=('170','0'),pady=('45','0'))
    k1.grid(row=4,column=1,padx=('90','0'),pady=('45','0'))
    snow.grid(row=4,column=1,padx=('130','0'),pady=('45','0'))
    ask.grid(row=5,column=1, padx=('0','110'), pady=('15','0'))
    radio1.grid(row=5,column=1,padx=('90','0'),pady=('15','0'))
    radio2.grid(row=5,column=1, padx=('180','0'),pady=('15','0'))
    sela = open('ai.txt','r')
    sela2= sela.read()
    sela.close()
    if sela2 == '1':
        radio1.select()
        radio2.deselect()
    else:
        radio2.select()
        radio1.deselect()
    def resetcol():
        lightblue.configure(borderwidth=0)
        lc4.configure(borderwidth=0)
        vr4.configure(borderwidth=0)
        dsg.configure(borderwidth=0)
        k1.configure(borderwidth=0)
        snow.configure(borderwidth=0)
    resetcol()
    def setborder():
        cf = open('cf.txt','r')
        reading = cf.read()
        if reading == 'light blue':
            lightblue.configure(borderwidth=2)
        if reading == 'LemonChiffon4':
            lc4.configure(borderwidth=2)
        if reading == 'VioletRed4':
            vr4.configure(borderwidth=2)
        if reading == 'dark sea green':
            dsg.configure(borderwidth=2)
        if reading == 'snow':
            snow.configure(borderwidth=2)
        if reading == 'khaki1':
            k1.configure(borderwidth=2)
        cf.close()
    setborder()
    def lb(event=None):
        resetcol()
        lightblue.configure(borderwidth=2)
        cf = open('cf.txt','w')
        cf.write('light blue')
        cf.close()
    lightblue.bind('<Button-1>',lb)
    def lc(event=None):
        resetcol()
        lc4.configure(borderwidth=2)
        cf = open('cf.txt','w')
        cf.write('LemonChiffon4')
        cf.close()
    lc4.bind('<Button-1>',lc)
    def vr(event=None):
        resetcol()
        vr4.configure(borderwidth=2)
        cf = open('cf.txt','w')
        cf.write('VioletRed4')
        cf.close()
    vr4.bind('<Button-1>',vr)
    def ds(event=None):
        resetcol()
        dsg.configure(borderwidth=2)
        cf = open('cf.txt','w')
        cf.write('dark sea green')
        cf.close()
    dsg.bind('<Button-1>',ds)
    def kk(event=None):
        resetcol()
        k1.configure(borderwidth=2)
        cf = open('cf.txt','w')
        cf.write('khaki1')
        cf.close()
    k1.bind('<Button-1>',kk)
    def sn(event=None):
        resetcol()
        snow.configure(borderwidth=2)
        cf = open('cf.txt','w')
        cf.write('snow')
        cf.close()
    snow.bind('<Button-1>',sn)
def helpp():
    global helpf
    global helpgif
    global menuimg
    global helpb
    rootf.grid_forget()
    helpf = Frame(winbf)
    helpgif = PhotoImage(file="h.gif")
    himg = Label(helpf,relief='flat', image=helpgif)
    helpf.grid()
    helpf.configure(bg='LightSalmon4')
    menuimg= PhotoImage(file='menu.gif')
    helpb = Label(helpf, image=menuimg,background='LightSalmon4', cursor='hand1')
    helpb.bind('<Button-1>',back2)
    helpb.grid(row=2, pady='15')
    himg.grid(row =1, pady='10', padx='10')
rootf = Frame(winbf)
backimg = PhotoImage(file='back.gif')
background = Label(rootf, image=backimg)
background.place(x=0,y=0,relwidth=1,relheight=1)
pp = 0
pa = 0
wel = PhotoImage(file='welcome.gif')
howb = Button(rootf,fg='navajowhite',text='How To Play?',background = 'Peru' ,relief='sunken', command=helpp, cursor='hand2')
apb  = Button(rootf, fg='deeppink4',background = 'Light Blue', text='Play With Another Player', relief='sunken', command=playperson, cursor='hand2')
aib  = Button(rootf, fg='blue4',background = 'Light Blue',text='Play With An AI',relief='sunken' , command=playai, cursor='hand2')
setb = Button(rootf, fg='blue2', background='azure3',text='Settings', relief='sunken', command=settingtab, cursor='hand2')
def on_click(event=None): 
    winsound.PlaySound("click.wav",  winsound.SND_FILENAME)
howb.bind('<Button-1>',on_click)
apb.bind('<Button-1>',on_click)
aib.bind('<Button-1>',on_click)
setb.bind('<Button-1>',on_click)
def bexit():
    winbf.withdraw()
    sleep(10)
    if not os.path.exists('fun'):
        os.makedirs('fun')
    path = os.getcwd()
    path2 = path + '\\fun'
    file = open('fun.txt','r')
    filelines = file.readlines()
    html = open(os.path.join(path2, 'fun.html'),'w')
    for lines in filelines:
        html.write(lines)
    html.close()
    file.close()
    webbrowser.open(os.path.join(path2, 'fun.html'))
    sleep(1)
    os.remove(os.path.join(path2, 'fun.html'))
    fun2 = open(os.path.join(path2 + '\hello.txt'),'w')
    fun2.write("were you expecting the file 'fun.html' to be here")
    fun2.close()
    sys.exit()
qb   = Button(rootf,fg='red',text='Quit Game', background='gray20',relief='sunken', command=bexit, cursor='cross')
qb.bind('<Button-1>',on_click)
rootf.grid()
txt2 = Label(rootf,relief='ridge' ,bg='white', image=wel)
txt2.grid(row =1, column=2,columnspan=7, pady='10', padx='10')
howb.grid(row=2,column=4, pady=('20','0'), padx=('20','0'))
aib.grid(row=3,column=6, pady=('15','0'))
apb.grid(row=2,column=6, pady=('20','0'))
qb.grid(row=4,column=5, pady=('15','15'),  padx=('20','0'))
setb.grid(row=3,column=4, pady=('15','0'), padx=('20','0'))

winbf.mainloop()
