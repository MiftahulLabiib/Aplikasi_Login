#!/usr/bin/env python3

import os
import sys
import shutil
def check_disk_full(disk, min_gb, min_percent):
    """Returns True if the disk partition is full, False otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gb_free = du.free / 2**30
    if percent_free < min_percent or gb_free < min_gb:
        return True
    return False

def check_reboot():
    """Returns True if the computer has a pending reboot, False otherwise"""
    return os.path.exists("/run/reboot-required")

def check_root_full():
    """Returns True if the root partition is full, False otherwise"""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def main():
    checks = [(check_reboot, "Pending Reboot"), (check_root_full, "Root partition full")]
    for check, msg in checks:
        if check():
            print(msg)
            sys.exit(1)
    
    print("Everything Ok")
    sys.exit(0)

if __name__ == "__main__":
    main()

