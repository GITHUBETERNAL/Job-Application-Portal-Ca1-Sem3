import tkinter
home = tkinter.Tk()
home.geometry("400x300")
home.configure(bg='black')

#=========================Functions==============================
def appfun():
        home.destroy()
        import CA102application

def recfun():
        home.destroy()
        import CA103recruiter

#=========================Heading================================
l1=tkinter.Label(home, text="Job Application Portal",width=20)
l1.place(x = 125, y = 50)

#==========================Buttons===============================
app=tkinter.Button(home, text="Application", command=appfun, width = 20)
app.place(x=62, y=150)

rec=tkinter.Button(home, text="Recruiter", command=recfun, width=20)
rec.place(x=187,y=150)


home.mainloop()