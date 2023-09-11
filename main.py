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
# du_text = ttk.ScrolledText(root, wrap=ttk.WORD,
#                                       width=20, height=8,
#                                       font=("Times New Roman", 15))
  
# du_text.grid(row=2,column=0,sticky="w")


# en_label = ttk.Label(text="English",width=50)
# en_label.grid(row=1,column=2)

# en_text = ttk.ScrolledText(root, wrap=ttk.WORD,
#                                       width=20, height=8,
#                                       font=("Times New Roman", 15))
  
# en_text.grid(row=2,column=2,sticky="w")



# du_text.focus()
root.mainloop()



