import tkinter
from tkinter.font import BOLD
import tkinter.messagebox
from tkinter import *
proj = Tk()
proj.geometry("1980x1080")
proj.configure(bg="#29A0B1")
proj.title("CA1 Project")

#---------------------Variables------------------
base=100000
#global rolesal
rolesal=0
#global typsal
typsal=0

#------------------Functions---------------------
def home():
        proj.destroy()
        import CA101homepage.py
            
def getrole():
            for i in lst10Role.curselection():
                if i == 1:
                            rolesal=100000
                elif i== 2:
                            rolesal=90000
                elif i== 3:
                            rolesal=80000
                elif i== 4:
                            rolesal=70000
                elif i== 5:
                            rolesal=60000
                elif i== 6:
                            rolesal=50000
                elif i== 7:
                            rolesal=40000
                else:
                            rolesal=30000
                #global rolesal
                print(rolesal)

def gettyp():
            choice= jbtyp.get()
            if choice == 0:
               typesal = 0.5

            if choice == 2:
                typesal = 1
                
            if choice == 3:
                typesal = 2
            print(choice)
        
def getval():
    #print(rolesal,typesal)
    tsalary=(base+(rolesal*typesal))
    tkinter.messagebox.showinfo("Form submitted. Expected salary: ", tsalary)
    print(tsalary)

#==================Widgets========================
#------------------Configuration------------------
Font_tuple_heading = ("Verdana", 30, BOLD )
Font_tuple0 = ("Arial",18)
Font_tuple1 = ("Arial",16)
Font_tuple2 = ("Comic Sans MS", 16)
Font_tuple3 = ("Arial", 12)
Font_tuple4 = ("Comic Sans MS", 12)

#------------------0 Heading------------------
heading=tkinter.Label(proj,text = "JOB APPLICATION PORTAL", bg='#29A0B1')
heading.configure(font= Font_tuple_heading)
heading.grid(row = 0, column = 2, columnspan = 50)
#------------------12 personal info------------------
l12 = tkinter.Label(proj,text = "Personal info: ",  fg='white', bg ='#29A0B1')
l12.configure(font=Font_tuple0)
l12.grid(row =1 ,column = 0,)

#------------------1 First Name------------------
l1 = tkinter.Label(proj,text = "First Name: ", fg='black')
l1.configure(font=Font_tuple1)
l1.grid(row = 1,column = 1, sticky='e')
e1 = tkinter.Entry(proj,bd =3)
e1.configure(font=Font_tuple2)
e1.grid(row = 1, column = 2 )

#------------------2 Middle Name------------------
l2 = tkinter.Label(proj,text = "Middle Name: ", fg='black', bg ='white')
l2.configure(font=Font_tuple1)
l2.grid(row = 2,column = 1, sticky='e' )
e2 = tkinter.Entry(proj,bd =3)
e2.configure(font=Font_tuple2)
e2.grid(row = 2, column = 2)

#------------------3 Last Name------------------
l3 = tkinter.Label(proj,text = "Last Name: ", fg='black', bg ='white')
l3.configure(font=Font_tuple1)
l3.grid(row = 3,column = 1, sticky='e')
e3 = tkinter.Entry(proj,bd =3)
e3.configure(font=Font_tuple2)
e3.grid(row = 3, column = 2)

#------------------4 PAN------------------
l4 = tkinter.Label(proj,text = "PAN Number: ",  fg='black', bg ='white')
l4.configure(font=Font_tuple1)
l4.grid(row = 4,column = 1,  sticky='e')
e4 = tkinter.Entry(proj,bd =3)
e4.configure(font=Font_tuple2)
e4.grid(row = 4, column = 2)

#------------------5 DOB-------------------
l5 = tkinter.Label(proj,text = "DOB(d/m/yy): ",  fg='black', bg ='white')
l5.configure(font=Font_tuple1)
l5.grid(row = 5,column = 1,  sticky='e')
e5 = tkinter.Entry(proj,bd =3)
e5.configure(font=Font_tuple2)
e5.grid(row = 5, column = 2)
#------------------13 contact no-------------------
l5c = tkinter.Label(proj,text = "contact no: ",  fg='black', bg ='white')
l5c.configure(font=Font_tuple1)
l5c.grid(row = 6,column = 1,  sticky='e')
e5c = tkinter.Entry(proj,bd =3)
e5c.configure(font=Font_tuple2)
e5c.grid(row = 6, column = 2)
#------------------14 email id-------------------
l5e = tkinter.Label(proj,text = "Email id ",  fg='black', bg ='white')
l5e.configure(font=Font_tuple1)
l5e.grid(row = 7,column = 1,  sticky='e')
e5e = tkinter.Entry(proj,bd =3)
e5e.configure(font=Font_tuple2)
e5e.grid(row = 7, column = 2)
#------------------6 Address------------------
l6 = tkinter.Label(proj,text = "Address: ",  fg='white', bg ='#29A0B1')
l6.configure(font=Font_tuple0)
l6.grid(row =1 ,column = 3,)

l6home = tkinter.Label(proj,text ="Home No.:", fg='black', bg ='white')
l6home.configure(font=Font_tuple3)
l6home.grid(row = 1, column = 4, sticky='e')
e6home = tkinter.Entry(proj,bd =3)
e6home.configure(font=Font_tuple4)
e6home.grid(row = 1, column = 5 )

l6street = tkinter.Label(proj,text ="Street:", fg='black', bg ='white')
l6street.configure(font=Font_tuple3)
l6street.grid(row = 2, column = 4, sticky='e')
e6street = tkinter.Entry(proj,bd =3)
e6street.configure(font=Font_tuple4)
e6street.grid(row = 2, column = 5 )

l6locality = tkinter.Label(proj,text ="Locality:", fg='black', bg ='white')
l6locality.configure(font=Font_tuple3)
l6locality.grid(row = 3, column = 4, sticky='e' )
e6locality = tkinter.Entry(proj,bd =3)
e6locality.configure(font=Font_tuple4)
e6locality.grid(row = 3, column = 5 )

l6landmark = tkinter.Label(proj,text ="Landmark:", fg='black', bg ='white')
l6landmark.configure(font=Font_tuple3)
l6landmark.grid(row = 4, column = 4, sticky='e')
e6landmark = tkinter.Entry(proj,bd =3)
e6landmark.configure(font=Font_tuple4)
e6landmark.grid(row = 4, column = 5)

l6district = tkinter.Label(proj,text ="District:", fg='black', bg ='white')
l6district.configure(font=Font_tuple3)
l6district.grid(row = 5, column = 4, sticky='e')
e6district = tkinter.Entry(proj,bd =3)
e6district.configure(font=Font_tuple4)
e6district.grid(row = 5, column = 5, )

l6state = tkinter.Label(proj,text ="State:", fg='black', bg ='white')
l6state.configure(font=Font_tuple3)
l6state.grid(row = 6, column = 4, sticky='e')
e6state = tkinter.Entry(proj,bd =3)
e6state.configure(font=Font_tuple4)
e6state.grid(row = 6, column = 5 )

l6zipcode = tkinter.Label(proj,text ="Zipcode:", fg='black', bg ='white' )
l6zipcode.configure(font=Font_tuple3)
l6zipcode.grid(row = 7, column = 4, sticky='e')
e6zipcode = tkinter.Entry(proj, width=6,bd =3)
e6zipcode.configure(font=Font_tuple4)
e6zipcode.grid(row =7 , column = 5)


#------------------9 Education----------------
l9 = tkinter.Label(proj, text = "Education: ", fg = 'white', bg = '#29A0B1')
l9.configure(font=Font_tuple0)
l9.grid(row = 15, column = 0, sticky='e')

l910 = tkinter.Label(proj,text = "10th Percentage: ", fg = 'black', bg = 'white')
l910.configure(font = Font_tuple3)
l910.grid(row = 16, column = 1, sticky = 'e')
e910 = tkinter.Entry(proj,bd =3)
e910.configure(font=Font_tuple4)
e910.grid(row = 16, column = 2)

l910B = tkinter.Label(proj,text = "Board: ", fg = 'black', bg = 'white')
l910B.configure(font = Font_tuple3)
l910B.grid(row = 16, column = 3,sticky = 'e')
e910B = tkinter.Entry(proj,bd =3)
e910B.configure(font=Font_tuple4)
e910B.grid(row = 16, column = 5)

l912 = tkinter.Label(proj,text = "12th Percentage: ", fg = 'black', bg = 'white')
l912.configure(font = Font_tuple3)
l912.grid(row = 17, column = 1,sticky = 'e')
e912 = tkinter.Entry(proj,bd =3)
e912.configure(font=Font_tuple4)
e912.grid(row = 17, column = 2)

l912B = tkinter.Label(proj,text = "Board: ", fg = 'black', bg = 'white')
l912B.configure(font = Font_tuple3)
l912B.grid(row = 17, column = 3,sticky = 'e')
e912B = tkinter.Entry(proj,bd =3)
e912B.configure(font=Font_tuple4)
e912B.grid(row = 17, column = 5)

l9Grad = tkinter.Label(proj,text = "Graduation: ", fg = 'black', bg = 'white')
l9Grad.configure(font = Font_tuple3)
l9Grad.grid(row = 18, column = 1,sticky = 'e')
e9Grad = tkinter.Entry(proj,bd =3)
e9Grad.configure(font=Font_tuple4)
e9Grad.grid(row = 18, column = 2)

l9college = tkinter.Label(proj,text = "College/University: ", fg = 'black', bg = 'white')
l9college.configure(font = Font_tuple3)
l9college.grid(row = 18, column = 3,sticky = 'e')
e9college = tkinter.Entry(proj,bd =3)
e9college.configure(font=Font_tuple4)
e9college.grid(row = 18, column = 5)

l9we = tkinter.Label(proj,text = "Work Experience: ", fg = 'black', bg = 'white')
l9we.configure(font = Font_tuple3)
l9we.grid(row = 19, column = 1,sticky = 'e')
e9we = tkinter.Entry(proj,bd =3)
e9we.configure(font=Font_tuple4)
e9we.grid(row = 19, column = 2)

#------------------10Applying For-------------
l10 = tkinter.Label(proj,text = "Applying For: " , fg = 'white' , bg = '#29A0B1')
l10.configure(font = Font_tuple0)
l10.grid(row = 20, column = 0)
l10Role = tkinter.Label(proj,text = "Role: ", fg = 'black', bg = 'white')
l10Role.configure(font = Font_tuple3)
l10Role.grid(row = 21, column = 1, sticky= 'n',pady = 10)
lst10Role = Listbox(proj, width = 40)
lst10Role.insert(0,'  ')
lst10Role.insert(1,' 1. Software Developer')
lst10Role.insert(2,' 2. Database Administrator')
lst10Role.insert(3,' 3. Computer Hardware Engineer')
lst10Role.insert(4,' 4. Computer System Analytics')
lst10Role.insert(5,' 5. Computer Network Architecture')
lst10Role.insert(6,' 6. Web Developer')
lst10Role.insert(7,' 7. Information Security Analyst')
lst10Role.insert(END,' 8. Computer and Information Research Scientist')
lst10Role.configure(font=Font_tuple3)
lst10Role.grid(row = 21, column = 2)

#------------------11 Job Type------------------
l11 = tkinter.Label(proj, text = "Job Type", fg = 'white', bg = '#29A0B1')
l11.configure(font=Font_tuple0)
l11.grid(row = 23, column = 0)
jbtyp=IntVar()
rb111 = Radiobutton(proj, text = "Internship", variable = jbtyp , value = 0, width =15, anchor = 'w', command=gettyp)
rb111.configure(font=Font_tuple3)
rb111.grid(row = 24, column = 1)
rb112 = Radiobutton(proj, text = "Part Time", variable = jbtyp , value = 1, width =15, anchor = 'w', command=gettyp)
rb112.configure(font=Font_tuple3)
rb112.grid(row = 25, column = 1)
rb113 = Radiobutton(proj, text = "Full Time", variable = jbtyp , value = 2, width =15, anchor = 'w',command=gettyp)
rb113.configure(font=Font_tuple3)
rb113.grid(row = 26, column = 1)

#-------------------Self--------------------------
lst10Rolel1 = tkinter.Label(proj, text = "Tell us about your skills")
lst10Rolel1.configure(font = Font_tuple3)
lst10Rolel1.grid(row = 25, column = 3,)
lst10Rolee1 = Entry(proj, width = 40)
lst10Rolee1.configure(font = Font_tuple4)
lst10Rolee1.grid(row = 25, column = 4)

#---------------------Buttons----------------------
brole=tkinter.Button(proj,text="Select Role", command=getrole)
brole.configure(font=Font_tuple3)
brole.grid(row = 21, column = 3)

b1 = tkinter.Button(proj,text="Submit Form",command=getval)
b1.configure(font=Font_tuple1)
b1.grid(row = 25, column = 5)

back = tkinter.Button(proj, text="Back", command="home")
back.configure(font=Font_tuple1)
back.grid(row = 0, column = 0)

proj.mainloop()
