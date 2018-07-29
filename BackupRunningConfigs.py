#!/usr/bin/env python
#Backs up switch running configurations to separate local files
#Prequisite: List the IP addresses of all your switches in Switches.py, one IP address per line
#Store Switches.py in the same directory as this script
#Based on script in David Bombai Udemy.com course Python Programming for Cisco Network Engineers

import getpass
import sys
import telnetlib

#Ask for credentials
user = raw_input("Enter username: ")
password = getpass.getpass()

#Open the file Switches.py
file = open ("Switches.py")

#Telnet to switches listed in file and get the running configuration
for line in file:
   print "Get running config from switch " + (line)
   telnet = telnetlib.Telnet(HOST)

   telnet.read_until("Username: ")
   telnet.write(user + "\n")
   if password:
       telnet.read_until("Password: ")
       telnet.write(password + "\n")

   #show all output instead of only 1 screen at a time
   telnet.write("terminal length 0\n")
   telnet.write("show run\n")
   telnet.write("exit\n")

   readoutput = telnet.read_all()

   saveoutput = open("switch" + HOST, "w")
   saveoutput.write(readoutput)
   saveoutput.close()



