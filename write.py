# 'Write'- A basic text editor in python 
# made using tkinter 

import tkinter as tk
from tkinter.filedialog import *

# Setting up the window
try:
    window=tk.Tk()
    window.minsize(800,500)
    window.title('Write')

    text=Text(window)
    text.pack(expand=True,fill=BOTH)

    # Defining Save,Open and New commands
    def save():
        file=open(asksaveasfilename(),'w')
        file.write(text.get('1.0',END+'-1c'))
        file.close()

    def my_open():
        file=open(askopenfilename(),'r')
        text.delete(1.0,END+'-1c')
        for line in file:
            text.insert(END,line)
        file.close()

    def new_file():
        text.delete(1.0,END+'-1c')

    # Adding required commands to the File menu
    file_menu=Menu(font=("open",10),tearoff=0)
    file_menu.add_command(label="New File",command=new_file)
    file_menu.add_command(label="Open File",command=my_open)
    file_menu.add_command(label="Save",command=save)

    main_menu=Menu()
    main_menu.add_cascade(label="File",menu=file_menu)

    # Main loop for the Editor
    window.config(menu=main_menu)
    window.mainloop()

except KeyboardInterrupt:
    quit()
