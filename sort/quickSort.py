#!/usr/bin/python

"""Quick Sort CLI tool
"""

def swap(a, b):
    return (b, a)

def set_pivot(list):
    (a, b, c) = (list[0], list[len(list)/2], list[-1])
    if a > b: (a, b) = swap(a, b)
    if b > c: (b, c) = swap(b, c)
    if a > b: (a, b) = swap(a, b)
    return (a, b, c)

def main():
    # gen random set
        # write to random input file
    # read from input set
    # sort
    # write to output file

if __name__ == '__main__':
    main()
