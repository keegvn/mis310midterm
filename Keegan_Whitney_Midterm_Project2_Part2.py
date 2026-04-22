from tkinter import *
import pandas as pd

root = Tk()
root.title("CCSU Mobile App")
root.geometry("700x500")
root.resizable(False, False)
root.configure(bg="light blue")

data = pd.read_csv("examfile.csv")

logo = PhotoImage(file="CCSULOGO.png")
logo = logo.subsample(3, 3)

logo_label = Label(root, image=logo, bg="light blue")
logo_label.place(x=10, y=10)

output_label = Label(
    root,
    text="",
    bg="light blue",
    justify="left",
    anchor="nw",
    font=("Arial", 10),
    width=50,
    height=16
)
output_label.place(x=140, y=200)

def calendar():
    df = pd.DataFrame(data, columns=["CalendarDate"])
    selected_rows = df[~df["CalendarDate"].isnull()]
    output_label.config(text=selected_rows.to_string(index=False))

def buildings():
    df = pd.DataFrame(data, columns=["Buildings"])
    selected_rows = df[~df["Buildings"].isnull()]
    output_label.config(text=selected_rows.to_string(index=False))

def faculty():
    df = pd.DataFrame(data, columns=["FacultyName"])
    selected_rows = df[~df["FacultyName"].isnull()]
    output_label.config(text=selected_rows.to_string(index=False))

#new buttons for part 2
def school_business():
    text = "School of Business\n\n"
    text = text + "- Accounting\n"
    text = text + "- Finance\n"
    text = text + "- Management & Organization\n"
    text = text + "- Marketing\n"
    text = text + "- Management Information Systems (MIS)\n"
    text = text + "- Business Analytics"
    output_label.config(text=text)

def mis_department():
    text = "MIS Department\n\n"
    text = text + "- Intro to MIS\n"
    text = text + "- Databases Management\n"
    text = text + "- Systems Analysis & Design\n"
    text = text + "- Business Analytics / Data Visualization\n"
    text = text + "- Network and Information Security\n"
    text = text + "- Project Management\n"
    text = text + "- Python for Business Applications"
    output_label.config(text=text)

button1 = Button(root, text="Calendar", command=calendar, bg="", fg="black", width=12)
button1.place(x=100, y=110)

button2 = Button(root, text="Buildings", command=buildings, bg="dark blue", fg="black", width=12)
button2.place(x=230, y=110)

button3 = Button(root, text="Faculty", command=faculty, bg="#003366", fg="black", width=12)
button3.place(x=360, y=110)

button4 = Button(root, text="School of Business", command=school_business, bg="#003366", fg="black", width=18)
button4.place(x=100, y=150)

button5 = Button(root, text="MIS Department", command=mis_department, bg="#003366", fg="black", width=18)
button5.place(x=300, y=150)

root.mainloop()