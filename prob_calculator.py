import copy
import random
class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color, number in kwargs.items():
      for i in range(number):
        self.contents.append(color)

  def draw(self, num_balls_drawn):
    '''
    This method should remove balls at random from contents and
    return those balls as a list of strings. The balls should not go back 
    into the hat during the draw, similar to an urn experiment without 
    replacement. If the number of balls to draw exceeds the available 
    quantity, return all the balls.
    '''
    if num_balls_drawn > len(self.contents):
      return self.contents
    else:
      balls_drawn = [] 
      for i in range(num_balls_drawn):
        # randomly get the number for the index of the ball
        ball_drawn = random.randint(0, len(self.contents)-1)
        # add the ball to the balls_drawn list
        balls_drawn.append(self.contents[ball_drawn])
        # remove the ball from self.contents
        self.contents.pop(ball_drawn)
      return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  '''
  For example, if you want to determine the probability of getting at 
  least two red balls and one green ball when you draw five balls from a 
  hat containing six black, four red, and three green. To do this, you 
  will perform N experiments, count how many times M you get at least two red balls and   one green ball, and estimate the probability as M/N.
   Each experiment consists of starting with a hat containing the 
  specified balls, drawing several balls, and checking if you got the 
  balls you were attempting to draw.
  '''
  matches = 0
  # make a deep copy of contents so we can reset it for the next draw
  original_contents = copy.deepcopy(hat.contents)

  # draw balls for as many times as num_experiments
  for i in range(num_experiments):
    balls_drawn = hat.draw(num_balls_drawn)
    # reset contents back to its original values
    hat.contents = copy.deepcopy(original_contents)
    
    # convert balls_drawn to a dictionary
    balls_drawn_dict = {}
    for item in balls_drawn:
      if item in balls_drawn_dict.keys():
        balls_drawn_dict[item] += 1
      else:
        balls_drawn_dict[item] = 1

    # check to see if we drew the expected_balls
    matched = True
    for color, number in expected_balls.items():
      if color in balls_drawn_dict.keys() and balls_drawn_dict[color] >= expected_balls[color]:
        pass
      else:
        matched = False
        break
    if matched:
      matches += 1

  return matches / num_experiments
