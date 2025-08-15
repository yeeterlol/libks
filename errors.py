class InvalidFile(Exception):
    """Failed our sanity checks"""
    def __init__(self):            
        super().__init__("This file has been detected to not be valid")
        
class BrokenFileIndexException(Exception):
    """Failed our sanity checks"""
    def __init__(self):            
        super().__init__("This file has a broken index")