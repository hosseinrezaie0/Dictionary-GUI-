#Import Modules
import googletrans
import pyttsx3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyperclip



#-----------------------------------UI-----------------------------------#
root = ttk.Window(themename="superhero")
root.title("Dictionary")
root.geometry("700x700")
# root.config(padx=20,pady=20)

# label = ttk.Label(text="German to English",font=("Arial",25))
# label.grid(row=0,column=0,columnspan=2)

canavs = ttk.Canvas(width=256,height=256)
file = ttk.PhotoImage(file="logo.png")
img = canavs.create_image(128,128,image=file)
canavs.grid(row=0,column=0)





root.mainloop()



