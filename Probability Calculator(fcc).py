import random
import copy

class Hat:
    def __init__(self, **balls):
        self.balls = balls
        self.contents = []
        # the self.contents list will be used later in the other methods
        # the classes argument needs to be a **kwargs so it is a variable number and registered as dict

        for k, v in self.balls.items():
            for i in range(v):
                self.contents.append(k)
                # add each ball to the self.contents(as many times as it equal to) 
                
    def draw(self, number_draw):
        # creating the draw method
        balls_drawn = []

        if number_draw > len(self.contents):
            balls_drawn = self.contents[:]
            return balls_drawn
            # return all balls if the draws are greater than the total balls amount
            
        for i in range(number_draw):
            r = random.randint(0, len(self.contents) - 1)
            balls_drawn.append(self.contents[r])
            del self.contents[r]

        return balls_drawn
        # return the balls that have been drawn 


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # creating the experiment function
    M = 0
    # M will represent the times the key draw happended 

    for i in range(num_experiments):
        c_hat = copy.deepcopy(hat)
        ch = c_hat.draw(num_balls_drawn)
        m = []

        for item in expected_balls:
            m.append(expected_balls[item] <= ch.count(item))

        if all(m):
            M += 1
        # find the total M
    return M / num_experiments
    # return the probabillity 
