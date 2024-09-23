import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("List Box")
app.geometry("600x400")

# หัวข้อ
header = tk.Label(app,text="Checklist Box",font=('Arial',14))
header.pack(pady=20)

# กรอบเนื้อหา
frame = tk.Frame(app)
frame.pack(expand=False)

# กรอบซ้าย
frame_left = tk.Frame(frame,bd=0.5,relief="solid")
frame_left.grid(row=0,column=0)

# สร้างตัวแปร และใช้ .BooleanVar เพื่อเก็บสถานะของแต่ละ checkbutton
list1 = tk.BooleanVar()
list2 = tk.BooleanVar()
list3 = tk.BooleanVar()
list4 = tk.BooleanVar()
list5 = tk.BooleanVar()
list6 = tk.BooleanVar()
list7 = tk.BooleanVar()

check1 = tk.Checkbutton(frame_left,text="Monday",variable=list1)
check1.grid(sticky="w",padx=(5,5),pady=(5,5))

check2 = tk.Checkbutton(frame_left,text="Tuesday",variable=list2)
check2.grid(sticky="w",padx=(5,5),pady=(5,5))

check3 = tk.Checkbutton(frame_left,text="Wednesday",variable=list3)
check3.grid(sticky="w",padx=(5,5),pady=(5,5))

check4 = tk.Checkbutton(frame_left,text="Thuesday",variable=list4)
check4.grid(sticky="w",padx=(5,5),pady=(5,5))

check5 = tk.Checkbutton(frame_left,text="Friday",variable=list5)
check5.grid(sticky="w",padx=(5,5),pady=(5,5))

check6 = tk.Checkbutton(frame_left,text="Saturday",variable=list6)
check6.grid(sticky="w",padx=(5,5),pady=(5,5))

check7 = tk.Checkbutton(frame_left,text="Sunday",variable=list7)
check7.grid(sticky="w",padx=(5,5),pady=(5,5))

# select button
select_btn = tk.Button(frame,text="Select")
select_btn.grid(row=0,column=1,padx=30)




app.mainloop()