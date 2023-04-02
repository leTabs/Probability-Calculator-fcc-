import random
import copy

class Hat:
    def __init__(self, **balls):
        self.balls = balls
        self.contents = []
        
        for k, v in self.balls.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, number_draw):
        balls_drawn = []
        
        if number_draw > len(self.contents):
            balls_drawn = self.contents[:]
            return balls_drawn
        
        
        for i in range(number_draw):
            r = random.randint(0,len(self.contents)-1)

            balls_drawn.append(self.contents[r])
            del self.contents[r]
        #print(self.contents)
        return balls_drawn



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    m = []
    expected_balls_list = []
    for k in expected_balls:
        expected_balls_list.append(k)
    #print(expected_balls_list)
    for i in range(num_experiments):
        c_hat = copy.deepcopy(hat)
        ch = c_hat.draw(num_balls_drawn)
        for item in expected_balls_list:
            
            m.append(expected_balls[item] <= ch.count(item))
            #print(expected_balls[item] <= ch.count(item))

        if False in m:
            pass
        else: M+=1
        m = []
    print((M/num_experiments) * 100) 
hat = Hat(black=6, red=4, green=3)

probability = experiment(hat = hat,
                expected_balls={"red":2,"green":1, 'black':2},
                num_balls_drawn=5,
                num_experiments=2000)
