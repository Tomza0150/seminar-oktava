#!/usr/bin/env python3
"""
Tento program zatim nic nedela
"""
import argparse
import sys

def cmdline_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    p.add_argument("required_positional_argument", help="desc")
    p.add_argument("--on", action="store_true", help="include to enable")
    p.add_argument("-v", "--verbosity", type=int, choices=[0,1,2], default=0, help="volba vymluvnosti")
    p.add_argument("-n", "--number", type=int, help="Zadej čislo")

    return p.parse_args()

if __name__=="__main__":
    
    try:
        args = cmdline_args()
        import random
        print(f"Hod:{random.randint(1,args.steny)}")
    except:
        print("Try ./main.py --help")
    