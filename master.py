from defaultdic import make_rundict
from makeRun import copy_create
from myQSUB import pyqsub
from itertools import product
import sys
import collections

dates=collections.OrderedDict()
arguments = sys.argv
copypath  = arguments[1]
outpath   = arguments[2]

#Pass the grid name to make_rundict
runvalues=make_rundict('acadia_force_2d')

#Add dates as dates['startdate']='enddate'
#Runs will start 3 days earlier to account for spinup
dates['2011-10-30']='2011-12-11'
dates['2011-08-12']='2011-11-03'

#Change anything in defaultdic.py
#For running a range of values assign the key a list to iterate over.
#Warning: As many options as needed can be changed.
#         This can result in alot of runs very quickly.
runvalues['BOTTOM_ROUGHNESS_MINIMUM']=[.00225,.0025,.00275]


masterlist = [ v for v in runvalues.values()]
for date in dates:  
    for i,looplist in enumerate(product(*masterlist)):         
        foldername=copy_create(runvalues,looplist,dates,date,copypath,outpath)
        if foldername!=False:
            pyqsub(outpath,foldername)


        

