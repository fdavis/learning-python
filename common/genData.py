#!/usr/bin/python

"""Random Integer Generator CLI Tool.
"""

# need simple random generator
def gen_random(min,max,nums):
    from binascii import hexlify
    from os import urandom

    if min > max:
        (min, max) = (max, min)
    spread = max - min + 1

    for x in range(1,nums):
        yield long(hexlify(urandom(16)),16) % spread + min


# need shuffled integers generator

def main():

    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-M", "--max", dest="max", default=1000, type="int",
                      help="max random number value", metavar="M")
    parser.add_option("-m", "--min", dest="min", default=1, type="int",
                      help="min random number value", metavar="m")
    parser.add_option("-n", "--numbers", dest="nums", default=50, type="int",
                      help="generate n random numbers", metavar="n")
    parser.add_option("-u", "--unique", dest="unique", action="store_true",
                      help="do not allow repeated numbers", metavar="u")
    parser.add_option('-v', action="count", dest='verbosity',
                      help="verbosity levels 0:normal, 1:details, 2:debug")
    (options, args) = parser.parse_args()

    # We usr write_details and write_debug for verbosity
    def print_msgs(*msgs):
        for msg in msgs:
            print msg
        #print

    if options.verbosity > 0:
        def write_details(*msgs):
            print_msgs(*msgs)
    else:
        def write_details(*msgs): None

    if options.verbosity > 1:
        def write_debug(*msgs):
            print_msgs(*msgs)
    else:
        def write_debug(*msgs): None

    write_details("Called with")
    write_details(options)

    for x in range(1,options.nums):
        print gen_random(options.min,options.max,options.nums).next()


if __name__ == '__main__':
    main()
