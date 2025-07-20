# Requires: pip install pandas openpyxl
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd

# --- Helper Functions ---
def import_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
    )
    if file_path:
        try:
            df = pd.read_excel(file_path, engine="openpyxl")
            # Expecting columns: Party Name, Mobile, Email
            # Add RNo as index+1
            tree.delete(*tree.get_children())  # Clear previous data
            for idx, row in df.iterrows():
                rno = idx + 1
                party = row.get("Party Name", "")
                mobile = row.get("Mobile", "")
                email = row.get("Email", "")
                tree.insert("", "end", values=(rno, party, mobile, email))
            messagebox.showinfo("File Imported", f"Loaded {len(df)} records from {file_path}")
        except Exception as e:
            messagebox.showerror("Import Error", f"Could not read file:\n{e}")

def select_records():
    messagebox.showinfo("Select Records", "Records selected!")

def clear_fields():
    whatsapp_id_entry.delete(0, tk.END)
    from_rno_entry.delete(0, tk.END)
    to_rno_entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)
    message_var.set(0)

def send_whatsapp():
    messagebox.showinfo("Send WhatsApp", "WhatsApp message sent!")

def send_email():
    messagebox.showinfo("Send Email", "Email sent!")

# --- Main Window ---
root = tk.Tk()
root.title("SMS/Email Sales Marketing")
root.geometry("900x600")

# --- Top Frame ---
top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=8, pady=4)

# Import File Button (icon placeholder)
import_icon = tk.PhotoImage(width=32, height=32)  # Placeholder icon
import_btn = tk.Button(top_frame, image=import_icon, text="Import File", compound="left", command=import_file, width=110, height=32)
import_btn.grid(row=0, column=0, padx=(0, 10), pady=2, sticky="w")

# Radio Buttons
options = ["PET", "PSF", "FIBRE", "OTHER", "FABRIC", "RPP", "MBPE"]
radio_var = tk.StringVar(value=options[0])
for i, opt in enumerate(options):
    tk.Radiobutton(top_frame, text=opt, variable=radio_var, value=opt).grid(row=0, column=i+1, padx=2, sticky="w")

# --- Second Row: Red Label and WhatsApp ID ---
tk.Label(top_frame, text="Mobile No. must have ISD Code", fg="red").grid(row=1, column=0, columnspan=3, sticky="w", pady=(2,0))
tk.Label(top_frame, text="WhatsApp Instant ID=>").grid(row=1, column=3, sticky="e", padx=(30,2))
whatsapp_id_entry = tk.Entry(top_frame, width=30)
whatsapp_id_entry.grid(row=1, column=4, columnspan=3, sticky="w", padx=(0,2))

# --- Third Row: Record Selection ---
tk.Label(top_frame, text="Select records From RNo").grid(row=2, column=0, sticky="e", pady=(6,0))
from_rno_entry = tk.Entry(top_frame, width=7)
from_rno_entry.grid(row=2, column=1, sticky="w", pady=(6,0))
tk.Label(top_frame, text="To RNo").grid(row=2, column=2, sticky="e", pady=(6,0))
to_rno_entry = tk.Entry(top_frame, width=7)
to_rno_entry.grid(row=2, column=3, sticky="w", pady=(6,0))

select_btn = tk.Button(top_frame, text="Select Records", command=select_records, width=14)
select_btn.grid(row=2, column=4, padx=4, pady=(6,0))
clear_btn = tk.Button(top_frame, text="Clear", command=clear_fields, width=8)
clear_btn.grid(row=2, column=5, padx=4, pady=(6,0))

# --- Fourth Row: File Format Instruction ---
tk.Label(top_frame, text="(Exl File Format: Party Name, Mobile (with ISD 91), Email only)", fg="red").grid(row=3, column=0, columnspan=7, sticky="w", pady=(2,0))

# --- Table Frame ---
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=8, pady=(0,4))

# Table (Treeview)
global tree
columns = ("RNo", "Party Name", "Mobile No", "Email ID")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")
tree.pack(fill="both", expand=True)

# --- Bottom Frame ---
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill="x", padx=8, pady=4)

# Message Checkbox
message_var = tk.IntVar()
msg_checkbox = tk.Checkbutton(bottom_frame, text="Message", variable=message_var)
msg_checkbox.grid(row=0, column=0, sticky="nw", padx=(0,4))

# WhatsApp Send Button (icon placeholder)
wa_icon = tk.PhotoImage(width=24, height=24)  # Placeholder icon
wa_send_btn = tk.Button(bottom_frame, image=wa_icon, text="Send", compound="left", command=send_whatsapp, width=80)
wa_send_btn.grid(row=1, column=0, sticky="nw", pady=(2,2))

# Email Send Button (icon placeholder)
mail_icon = tk.PhotoImage(width=24, height=24)  # Placeholder icon
mail_send_btn = tk.Button(bottom_frame, image=mail_icon, text="Send", compound="left", command=send_email, width=80)
mail_send_btn.grid(row=2, column=0, sticky="nw", pady=(2,2))

# Message Text Area
message_text = tk.Text(bottom_frame, width=70, height=6)
message_text.grid(row=0, column=1, rowspan=3, padx=(10,0), pady=2, sticky="nsew")

# Allow resizing of message area
bottom_frame.grid_columnconfigure(1, weight=1)
bottom_frame.grid_rowconfigure(0, weight=1)

root.mainloop()



