#!/bin/bash
echo input ip
read varname
echo scanning...

nmap -sP -PE $varname --send-ip --reason -n -v
