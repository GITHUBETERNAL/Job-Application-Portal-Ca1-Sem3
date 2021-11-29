import tkinter
from tkinter.font import BOLD
rec = tkinter.Tk()
rec.geometry("1920x1080")
rec.configure(bg='dark blue')
#========================Configuration===========================
Font_tuple_heading = ("Verdana", 30, BOLD )
Font_tuple0 = ("Arial",18)
Font_tuple1 = ("Arial",16)
Font_tuple2 = ("Comic Sans MS", 16)
Font_tuple3 = ("Arial", 12)
Font_tuple4 = ("Comic Sans MS", 12)

#========================Widgets=================================
l1=tkinter.Label(rec, text="Recruiter's Page", width=34, font=Font_tuple_heading)
l1.place(x=250, y=0)

l2=tkinter.Label(rec, text="Enter Application Number", width = 20, font=Font_tuple0)
l2.place(x=0, y = 65)

e1= tkinter.Entry(rec, bd=3, width=30, font=Font_tuple2)
e1.place(x = 350, y = 65)

#=========================Buttons===============================
b1=tkinter.Button(rec, text="Show All Applications", font=Font_tuple0)
b1.place(x = 10, y = 130)

rec.mainloop()
