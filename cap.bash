#!/bin/bash
/usr/bin/python3 new_acct.py
i="0" 
while [ $i -lt 21 ] 
do
echo "Starting exercise $i"
/usr/bin/python captstone$i.py
#/usr/bin/python pyWars$i.py
i=$[$i+1]
done

