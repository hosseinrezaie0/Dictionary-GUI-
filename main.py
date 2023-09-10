#Import Modules
import googletrans
import pyttsx3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyperclip



#-----------------------------------UI-----------------------------------#
root = ttk.Window(themename="superhero")
root.title("Dictionary")
root.geometry("500x500")
# root.config(padx=20,pady=20)

label = ttk.Label(text="German to English",font=("Arial",25))
label.grid(row=0,column=1,columnspan=6)





root.mainloop()



