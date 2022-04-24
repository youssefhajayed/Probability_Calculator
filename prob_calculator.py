import copy
import random


# Consider using the modules imported above.

class Hat:
    contents = []

    def __init__(self, **kwargs):

        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)



    def draw(self, number):
        output = []

        if number >= len(self.contents):
            return self.contents
        output = random.sample(self.contents, number)

        for i in output:
            for j in self.contents:
                if i == j:
                    self.contents.remove(i)
                    break

        return output


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    valid_experiment = 0

    temp = copy.copy(hat.contents)

    for i in range(num_experiments):
        balls_draw = hat.draw(num_balls_drawn)
        items = 0

        for k, v in expected_balls.items():

            comparison = 0
            for j in range(len(balls_draw)):

                if balls_draw[j] == k:
                    comparison = comparison + 1

                if comparison == v:
                    items = items + 1
                    break

        if items == len(expected_balls):
            valid_experiment = valid_experiment + 1

        hat.contents = copy.copy(temp)

    return valid_experiment / num_experiments
