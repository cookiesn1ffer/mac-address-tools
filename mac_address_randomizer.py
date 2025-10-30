#! /usr/bin/env python

import subprocess



interface = input("interface > ") #stores interface value


subprocess.call("sudo ifconfig " + interface + " down ", shell=True)
subprocess.call("sudo macchanger -r " + interface, shell=True)
subprocess.call("sudo ifconfig " + interface + " up", shell=True)

print(subprocess.call("ifconfig " + interface, shell=True)) #final output