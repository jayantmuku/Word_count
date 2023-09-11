import tkinter as t
def count():
    words=area.get(1.0,"end-1c")
    n=len(words.split())
    m.config(text="NUMBER OF WORDS="+str(n))
def book():
    exit()
def reset():
    area.delete(1.0,"end")


win=t.Tk()
win.config(bg="brown")
win.geometry("700x400")
bt=t.Button(win,text="COUNT",command=count,font="bold")
bt.place(x=158,y=280)
bt1=t.Button(win,text="EXIT",command=book,font="bold",width=6)
bt1.place(x=310,y=280)
bt2=t.Button(win,text="RESET",command=reset,font="bold")
bt2.place(x=235,y=280)
area=t.Text(win,height=15,width=59)
area.place(x=159,y=30)
m=t.Label(win,bg="brown",font="bold",fg="white")
m.place(x=150,y=310)
