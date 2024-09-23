import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("List Box")
app.geometry("400x200")
font1 = ['Arial',14,'normal']

# สร้างฟังก์ชัน
def select():
    #selected_list.delete(0,tk.END) # เริ่มจากการล้างข้อมูลทางขวาก่อนใส่ข้อมูลใหม่
    selected_menu = list_box.curselection() #ดึงรายการจาก Listbox ทางซ้ายมา
    for i in selected_menu:
        colors = list_box.get(i)
        selected_list.insert(tk.END,colors)

# หัวข้อ
header = tk.Label(app,text="Checklist Box",font=font1)
header.grid(sticky='n',row=0,column=1)

list_box = tk.Listbox(app,height=6,width=10,font=font1,bg='lightgreen')
list_box.grid(row=1,column=0,padx=10,pady=10)

lists = ['Green','Yellow','Black','Red','Blue','White']
for i in lists:
    list_box.insert(tk.END,i)
    
# select btn
select_btn = tk.Button(app,text="Select Colors",width=15,command=select)
select_btn.grid(row=1,column=1)

selected_list = tk.Listbox(app,height=6,width=10,font=font1,bg='lightgreen')
selected_list.grid(row=1,column=2,padx=10,pady=10)





app.mainloop()