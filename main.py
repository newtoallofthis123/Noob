from tkinter import *
import cliTools

gui = Tk()
gui.title("Noob")
gui.geometry("300x300")

menu = Menu(gui)
gui.config(menu=menu)

cli_tools = Menu(menu, tearoff=False)
menu.add_cascade(label="Cli Tools", menu=cli_tools)
cli_tools.add_command(label="Wikid", command=cliTools.wikid)

gui.mainloop()
