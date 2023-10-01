import pathlib
import random
import pyperclip
import tkinter.messagebox
from tkinter import *

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!',
              '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
              '[', ']', '^', '_', '`', '{', '|', '}', '~']


def generateRandomPassword():
    passwordInput.delete(0, END)
    password = ""
    for i in range(1,15):
        randomIndex = random.randint(0, 92)
        password += characters[randomIndex]
    passwordInput.insert(0, password)
    pyperclip.copy(password)


def addToData():
    if websiteInput.get() != "" and usernameInput.get() != "" and passwordInput.get() != "":

        savePrompt = tkinter.messagebox.askokcancel(title=websiteInput.get(),
                                                    message="Details entered:\n"
                                                    f"Email/Username: {usernameInput.get()}\n"
                                                    f"Password: {passwordInput.get()}\n"
                                                    f"Do you want to save?")

        if savePrompt:
            with open(pathlib.Path(__file__).parent/"data.txt", "a") as data:
                data.write(f"{websiteInput.get()} | {usernameInput.get()} | {passwordInput.get()}" + "\n")
            tkinter.messagebox.showinfo(message="Password has been copied to the clipboard.")

        websiteInput.delete(0, END)
        usernameInput.delete(0, END)
        passwordInput.delete(0, END)

    else:
        print("Error, please fill all of the fields")
        tkinter.messagebox.showerror(title="Missing data!",
                                     message="Missing data!\nMake sure to fill out all of the fields.")


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logoImg = PhotoImage(file=pathlib.Path(__file__).parent/"logo.png")
canvas.create_image(100, 100, image=logoImg)
canvas.grid(column=1, row=0)

websiteLabel = Label(text="Website:")
websiteLabel.grid(column=0, row=1, columnspan=1, sticky="E", padx=2, pady=2)

websiteInput = Entry()
websiteInput.grid(column=1, row=1, columnspan=2, sticky="EW", padx=2, pady=2)

usernameLabel = Label(text="Email/Username:")
usernameLabel.grid(column=0, row=2, columnspan=1, sticky="E", padx=2, pady=2)

usernameInput = Entry()
usernameInput.grid(column=1, row=2, columnspan=2, sticky="EW", padx=2, pady=2)

passwordLabel = Label(text="Password:")
passwordLabel.grid(column=0, row=3, columnspan=1, sticky="E", padx=2, pady=2)

passwordInput = Entry()
passwordInput.grid(column=1, row=3, columnspan=1, sticky="EW", padx=2, pady=2)

generatePasswordBtn = Button(text="Generate Password", command=generateRandomPassword)
generatePasswordBtn.grid(column=2, row=3, columnspan=1, sticky="EW", padx=2, pady=2)

addBtn = Button(text="Add", command=addToData)
addBtn.grid(column=1, row=4, columnspan=2, sticky="EW", padx=2, pady=2)

window.mainloop()
