#Import Modules
import googletrans
import pyttsx3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyperclip



#-----------------------------------UI-----------------------------------#
root = ttk.Window(themename="superhero")
root.title("Dictionary")
root.geometry("870x700")
root.resizable(0,0)
# root.config(padx=50)

# label = ttk.Label(text="German to English",font=("Arial",25))
# label.grid(row=0,column=0,columnspan=2)

canavs = ttk.Canvas(width=256,height=256)
file = ttk.PhotoImage(file="logo.png")
canavs.create_image(128,128,image=file)
canavs.place(x=0,y=0)

du_label = ttk.Label(text="German",width=50)
du_label.place(x=50,y=200)
input_text = ttk.Text(wrap=ttk.WORD,height=10,width=25)
input_text.place(x=50,y=250)

en_label = ttk.Label(text="English")
en_label.place(x=500,y=200)
output_text = ttk.Text(wrap=WORD,height=10,width=25)
output_text.place(x=500,y=250)

translate_btn = ttk.Button(text="Translate", bootstyle="success")
translate_btn.place(x=380,y=600)


root.mainloop()



