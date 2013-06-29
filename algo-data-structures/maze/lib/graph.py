#!/usr/bin/python
# coding=utf-8

import car
import sys
import util

class graph:

  # attempt to load plaintext map file
  # format should be only block/space/car characters and newlines
  def __init__(filename):
    self.map = []
    try:
      f = open(filename)
      for line in f.readlines():
        row = []
        for x in line.strip():
          if util.isValidChar(x):
            row.append(x)
          else:
            sys.stderr.write('Ignoring bad character: %s' % x)
        self.map.append(row)
      f.close()

    except IOError as e:
      sys.stderr.write('Failed to load map file.\n')
      raise e
      


  def __unicode__():
    for row in self.map:
      for col in row:
        sys.stdout.write(col)
      sys.stdout.write('\n')
