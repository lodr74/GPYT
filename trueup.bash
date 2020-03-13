#!/bin/bash
/usr/bin/python3 new_acct.py
i="0" 
while [ $i -lt 88 ] 
do
echo "Starting exercise $i"
/usr/bin/python3 pyWars$i.py
/usr/bin/python pyWars$i.py
i=$[$i+1]
done

