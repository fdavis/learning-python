#!/usr/bin/python

def main():

    from optparse import OptionParser
    import os
    import base64

    parser = OptionParser()
    parser.add_option("-i", "--in-file", dest="in_path", default="", type="string",
                      help="file to copy", metavar="IN_FILE_PATH")
    parser.add_option("-o", "--out-file", dest="out_path", default="", type="string",
                      help="copy destination", metavar="OUT_FILE_PATH")
    parser.add_option("-c", "--chunk-size", dest="chunk_size", default=16, type="int",
                      help="size of chunks", metavar="CHUNK_SIZE")
    parser.add_option("-f", "--force", dest="force", default=False, 
                      help="overwrite destination if it exists", action="store_true")
    (options, args) = parser.parse_args()

    if not os.path.exists(options.in_path):
        raise IOError("in file cannot be found: %s" % options.in_path)

    if not options.force and os.path.exists(options.out_path):
        raise IOError("out file exist: %s (use -f to overwrite)" % options.out_path)

    ifh = open(options.in_path, 'rb')
    ofh = open(options.out_path, 'wb')
    data = base64.b64encode(ifh.read(options.chunk_size))
    c = 0
    while data != "":
        ofh.write(base64.b64decode(data))
        data = base64.b64encode(ifh.read(options.chunk_size))
        c += 1
        print c

    ifh.close()
    ofh.close()
















if __name__ == '__main__':
    main()

