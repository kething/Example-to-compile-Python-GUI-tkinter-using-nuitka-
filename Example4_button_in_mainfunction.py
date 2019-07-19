import tkinter as tk
from tkinter import messagebox    


def quit():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy() 

def write_slogan():
    print("Tkinter is easy to use!")
    
    
if __name__=='__main__':
    
    root = tk.Tk()

    root.geometry("200x200")
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, 
                       text="QUIT", 
                       fg="red",
                       command=quit)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                      text="Hello",
                      command=write_slogan)
    slogan.pack(side=tk.LEFT)
    root.mainloop()
