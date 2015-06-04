import sys
import subprocess
import re
import time
import os



def pyqsub(outpath,foldername,wait):

    #add slash to path if they were not included
    if outpath[-1]!='/':
        outpath+='/'

    os.chdir(outpath+foldername)
    commandQsub = subprocess.check_output(['qsub', 'RUN_PAR_2D.sh'])

    if wait:
    	pattern = r'\b\d{1,9}\b'
    	match = re.search(pattern,commandQsub)

    	jobID = match.group(0)
    	#print jobID

    	match=True
    	pattern = r'\b{}\b'.format(jobID)

        while match:
            commandQstat = subprocess.check_output(["qstat"])
            match = re.search(pattern,commandQstat)
            #print 'Still running'
            time.sleep(120)
