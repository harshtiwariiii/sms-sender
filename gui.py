import tkinter as tk
from tkinter import filedialog,messagebox


def import_file():
    filr_path =filedialog.askopenfilename(
        filetypes=[("Excel files","*.xlsx"),("All files","*.*")]
    )
    if file_path:
        messagebox.showinfo("File Selected",f"Selected: {file_path}")

def select_records():
    messagebox.showinfo("Select Records","Records selected!")#logic hold krne ke liye use kara h 

def clear_fields():
    whatsapp_id_entry.delete(0,tk.END)
    from_rno_entry.delete(0,tk.END)
    to_rno_entry.delete(0,tk.END)


root =tk.Tk()
root.title("SMS/EMAIL SALES MARKETING")
root.geometry("700x350")

import_btn = tk.Button(root, text="Import File", command=import_file)
import_btn.grid(row=0,column=0,padx=10,pady=10,sticky="w")

options=["PET","PSF","FIBRE","OTHER","FABRIC","RPP","MBPE"]
radio_var =tk.StringVar(value=options[0])
for i, opt in enumerate(options):
    tk.Radiobutton(root,text=opt,variable=radio_var,value=opt).grid(row=0,column=i+1,padx=2,sticky="w")

tk.Label(root,text="SELECT RECORD FROM RNo.").grid(row=2,column=0,sticky="e")
whatsapp_id_entry=tk.Entry(root,width=30)
whatsapp_id_entry.grid(row=1,column=1,columnspan=2,sticky="w")

tk.Label(root,text="Select record From RNo").grid(row=2,column=0,sticky="e")
from_rno_entry = tk.Entry(root, width=5)
from_rno_entry.grid(row=2, column=1, sticky="w")
tk.Label(root, text="To RNo").grid(row=2, column=2, sticky="e")
to_rno_entry = tk.Entry(root, width=5)
to_rno_entry.grid(row=2, column=3, sticky="w")

tk.Button(root,text="Select Records",command=select_records).grid(row=2,column=4,padx=5)
tk.Button(root,text="clear",command=clear_fields).grid(row=2, column=5,padx=5)

headers=["RNO","Party Name","Mobile no","Email ID"]
for i ,h in enumerate(headers):
    tk.Label(root,text=h,borderwidth=1,relief="solid",width=18).grid(row=4,column=i,padx=1,pady=10)


table_placeholder = tk.Label(root, text="(Table data will appear here)", fg="gray")
table_placeholder.grid(row=5, column=0, columnspan=4, pady=20)

root.mainloop()



