#!/bin/bash
echo input ip

read varname

echo scanning...

fping -r 0 -g $varname
