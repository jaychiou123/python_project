from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    data = pandas.read_csv("germain_word_left.csv")
except:
    data = pandas.read_csv("./data/german_words.csv")
finally:
    ger_lists = data.to_dict(orient="records")



## button callback
def check_butt():
    global flip_timer
    try:
        window.after_cancel(flip_timer)
    except:
        pass
    ger_lists.remove(n_pick)
    remaining = pandas.DataFrame(ger_lists)
    remaining.to_csv("germain_word_left.csv", index=False)
    print(len(ger_lists))
    flip_card_to_front()
    flip_timer = window.after(3000, func=flip_card_to_back)

def unseen_butt():
    flip_card_to_front()

## Flip the card
def flip_card_to_back():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(canvas_language, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=n_pick["english"], fill="white")

def flip_card_to_front():
    global n_pick
    n_pick = random.choice(ger_lists)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(canvas_language, text="German", fill="black")
    canvas.itemconfig(canvas_word, text=n_pick["germany"], fill="black")



## Canvas setup
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas_language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



## button setup
check = PhotoImage(file="./images/right.png")
known = Button(image=check, highlightthickness=0, command=check_butt)
known.grid(column=1, row=1)
cross = PhotoImage(file="./images/wrong.png")
unseen = Button(image=cross, highlightthickness=0, command=unseen_butt)
unseen.grid(column=0, row=1)

flip_card_to_front()
window.after(3000, func=flip_card_to_back)







window.mainloop()
