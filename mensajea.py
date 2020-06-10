import commands
import sys

commands.getoutput('echo xxx >> f')

print 'dentro'
if sys.argv[1] == 'final':
    print 'final'
    commands.getoutput('echo xxx >> final')
else:
    print 'argumento mierdoso'

