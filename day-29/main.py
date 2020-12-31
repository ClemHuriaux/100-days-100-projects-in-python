from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator(length=16):
    if len(input_password.get()):
        input_password.delete(0, "end")
    printable = f'{string.ascii_letters}{string.digits}{string.punctuation}'
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    input_password.insert(0, random_password)
    pyperclip.copy(random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    entries = (input_website.get(), input_email_user.get(), input_password.get())
    to_save = f"{entries[0]} | {entries[1]} | {entries[2]}"

    for entry in entries:
        if not len(entry):
            messagebox.showwarning(title="Nope", message="Please fill all fields !")
            return

    answer = messagebox.askokcancel(title=entries[0], message=f"These are the details entered: \nEmail: {entries[1]} "
                                                              f"\nPassword: {entries[2]} \nIs it ok to save?")
    if answer:
        delete()
        with open("data.txt", "a+") as f:
            f.write(f"{to_save}\n")


def delete():
    input_website.delete(0, 'end')
    input_password.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
email_user_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(column=0, row=1)
email_user_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

input_website = Entry(width=35)
input_email_user = Entry(width=35)
input_password = Entry(width=21)

input_website.grid(column=1, row=1, columnspan=2)
input_email_user.grid(column=1, row=2, columnspan=2)
input_password.grid(column=1, row=3)
input_website.focus()
input_email_user.insert(0, "clem@mail.com")
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
