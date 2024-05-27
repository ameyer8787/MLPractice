from tkinter import *
import time

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editMenu)

        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        fileMenu.add_command(label="Undo")
        fileMenu.add_command(label="Redo")

        self.label = Label(text="", fg="Red", font=("Georgia", 20))
        self.label.place(x=50, y=80)
        self.update_clock()

        #widgent can take all window
        self.pack(fill=BOTH, expand=1)

        #create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)

        # place buttona at (0,0)
        exitButton.place(x=0, y=0)

    def clickExitButton(self):
        exit()

    def exitProgram(self):
        exit()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)



root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("320x200")
root.after(1000, app.update_clock)
root.mainloop()