import tkinter
#Kwargs / Keyword Arguments are used in entire Project as Tkinter works on kwargs Inputs
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=300, height=500)
window.config(padx=100,pady=100)
#padding for entire window
label = tkinter.Label(text="I am a Label", font=("Calibri", 24, "bold"))
label.place(x=110, y=233)
label.grid(column=0, row=0)
#variable_name.pack() is used to display the Label (Text on Screen)
#label.pack()
#_tkinter.TclError: cannot use geometry manager pack inside . which already has slaves managed by grid {cannot use pack and grid at the same time,choose between one}
#label.pack(side="right")
#Modify / Replace Old Text
label.config(text="Hello")


def button_clicked():
    print("I got Clicked")
    label.config(text="Yayy!!! I got Clicked")


#command keyword is used to call a function defined
button = tkinter.Button(text="Pls Click me", font=(
    "Calibri", 18, "italic"), command=button_clicked)
#button.pack()
button.grid(column=1, row=1)


input = tkinter.Entry(width=20)
#input.pack()
input.grid(column=2, row=2)


def inputs():
    print(input.get())
    label.config(text=input.get())


button2 = tkinter.Button(text="I am a Button", font=(
    "Calibri", 18, "italic"), command=inputs)
button2.grid(column=3, row=3)


window.mainloop()
