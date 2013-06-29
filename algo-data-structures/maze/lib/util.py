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

