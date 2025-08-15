import struct

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