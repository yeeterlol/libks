import sys 
from struct import *
from utils import bkdr, check_endian, get_name, dump_files
from errors import InvalidFile

LINE_SIZE = 16
PADDING_BYTE = 4294967295


def extract(file):
    with open(file, "rb+") as f:
        header = f.read(LINE_SIZE)
        if len(header) != LINE_SIZE: raise InvalidFile
        
        header_details = check_endian(header[0:4])
        
        infostruct = ">IIII"
        if header_details == "little": infostruct = "<IIII"
        
        fcount, finfo, fbuf, start = unpack(infostruct, header)
        stop = (finfo + 1) * LINE_SIZE
        
        file_index = {}
        while (byte := f.read(LINE_SIZE)):
            if f.tell() > stop: break
            named, data, size, next_index = unpack(infostruct, byte)
            if named == PADDING_BYTE: continue 
            
            name = get_name(file, named, stop)
            file_index[name] = {"indexStart": (start+data), "size": size}
        print(file_index)
        dump_files(file, file_index)
            
            
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("ksedit 0.0.1")
        print("py main.py [file] [x/d/c]")
        sys.exit()
    
    file = sys.argv[1]
    method = sys.argv[2]
    if method == 'x': extract(file)
    else: print("wip")
    
    
    
    