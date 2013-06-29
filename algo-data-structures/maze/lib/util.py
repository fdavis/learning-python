#!/usr/bin/python
# coding=utf-8

# taken from http://stackoverflow.com/questions/1169725/adding-values-from-tuples-of-same-length
class coordinate(tuple):

    def __new__(cls, *args):
        return tuple.__new__(cls, args)

    def __add__(self, other):
        return T(*([sum(x) for x in zip(self, other)]))

    def __sub__(self, other):
        return self.__add__(-i for i in other)

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

    # this is used to increment position based on the direction
    self.DIRECTION_TO_POSITION_MAP = {0: coordinate(0,1),
                                      1: coordinate(1,1),
                                      2: coordinate(1,0),
                                      3: coordinate(1,-1),
                                      4: coordinate(0,-1),
                                      5: coordinate(-1,-1),
                                      6: coordinate(-1,0),
                                      7: coordinate(-1,1)
                                      }


