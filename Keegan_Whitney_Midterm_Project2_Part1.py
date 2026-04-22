from tkinter import *
import pandas as pd

root = Tk()
root.title("CCSU Mobile App")
root.geometry("600x450")
root.resizable(False, False)
root.configure(bg="light blue")

data = pd.read_csv("examfile.csv")

logo = PhotoImage(file="CCSULOGO.png")
logo = logo.subsample(2, 2)

logo_label = Label(root, image=logo, bg="light blue")
logo_label.place(x=10, y=10)

output_label = Label(
    root,
    text="",
    bg="light blue",
    justify="left",
    anchor="nw",
    font=("Arial", 10),
    width=45,
    height=15
)
output_label.place(x=120, y=180)

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

#buttons (clean spacing)
button1 = Button(root, text="Calendar", command=calendar, bg="light green", width=12)
button1.place(x=150, y=110)

button2 = Button(root, text="Buildings", command=buildings, bg="light green", width=12)
button2.place(x=270, y=110)

button3 = Button(root, text="Faculty", command=faculty, bg="light green", width=12)
button3.place(x=390, y=110)

root.mainloop()