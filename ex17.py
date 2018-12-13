from sys import argv
from os.path import exists
# list of parameter need to mention
script, from_file,to_file = argv
# 
print " Copy from %s to %s "%(from_file,to_file)

in_file = open(from_file)
indata=in_file.read()
print "The output file is %d bytes long" %len(indata)
print "Does output file exists %r" %exists(to_file)
print "Ready , hot return to continue for exit CTRL+C to abort"

raw_input()

out_file = open(to_file,'w')
out_file.write(indata)
print "alright, all done"
out_file.close()
in_file.close()