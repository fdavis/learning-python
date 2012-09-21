#!/usr/bin/python

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
print options, args

def test_func(a,
	      snarp,
	      jarp,
	      snack):
	print "test func"

def other_fc(
	berker,
	snarp):
	print "other func"


#test_func(1,1,1,1)
#other_fc(1,1)
	

