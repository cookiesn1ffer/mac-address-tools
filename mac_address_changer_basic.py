#! /usr/bin/env python

#FUNCTIONS
import subprocess

interface = input("interface > ") #stores interface value
print(subprocess.call(["ifconfig", interface])) #prints interface current status
new_mac = input("new MAC > ") #stores new_mac value

print("[+] Changing mac address for " + interface + " to " + new_mac)

subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])

print(subprocess.call(["ifconfig", interface])) #final output
