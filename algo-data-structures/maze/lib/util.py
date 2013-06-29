#!/usr/bin/python

class constants:

  def __init__():
    self.BLOCK = '█'
    self.SPACE = '+'
    self.CAR = '@'

    self.CHAR_MAP = {0: SPACE, 1: BLOCK, 2: CAR}

    self.DEFAULT_DIRECTION = 2
    self.DIRECTION_MAP = {0: 'North',
                          1: 'Northeast',
                          2: 'East',
                          3: 'Southeast',
                          4: 'South',
                          5: 'Southwest',
                          6: 'West',
                          7: 'Northwest'
                          }

    self.DEFAULT_POSITION = (0, 0)

