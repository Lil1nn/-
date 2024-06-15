import tkinter as tk
from tkinter import ttk


def on_sign_up():
    print("Sign Up button clicked")


def on_sign_in():
    print("Sign In button clicked")


# Create the main window
root = tk.Tk()
root.title("Sign Up")
root.geometry("300x400")
root.configure(bg='#2C2F33')

# Create and place the labels and entries
fields = ['Username', 'Email', 'Password', 'Retype password']
entries = {}

for idx, field in enumerate(fields):
    label = tk.Label(root, text=field, bg='#2C2F33', fg='white', anchor='w')
    label.place(x=30, y=30 + idx * 60, width=240, height=20)

    entry = ttk.Entry(root, show='*' if 'Password' in field else '')
    entry.place(x=30, y=50 + idx * 60, width=240, height=25)
    entries[field] = entry

# Terms and policies checkbox
terms_var = tk.IntVar()
terms_check = tk.Checkbutton(root, text="Accept the terms and policies", variable=terms_var, bg='#2C2F33', fg='white')
terms_check.place(x=30, y=270, width=240, height=20)

# Sign Up button
sign_up_btn = tk.Button(root, text="SIGN UP", bg='#00BFFF', fg='white', command=on_sign_up)
sign_up_btn.place(x=30, y=300, width=240, height=30)

# Sign In button
sign_in_label = tk.Label(root, text="Already have an account?", bg='#2C2F33', fg='white')
sign_in_label.place(x=80, y=340, width=150, height=20)

sign_in_btn = tk.Button(root, text="SIGN IN", bg='#696969', fg='white', command=on_sign_in)
sign_in_btn.place(x=30, y=360, width=240, height=30)

# Start the main event loop
root.mainloop()
