#$ -S /bin/bash
#$ -cwd
#$ -N alljobs
#$ -R y
#$ -j y
#$ -l h_rt=330:00:00
time python master.py > fvsubber_output
echo "Application ends at `date`"
