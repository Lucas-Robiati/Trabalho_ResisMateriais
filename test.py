import tkinter as tk
from tkinter import ttk


def createmenu(win):
    top = tk.Menu(win)
    win.config(menu=top)
    file = tk.Menu(top)
    file.add_command(label='Quit', command=win.quit, underline=0)
    top.add_cascade(label='File', menu=file, underline=0)


def panels(parent):
    n = ttk.Notebook(parent)
    n.pack(fill = tk.BOTH, expand=True, **mainframe_defaults)
    f1 = ttk.Frame(n)
    f2 = ttk.Frame(n)

    n.add(f1, text='Mods')
    n.add(f2, text='Modfiles')

    tree = ttk.Treeview(f1, columns=('mod_id', 'version', 'category_id', 'insert_timestamp'))
    tree.grid(row=4, columnspan=6, sticky='nsew')
    tree.insert(
        '',
        'end',
        iid='id1',
        text='sometext',
        values=(12, 24, 35, 67)
    )
    f1.grid_columnconfigure(0, weight=1)
    f1.grid_rowconfigure(4, weight=1)


root = tk.Tk()
root.title("Xyrim")
root.geometry("")
print("Windowing system: " + root.tk.call('tk', 'windowingsystem'))

root.option_add('*tearOff', False)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky='nswe')
mainframe_defaults = {
    'padx' : 5,
    'pady' : 5}

createmenu(root)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

panels(mainframe)
