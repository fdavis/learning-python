#!/usr/bin/python

import util
from util import constants as C

class car:
  def __init__(pos = None, dir = None):
    if pos:
      self.position = pos
    else:
      self.position = C.DEFAULT_POSITION

    if dir:
      self.dir = dir 
    else:
      self.dir = C.DEFAULT_DIRECTION 

    self.touching = None


  def 

