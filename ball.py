# ball.py — описує, як поводиться м’яч
import random


class Ball:
    def __init__(self, canvas, size=50):
        self.canvas = canvas
        self.size = size
        self.x = 0
        self.y = 0

        self.id = None

    def spawn(self):
        self.canvas.delete(self.id)
        width = int(self.canvas['width'])
        height = int(self.canvas['height'])
        # print(type(width), type(height))
        # print(type(self.size))

        self.x = random.randrange(0, width - self.size)
        self.y = random.randrange(0, height - self.size)

        self.id = self.canvas.create_oval(
            self.x, self.y,
            self.x + self.size, self.y + self.size,
            fill='red'
        )


class Ball_example(Ball):
    def __init__(self, canvas):
        self.canvas = canvas
        super().__init__(self.canvas)

    def spawn(self):
        self.canvas.delete(self.id)
        width = int(self.canvas['width'])
        height = int(self.canvas['height'])

        self.x = random.randrange(0, width - self.size)
        self.y = random.randrange(0, height - self.size)


        self.id = self.canvas.create_oval(
            self.x, self.y,
            self.x + self.size, self.y + self.size,
            fill='blue'
        )

    def is_clicked(self, click_x, click_y):   # порівняти координати
        return (self.x <= click_x <= self.x + self.size) and (self.y <= click_y <= self.y + self.size)
