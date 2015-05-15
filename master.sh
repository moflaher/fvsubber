#!/bin/bash
gridName="smallcape_force"

export gridName

for drag in {0..1}
    for time in {0..8}
    do
        python /home/moflaher/scratch/minaspassage/smallcape_force/massruns/makeRun.py $gridName $time $drag
        python /home/moflaher/scratch/minaspassage/smallcape_force/massruns/myQSUB.py $time $drag
    done
done
