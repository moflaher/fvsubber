from defaultdic import make_rundict
from makeRun import copy_create
from myQSUB import pyqsub
from itertools import product

runvalues,othervalues=make_rundict('smallcape_force')

dates=['somedate stuff here, figureout structure']
#also changes any default runvalues here!!!!


masterlist = [ v for v in runvalues.values()]
for i,looplist in enumerate(product(*masterlist)):
    copy_create(looplist,othervalues,dates[i,0],dates[i,1])
    pyqsub(looplist,othervalues,dates[i,0],dates[i,1])


        

