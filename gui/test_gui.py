import tkinter as tk

root = tk.Tk()
root.title("Example GUI")

label = tk.Label(root, text="Hello, my name is Tkinter")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit")
button.pack()

def event_handle():
    content = entry.get()
    label.config(text="Hello, " + content + "!")

button.config(command=event_handle)

if __name__ == '__main__':
    root.mainloop()