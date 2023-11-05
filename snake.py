from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Snake Game")

frm = Frame(root)
frm.grid(padx=10, pady=10)

image = Image.open("C:\\Users\\Користувач\\tkinter\\snake.JPG")
photo = ImageTk.PhotoImage(image)

label = Label(frm, image=photo)
label.grid(column=0, row=1, columnspan=2, rowspan=2)

label_text = Label(frm, text="Snake", font=("Time New Roman", 50))
label_text.grid(column=0, row=0, columnspan=2)

button_exit = Button(frm, text="EXIT", command=root.destroy, bg="black", fg="white", relief="flat", font=("Time New Roman", 20))
button_exit.grid(column=0, row=3, columnspan=2)

button_level1 = Button(frm, text="LEVEL 1", command=root.destroy, bg="black", fg="white", relief="flat", font=("Time New Roman", 20))
button_level1.place(relx=0.85, rely=0.2, anchor="center")

button_level2 = Button(frm, text="LEVEL 2", command=root.destroy, bg="black", fg="white", relief="flat", font=("Time New Roman", 20))
button_level2.place(relx=0.80, rely=0.3, anchor="center")

button_level3 = Button(frm, text="LEVEL 3", command=root.destroy, bg="black", fg="white", relief="flat", font=("Time New Roman", 20))
button_level3.place(relx=0.75, rely=0.4, anchor="center")

button_free_play = Button(frm, text="FREE PLAY", command=root.destroy, bg="black", fg="white", relief="flat", font=("Time New Roman", 20))
button_free_play.place(relx=0.71, rely=0.5, anchor="center")

root.mainloop()