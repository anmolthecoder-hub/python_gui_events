import tkinter as tk

def mouse_motion(event):
    print(f"Mouse at: x={event.x}, y={event.y}")

root = tk.Tk()
root.title("Mouse Motion Demo")

label = tk.Label(root, text="Move mouse over me", bg="yellow", width=30, height=5)
label.pack(pady=30)

# Binding the <Motion> event
label.bind("<Motion>", mouse_motion)

root.mainloop()
