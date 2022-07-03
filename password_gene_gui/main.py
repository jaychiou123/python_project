from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    entry_3.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }
    filled_flag = False
    if len(website) == 0 or len(password) ==0:
        messagebox.showerror(title="Error", message="At least one information is not given.")
    else:
        try:
            with open("data.json", 'r') as data_file:
                dict_data = json.load(data_file)
                dict_data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(dict_data, data_file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            entry_3.delete(0, END)
            entry_1.delete(0, END)
# ----------------------------------------------------------------------#
def search_pass():
    website = entry_1.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
    messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_1 = Label(text="Website:")
label_1.grid(column=0, row=1)
label_2 = Label(text="Email/Username:")
label_2.grid(column=0, row=2)
label_3 = Label(text="Password:")
label_3.grid(column=0, row=3)

entry_1 = Entry(width=20)
entry_1.grid(column=1, row=1)
entry_1.focus()
entry_2 = Entry(width=36)
entry_2.grid(column=1, row=2, columnspan=2)
entry_2.insert(0, "example@gmail.com")
entry_3 = Entry(width=20)
entry_3.grid(column=1, row=3)

button_gen = Button(text="Generate Password", command=generate_password)
button_gen.grid(column=2, row=3)
button_add = Button(text="Add", width=36, command=save_data)
button_add.grid(column=1, row=4, columnspan=2)
button_search = Button(text="Search", width=13, command=search_pass)
button_search.grid(column=2, row=1)











window.mainloop()