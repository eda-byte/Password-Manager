from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pw_box.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_input.get()
    username=username_input.get()
    password=pw_box.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"The details entered:\nWebsite: {website}\nEmail: {username}\nPassword: {password}\nIs it OK to save them?")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {username} | {password}\n")
            website_input.delete(0, 'end')
            username_input.delete(0, 'end')
            pw_box.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(width=200,height=200,highlightthickness=0)
pass_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)
canvas.grid(column=1,row=0)

#Buttons
add_button=Button(text="Add",highlightthickness=0,width=36,command=save )
add_button.grid(column=1,row=4,columnspan=2)#
generate_pw_button=Button(text="Generate Password",highlightthickness=0,command=generate_password)
generate_pw_button.grid(column=2,row=3)#
#Labels
website_label= Label(text="Website:" ,highlightthickness=0 )
website_label.grid(column=0,row=1)

username_label= Label(text="Email/Username:",highlightthickness=0 )
username_label.grid(column=0,row=2)

pw_label= Label(text="Password:",highlightthickness=0 )
pw_label.grid(column=0,row=3)
#Entries
website_input = Entry(width=38)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()

username_input = Entry(width=38)
username_input.grid(column=1,row=2,columnspan=2)
username_input.insert(0,"eda.oz@tutamail.com")
pw_box = Entry(width=21)
pw_box.grid(column=1,row=3)

 



window.mainloop()