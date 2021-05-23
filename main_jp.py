from json.decoder import JSONDecodeError
from json.encoder import JSONEncoder
import tkinter
from tkinter.constants import CENTER
import tkinter.messagebox as messagebox
import random
import pyperclip
import json
from PIL import Image, ImageTk
import pandas as pd
import numpy as np

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# df = pd.read_csv("french_words.csv")
df = pd.read_csv("Japanese_top_20_tourist_words.csv")
temp_answer = ""

# Flip Cards -----------
def GenerateNewCard():
    global df, temp_answer
    select_row_number = np.random.randint(0, df.shape[0])
    select_row = df.iloc[select_row_number]
    question_word = select_row['Japanese']
    temp_answer = select_row['English']
    pronounce_word = select_row['Pronounce']
    
    reconstructed_question_word = question_word + "\n" + pronounce_word
    
    canvas1.itemconfig(question_text, text= reconstructed_question_word, font=('Ariel',15,'italic'))
    canvas2.itemconfig(answer_text, text="")
    # canvas2.itemconfig(answer_text, text= answer_word)

def GetAnswer():
    global temp_answer
    canvas2.itemconfig(answer_text, text= temp_answer, font=('Ariel',15,'bold'))


# UI Design ------------
window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50)


word_frame = Image.open("quote-template2.png")
word_frame = word_frame.resize((500,500))
word_frame = ImageTk.PhotoImage(word_frame)
button = tkinter.Button(image = word_frame, highlightthickness=0, command= GetAnswer)
button.grid(row=0, column=0, columnspan=2)

canvas1 = tkinter.Canvas(width= 300, height= 70, highlightthickness=0)
question_text = canvas1.create_text(150, 30, text= "Yes to start", font=('Ariel',25,'italic'))
canvas1.place(relx= 0.57, rely = 0.35, anchor=CENTER)

canvas2 = tkinter.Canvas(width= 300, height= 50, highlightthickness=0)
answer_text = canvas2.create_text(150, 20, text= "", font=('Ariel',25,'bold'))
canvas2.place(relx= 0.48, rely = 0.53, anchor=CENTER)


wrong_button = tkinter.Button(text="No", command=GenerateNewCard)
wrong_button.grid(row=1, column=0)

correct_button = tkinter.Button(text="Yes", command=GenerateNewCard)
correct_button.grid(row=1, column=1)



window.mainloop()
