from tkinter import *

window=Tk()
window.title("tkinter Window")
window.geometry("400x400")

information=Label(text="Hello, My name is Meghana", fg="orange", bg="lightblue")
button=Button(text="Click Me!", fg="black", bg="white")
entry=Entry(fg="black", bg="lightgreen", width=75)
frame=Frame(master=window, relief=RAISED, borderwidth="3")
label=Label(master=frame, text="Tkinter Window_Sample1")
textbox=Text(fg="brown", bg="green")

information.pack()
button.pack()
entry.pack()
frame.pack()
label.pack()
textbox.pack()

window.mainloop()
