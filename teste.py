import tkinter as tk

def on_resize(event):
    width = event.width
    height = event.height
    print(f"Window resized to: width={width}, height={height}")

root = tk.Tk()
root.title("Resize Signal Example")

root.bind("<Configure>", on_resize)

# Making the window resizable
root.resizable(True, True)

root.mainloop()
