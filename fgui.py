from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

def compute():
    messagebox.showinfo("Message", "Successful Completition")

win=Tk()
win.title("Time Table generator")
win.geometry("500x500+10+10")
header=Label(text="Time Table generator",fg="white",bg="black",width=100,height=4)
header.pack()
label=Label(text="Enter excel path",height=1)
label.place(x=100, y=100)
e1=StringVar()
entry1=Entry(fg="black",width=20,textvariable=e1)
entry1.focus
entry1.place(x=250, y=100)
label1=Label(text="Enter output path",height=1)
label1.place(x=100, y=150)
e2=StringVar()
entry2=Entry(fg="black",width=20,textvariable=e2)
entry2.place(x=250, y=150)

label2=Label(text="Which type of Timetable do you want:",height=1)
label2.place(x=100, y=200)
v0=IntVar()
v0.set(1)
r1=Radiobutton(win, text="Faculty-wise", variable=v0,value=1)
r2=Radiobutton(win, text="Course-wise", variable=v0,value=2)
r1.place(x=150,y=230)
r2.place(x=250, y=230)

label3=Label(text="What should be the file-type:",height=1)
label3.place(x=100, y=300)              
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(win, text = "Excel Sheets", variable = v1)
C2 = Checkbutton(win, text = "PDFs", variable = v2)
C1.place(x=150, y=330)
C2.place(x=250, y=330)

label=Label(text="Seperate or Combined Excel files:",height=1)
label.place(x=100, y=400)
var = StringVar()
var.set("NA")
data=("NA", "Seperate", "Consolidated")
cb=Combobox(win, values=data)
cb.place(x=300, y=400)
button=Button(text="Submit",height=2,command=compute)
button.place(x=250,y=450)


input_path=e1.get()
output_path=e2.get()
timetable_faculty_type=v0.get()
timetable_course_type=v0.get()
timetable_excel_type=v1.get()
timetable_pdf_type=v2.get()
excel_file_type=var.get()



win.mainloop()

print(input_path)
print(output_path)
print(timetable_faculty_type)
print(timetable_course_type)
print(timetable_excel_type)
print(timetable_pdf_type)
print(excel_file_type)