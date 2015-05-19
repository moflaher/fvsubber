from defaultdic import make_rundict
from makeRun import copy_create
from myQSUB import pyqsub
from itertools import product
import sys
import collections

dates=collections.OrderedDict()
arguments = sys.argv
copypath = arguments[1]


runvalues=make_rundict('acadia_force_2d')
dates['2011-10-30']='2011-12-11'
dates['2011-08-12']='2011-11-03'

#also changes any default runvalues here!!!!


masterlist = [ v for v in runvalues.values()]
for i,looplist in enumerate(product(*masterlist)):
    copy_create(looplist,othervalues,dates[i,0],dates[i,1])
    pyqsub(looplist,othervalues,dates[i,0],dates[i,1])


        

