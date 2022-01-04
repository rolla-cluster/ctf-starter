#!/bin/bash

# ask for box name
printf "Enter name of box of challenge \n"
read boxname
# ask for IP
printf "Enter IP \n"
read rIP

printf "\n------------------------- Preparing Env ----------------------------\n\n"
mkdir ~/HTB/$boxname
cd ~/HTB/$boxname
touch scratch.md #for notes/analysis
printf "=== Made a new directory: $boxname \n"

printf "=== Checking for HTTP server and running wordlist gatherer\n"
python3 ~/ctf-starter/main.py $rIP


printf "Running a full NMAP scan, default scripts, saving output \n"
nmap -sV -sC -v $rIP -oN nmapscan.txt

printf "DONE scanned: $rIP for the box: $boxname"
printf "\n----------------------------------------------------------------------------\n"

printf "\nYour tun0 IP is:\n"
ip addr show tun0 | grep global
