from random import choice

from tensorflow.python.ops.summary_ops_v2 import get_step


class RandomWalk:
    '''A class that generates random walks'''

    def __init__(self, num_points=5000):
        self.num_points = num_points
        '''all randomwalk start at point(0,0)'''
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        return direction * distance

    def generate(self):
        '''generates random walks'''
        while len(self.x_values) < self.num_points:
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            x_step = self.get_step()

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:  # 拒绝原地踏步
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
