from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generat_password():
    password_letters=[random.choice(letters) for _ in range(random.randint(8, 10))]
    pssword_symbols=[random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers=[random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list=password_numbers+password_letters+pssword_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    en3.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = en1.get()
    passowrd=en2.get()
    em=en3.get()
    if len(website)==0 or len(passowrd)==0 or len(em)==0:
        messagebox.showerror(title="error",message="ther is a filed you didn't fill")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"these are details enterd:\nEmail:{em}\nPassword:{passowrd}\n is it ok?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}|{passowrd}|{em}\n")
                en1.delete(0, END)
                en2.delete(0, END)
                en3.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
windos=Tk()
windos.title("password")
windos.config(padx=50,pady=50)
windos.minsize(width=800,height=600)
canavas=Canvas(width=200, height=200)
image=PhotoImage(file="logo.png")
canavas.create_image(100,100,image=image)
canavas.grid(column=10,row=2)
web=Label(text="Web")
web.grid(column=9,row=5)
en1=Entry(width=35)



en1.grid(column=10,row=5,columnspan=4)
en1.focus()

email=Label(text="email/username")
email.grid(column=9,row=6)
en2=Entry(width=35)
en2.insert(0,"angela@.com")
en2.grid(column=10,row=6,columnspan=5)
pas=Label(text="password")
pas.grid(column=9,row=7)
en3=Entry(width=21)
en3.grid(column=10,row=7)
gen_pass=Button(text="generate password",command=generat_password)
gen_pass.grid(column=13,row=7)
add_pass=Button(text="add",width=36,command=add)
add_pass.grid(row=8,column=10,columnspan=5)

windos.mainloop()