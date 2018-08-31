#!/bin/bash
INPUTIP=$1

if [ -z $INPUTIP ] 
then 
echo " you must have a parameter"

else 
echo "alive host" 
 fping -g $INPUTIP/24 -A -a -q 
fi
