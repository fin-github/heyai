# Backend for heyai
import os
from sys import argv
from icecream import ic

def main(args: list):
    print("HeyAI by Fin")
    
    
if __name__ == "__main__":
    if argv[1] == "!echoback":
        ic(argv)
        quit("echoback complete")
    
    main(argv[1:])