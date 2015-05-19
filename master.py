from defaultdic import make_rundict
from makeRun import copy_create

#from myQSUB import pyqsub
from itertools import product
import sys
import collections

dates=collections.OrderedDict()
arguments = sys.argv
copypath  = arguments[1]
outpath   = arguments[2]


runvalues=make_rundict('acadia_force_2d')
dates['2011-10-30']='2011-12-11'
dates['2011-08-12']='2011-11-03'

runvalues['BOTTOM_ROUGHNESS_MINIMUM']=[.002,.00225,.0025]


masterlist = [ v for v in runvalues.values()]
for date in dates:  
    for i,looplist in enumerate(product(*masterlist)):         
        foldername=copy_create(runvalues,looplist,dates,date,copypath,outpath)
        pyqsub(outpath,foldername)


        

