#!/usr/bin/env python3

import os
import sys

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if disk_full():
	print("Disk Full."
	sys.exit(1)
    print("EVerything Ok")
    sys.exit(0)
main()
