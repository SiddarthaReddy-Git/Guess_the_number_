import tkinter as tk
import random
from tkinter import simpledialog, messagebox
number = random.randint(1, 100)
messagebox.showinfo("Guess","Guess the number between 1 to 100 : ")
turns = 0
while True:
    guess = simpledialog.askinteger("input","what is your number : ")
    if guess < number:
        messagebox.showwarning("incorrect","Too low try again")
        turns +=1
    elif guess > number:
        messagebox.showwarning("incorrect","Too high try again")
        turns +=1
    else:
        messagebox.showinfo("correct","great u guessed it right...")
        turns +=1
        break
if turns <= 5:
    messagebox.showinfo("complete","you won")
    messagebox.showinfo("complete","number of turns : "+str(turns))
    if turns > 5:
        messagebox.showinfo("out of guesses...")
        messagebox.showinfo("complete","you lose")
        messagebox.showinfo("complete","number of turns : "+str(turns))
        
else:
    messagebox.showwarning("Invalid","Invalid input")
    