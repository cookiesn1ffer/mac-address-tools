#! /usr/bin/env python

#FUNCTIONS
import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

(options, arguments) =parser.parse_args()

interface = options.interface #stores interface value
new_mac = options.new_mac #stores new_mac value

print("[+] Changing mac address for " + interface + " to " + new_mac)

subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])

print(subprocess.call(["ifconfig", interface])) #final output
