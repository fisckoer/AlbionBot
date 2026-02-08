import math
import time
import random

class Navigator:

    def __init__(self, controller, max_val):
        self.controller = controller
        self.max_val = max_val

        self.angle = 0.0
        self.angle_step = math.pi / 6
        self.move_duration = 1.2

    def move_interruptible(self, stop_flag):
        step_time = 0.1
        steps = 5 #int(self.move_duration / step_time)

        x = int(math.cos(self.angle) * self.max_val)
        y = int(math.sin(self.angle) * self.max_val)

        for _ in range(steps):
            if stop_flag():
                self.controller.release_left_stick()
                return

            self.controller.move_left_stick(x, y)
            time.sleep(step_time)

        self.controller.release_left_stick()

    def rotate(self):
        self.angle += math.pi/random.randint(1, 6)
        if self.angle >= math.tau:
            self.angle = 0.0
