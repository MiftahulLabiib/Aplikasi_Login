#!/usr/bin/env python3

import os
import sys

(...)
def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if check_disk_full(disk = "/", min_gb = 2, min_percent = 10):
	print("Disk Full."
	sys.exit(1)
    print("EVerything Ok")
    sys.exit(0)
(...)
