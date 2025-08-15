

from .test_generator import TestDataGenerator
from .test_model import TestDataModel
import sys

sys.dont_write_bytecode = True

def test_event_loop(args, limit):
    print(f"Running in test mode with args: {args}")
    for idx, url in enumerate(args.urls):
        if isinstance(url,list):
            print(idx, url, type(url), limit)
            data = TestDataGenerator(url, limit)
            

        
        
        

    
