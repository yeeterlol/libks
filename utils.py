import struct
from errors import BrokenFileIndexException
import codecs
import os
from pathlib import Path

END_BYTE = b'\0'

def bkdr(name):
    res = 0
    for ch in name:
        c = ord(ch)
        # force uppercase any characters
        if 'a' <= ch <= 'z':
            c -= 0x20 
        res = (res * 31 + c) & 0xffffffff
    return res 

def check_endian(header):
    # shit fucking hack but it works
    # bpms are usually way fucking smaller than typical to be honest
    data = {"big": ">I", "little": "<I"}
    a = struct.unpack(data["big"], header)
    b = struct.unpack(data["little"], header)
    if (a < b): return "big"
    if (b < a): return "little"
    
def get_name(fn, name, stop):
    filename = ""
    with open(fn, "rb+") as f:
        f.seek(stop + name)
        entry = f.read(1)
        if len(entry) != 1: raise BrokenFileIndexException
        filename += codecs.decode(entry, errors='ignore')
        while (byte := f.read(1)):
            if byte == b'\0': break
            filename += codecs.decode(byte, errors='ignore')
    return filename
        
def dump_files(file, file_index):
    for item in file_index:
        istart = file_index[item]['indexStart']
        size = file_index[item]['size']
    
        shit = Path(item)
        shit.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file, 'rb') as infile, open(item, 'wb') as outfile:
            infile.seek(istart)
            reader = infile.read( (istart + size) - istart )
            outfile.write(reader)