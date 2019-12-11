
import sys
import re

ic = int(sys.argv[1])

with open(sys.argv[2]) as asidstory:
    i = 0
    for line in asidstory:
        # ignore 1st line
        if i>0: 
            bar = re.search("^\s*$", line)
            if bar:
                break
            foo = line.split()
            start_ic = int(foo[4])
            end_ic = int(foo[6])
            if start_ic <= ic and ic <= end_ic:
                print line,
        i += 1
