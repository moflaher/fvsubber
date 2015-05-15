import sys
import subprocess
import re
import time
import os



arguments = sys.argv


timenum = int(arguments[1])
drag = int(arguments[2])

filepath="/home/moflaher/scratch/minaspassage/smallcape_force/"
start_dates=['2013-08-17', '2011-10-30','2011-08-12', '2010-07-11', '2009-01-28', '2008-08-17','2008-04-29', '2012-08-25','2012-06-03']
end_dates  =['2013-10-24', '2011-12-11','2011-11-03', '2010-08-22', '2009-03-02', '2008-09-24','2008-07-10', '2012-10-23','2012-08-29']
start_dates=['2011-10-30','2011-08-12']
end_dates  =['2011-12-11','2011-11-03']

drag_list=['0.0025']

os.chdir(filepath+drag_list[drag]+("%s"%start_dates[timenum])+"_"+ ("%s"%end_dates[timenum]))

commandQsub = subprocess.check_output(['qsub', 'RUN_PAR2.sh'])
#print commandQsub



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
