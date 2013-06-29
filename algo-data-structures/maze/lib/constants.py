#!/usr/bin/python
# coding=utf-8

from util import coordinate

BLOCK = '█'
SPACE = '+'
CAR = '@'

CHAR_MAP = {0: SPACE, 1: BLOCK, 2: CAR}

DEFAULT_DIRECTION = 2
DIRECTION_MAP = {0: 'North',
                 1: 'Northeast',
                 2: 'East',
                 3: 'Southeast',
                 4: 'South',
                 5: 'Southwest',
                 6: 'West',
                 7: 'Northwest'
                 }

DEFAULT_POSITION = coordinate(0, 0)

# this is used to increment position based on the direction
DIRECTION_TO_POSITION_MAP = {0: coordinate(0,1),
                             1: coordinate(1,1),
                             2: coordinate(1,0),
                             3: coordinate(1,-1),
                             4: coordinate(0,-1),
                             5: coordinate(-1,-1),
                             6: coordinate(-1,0),
                             7: coordinate(-1,1)
                             }
