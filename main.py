import sys 
from struct import *
from utils import bkdr, check_endian

class InvalidFile(Exception):
    """Failed our sanity checks"""
    def __init__(self):            
        super().__init__("This file has been detected to not be valid")


def extract(file):
    with open(file, "rb+") as f:
        header = f.read(16)
        if len(header) != 16: raise InvalidFile
        
        header_details = check_endian(header[0:4])
        print(header_details)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("py main.py [file] [x/d]")
    file = sys.argv[1]
    method = sys.argv[2]
    if method == 'x': extract(file)
    
    
    
    