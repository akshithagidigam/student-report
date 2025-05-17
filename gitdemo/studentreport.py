from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("student report")

student_details = {
    "111723039002": {
        "Name": "Neha Yamini",
        "marks": {"Python": "95", "WebTech": "89", "c++": "90", "Maths": "90"},
        "Grade": "A"
    },
    "111723039003": {
        "Name": "Bhavya Unni",
        "marks": {"Python": "95", "WebTech": "89", "c++": "90", "Maths": "90"},
        "Grade": "A"
    },
    "111723039004": {
        "Name": "Rishika",
        "marks": {"Python": "95", "WebTech": "89", "c++": "90", "Maths": "90"},
        "Grade": "A"
    },
    "111723039005": {
        "Name": "Alice saloni",
        "marks": {"Python": "95", "WebTech": "89", "c++": "90", "Maths": "90"},
        "Grade": "A"
    },
    "111723039007": {
        "Name": "Gidigam Akshitha",
        "marks": {"Python": "95", "WebTech": "89", "c++": "90", "Maths": "90"},
        "Grade": "A"
    },
    "111723039012": {
        "Name": "Sudhiksha",
        "marks": {"Python": "95", "WebTech": "89", "c++": "90", "Maths": "90"},
        "Grade": "A"
    },
}

def show_report():
    uid = uid_entry.get()
    if uid in student_details:
        student = student_details[uid]
        print(f"------student report------")
        print(f"\n Name : {student['Name']}")
        print(f"\n UID : ", uid)
        print(f"\n Grade : {student['Grade']}")
        print(f"\n Marks  ")
        print("--------------------")
        print("Python  :", student["marks"]["Python"])
        print("WebTech :", student["marks"]["WebTech"])
        print("c++     :", student["marks"]["c++"])
        print("Maths   :", student["marks"]["Maths"])
        print("--------------------")
    else:
        messagebox.showwarning("Error", "No student found with this UID.")

label = Label(root, text="Enter 12-digits of unique identifier")
label.pack(pady=5)
uid_entry = Entry(root)   
uid_entry.pack(pady=5)

Button(root, text="Show Report", command=show_report).pack(pady=5)

root.mainloop()
