#import tkinter as tk
#root = tk.Tk()

from tkinter import *
from ball import Ball_example


# import random   #випадкові числа

#
# class Ball:
#     def __init__(self, canvas, size=50):
#         self.canvas = canvas
#         self.size = size
#         self.x = 0
#         self.y = 0
#
#         self.id = None
#
#     def spawn(self):
#         self.canvas.delete(self.id)   #видаляє м’яч (графічний об’єкт) з полотна.
#         width = int(self.canvas['width'])
#         height = int(self.canvas['height'])  # отримуємо розміри полотна в пікселях як числа
#         # print(type(width), type(height))
#         # print(type(self.size))
#
#
#         self.x = random.randrange(0, width - self.size)  # випадкові координати м'яча щоб він не виходив за границю полотна
#         self.y = random.randrange(0, height - self.size)
#
#
#         self.id = self.canvas.create_oval(    # self.id - зберігає ID цього круга, щоб його можна було потім змінювати або видалити.
#             self.x, self.y,
#             self.x + self.size, self.y + self.size,  # координата + розмір м'яча
#             fill='red'
#         )

class Game:
    def __init__(self, root):    #конструктор класу Game
        self.root = root         # зберігає головне вікно
        self.root.title("Catch Ball")
        self.score = 0
        self.timer_left = 10


        self.canvas = Canvas(root, width=400, height=300, bg="white")   # біле полотно розміром 400×300
        self.canvas.pack()

        self.score_label = Label(root, text="Score: 0", font="Arial, 16")
        self.score_label.pack()

        self.time_label = Label(root, text="Time: 20", font="Arial, 16")
        self.time_label.pack()


        self.canvas.bind("<Button-1>", self.on_click)  # 1. найменування кнопки  2. ім'я функції

        self.ball = Ball_example(self.canvas)
        self.ball.spawn()

        self.entry = None
        self.save_button = None
        self.result_label = None

        self.update_timer()  # запускаємо таймер



#       self.root.after(1000,self.ball.spawn()) # 1000 сек затримки
#       self.root.after(2000, self.ball.spawn())
#       self.root.after(3000, self.ball.spawn())



    def on_click(self, event):  # on_click - method
        # print(event.x, event.y)  #викликали координати
        if self.ball.is_clicked(event.x, event.y):
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.ball.spawn()



    def update_timer(self):

        if self.timer_left > 0:
            self.timer_left -= 1
            self.time_label['text'] = f"Time :{self.timer_left}"
            self.ball.spawn()                  # з'являється кулька в новому місці
            self.canvas.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.create_text(200, 120, text="Game over, baby", font=("Arial", 20), fill="green")
        self.canvas.create_text(200, 150, text=f"Score: {self.score}", font=("Arial", 14))

        # Entry для введення імені
        Label(self.root, text="Введіть ваше ім'я:").pack()
        self.entry = Entry(self.root)
        self.entry.pack()

        # Кнопка збереження
        self.save_button = Button(self.root, text="Зберегти результат", command=self.save_result)
        self.save_button.pack()

    def save_result(self):
            name = self.entry.get().strip()
            if name:
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"{name},{self.score}\n")
                self.entry.destroy()
                self.save_button.destroy()
                self.show_results()

    def show_results(self):
        try:
            with open("results.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            lines = []

        results = [line.strip().split(",") for line in lines if "," in line]
        results.sort(key=lambda x: int(x[1]), reverse=True)

        result_text = "🏆 Результати:\n"
        for i, (name, score) in enumerate(results[:5], 1):  # топ-5
            result_text += f"{i}. {name}: {score}\n"

        self.result_label = Label(self.root, text=result_text, font=("Arial", 12), justify=LEFT)
        self.result_label.pack()



if __name__ == "__main__": # чи співпадає ім'я запущеного файлу із зараз
    root = Tk()
    game = Game(root)
    root.mainloop()
    # game.on_click()   # виклик методу click у об'єкта game
    # game.canvas       # метод для обробки кліку миші










