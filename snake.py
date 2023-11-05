import tkinter as tk
from PIL import Image, ImageTk
import random

class SnakeGame:
    def __init__(self, root, snake_speed):
        self.root = root
        self.root.title("Snake Game")
        self.root.geometry("1000x800")

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.label_score = tk.Label(self.root, text="Score: 0", font=("Arial", 14))
        self.label_score.pack()

        self.label_length = tk.Label(self.root, text="Length: 1", font=("Arial", 14))
        self.label_length.pack()

        self.snake_speed = snake_speed
        self.snake = [(5, 5)]
        self.food = (10, 10)
        self.score = 0
        self.snake_length = 1
        self.boundaries = (0, 0, 40, 30)

        self.direction = "Right"

        self.update_game()

    def update_game(self):
        self.update_snake()
        self.label_length.config(text=f"Length: {self.snake_length}")

        if self.food is None:
            self.food = self.generate_food()

        if self.snake[0] == self.food:
            self.food = None
            self.snake.append(self.snake[-1])
            self.score += 1
            self.snake_length += 1
            self.label_score.config(text=f"Score: {self.score}")
            self.label_length.config(text=f"Length: {self.snake_length}")

        # Додана перевірка на зіткнення з рамками
        if self.is_collision_with_boundaries():
            self.end_game()

        self.canvas.delete("all")


        self.canvas.create_rectangle((0, 0, 800, 600), outline="black",width=10)

        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="green")

        if self.food:
            x, y = self.food
            self.canvas.create_oval(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="red")

        self.root.after(int(1000 / self.snake_speed), self.update_game)

    def generate_food(self):
        while True:
            x = random.randint(1, 38)
            y = random.randint(1, 28)
            if (x, y) not in self.snake:
                return x, y

    def update_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Right":
            new_head = (head_x + 1, head_y)
        elif self.direction == "Left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 1)

        self.snake = [new_head] + self.snake[:-1]

    def on_key_press(self, event):
        if event.keysym == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif event.keysym == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif event.keysym == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif event.keysym == "Down" and self.direction != "Up":
            self.direction = "Down"

    # Додана функція перевірки на зіткнення з рамками
    def is_collision_with_boundaries(self):
        head_x, head_y = self.snake[0]
        return (head_x < self.boundaries[0] or head_x >= self.boundaries[2] or
                head_y < self.boundaries[1] or head_y >= self.boundaries[3])


    def end_game(self):
        self.root.after_cancel(self.root.after_id)
        self.canvas.delete("all")
        game_over_label = tk.Label(self.root, text="Game Over", font=("Arial", 24))
        game_over_label.place(x=400, y=300, anchor="center")



def show_level1_page():
    global level1_window
    level1_window = tk.Tk()
    level1_window.title("LEVEL 1")
    level1_window.geometry("1000x800")

    back_button = tk.Button(level1_window, text="Back", command=level1_window.destroy)
    back_button.pack()

    game = SnakeGame(level1_window, 5)

    level1_window.bind("<KeyPress>", game.on_key_press)
    level1_window.focus_set()

def show_level2_page():
    global level2_window
    level2_window = tk.Tk()
    level2_window.title("LEVEL 2")
    level2_window.geometry("800x600")

    back_button = tk.Button(level2_window, text="Back", command=level2_window.destroy)
    back_button.pack()

    game = SnakeGame(level2_window, 10)

    level2_window.bind("<KeyPress>", game.on_key_press)
    level2_window.focus_set()

def show_level3_page():
    global level3_window
    level3_window = tk.Tk()
    level3_window.title("LEVEL 3")
    level3_window.geometry("800x600")

    back_button = tk.Button(level3_window, text="Back", command=level3_window.destroy)
    back_button.pack()

    game = SnakeGame(level3_window, 20)

    level3_window.bind("<KeyPress>", game.on_key_press)
    level3_window.focus_set()

def show_free_play_page():
    global free_play_window
    free_play_window = tk.Tk()
    free_play_window.title("FREE PLAY")
    free_play_window.geometry("800x600")

    back_button = tk.Button(free_play_window, text="Back", command=free_play_window.destroy)
    back_button.pack()

    game = SnakeGame(free_play_window, 40)

    free_play_window.bind("<KeyPress>", game.on_key_press)
    free_play_window.focus_set()

def show_main_page():
    global level1_window, level2_window, level3_window, free_play_window
    if level1_window:
        level1_window.destroy()
    if level2_window:
        level2_window.destroy()
    if level3_window:
        level3_window.destroy()
    if free_play_window:
        free_play_window.destroy()

root = tk.Tk()
root.title("Snake Game")

frm = tk.Frame(root)
frm.grid(padx=10, pady=10)

image = Image.open("C:\\Users\\Користувач\\tkinter\\snake.JPG")
photo = ImageTk.PhotoImage(image)

label = tk.Label(frm, image=photo)
label.grid(column=0, row=1, columnspan=2, rowspan=2)

label_text = tk.Label(frm, text="Snake", font=("Time New Roman", 50))
label_text.grid(column=0, row=0, columnspan=2)

button_exit = tk.Button(frm, text="EXIT", command=root.destroy, bg="black", fg="white", relief="flat", font=("Time New Roman", 20))
button_exit.grid(column=0, row=3, columnspan=2)

button_level1 = tk.Button(frm, text="LEVEL 1", command=show_level1_page, bg="black", fg="white", relief="flat", font=("Time New Roman", 20))
button_level1.place(relx=0.85, rely=0.2, anchor="center")

button_level2 = tk.Button(frm, text="LEVEL 2", command=show_level2_page, bg="black", fg="white", relief="flat", font=("Time New Roman", 20))
button_level2.place(relx=0.80, rely=0.3, anchor="center")

button_level3 = tk.Button(frm, text="LEVEL 3", command=show_level3_page, bg="black", fg="white", relief="flat", font=("Time New Roman", 20))
button_level3.place(relx=0.75, rely=0.4, anchor="center")

button_free_play = tk.Button(frm, text="Crazy PLAY", command=show_free_play_page, bg="black", fg="white", relief="flat", font=("Time New Roman", 20))
button_free_play.place(relx=0.71, rely=0.5, anchor="center")

root.mainloop()