#!/usr/bin/python
# coding=utf-8

import util
import constants as C

class maze(graph):
  def __init__(self, pos = None, dir = None):
    if pos:
      self.position = util.coordinate(pos)
    else:
      self.position = C.DEFAULT_POSITION

    if dir:
      self.direction = dir 
    else:
      self.direction = C.DEFAULT_DIRECTION 

    self.touching = None

  def move(squares = 1):
    self.position += C.DIRECTION_POSITION_MAP(self.direction) * squares
    

  def __repr__(self):
    return "Pos: " + str(self.position) + " Dir:" + str(self.direction)
