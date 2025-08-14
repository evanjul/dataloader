import sys
import os
import datetime
import argparse

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

# Now import the test modules
from src.huggingface_dataloader.tests.test_parser import TestParser
from src.huggingface_dataloader.tests.test_main import test_main

sys.dont_write_bytecode = True

def run(test_mode: bool, main_mode: bool, args: argparse.Namespace):
    try:
        start_time = datetime.datetime.now()
        if test_mode:
            test_main(args)
        elif main_mode:
            main(args)
    except Exception as e:
        print(f"Error: {e}")    
    finally:
        end_time = datetime.datetime.now()
        print(f"Total time: {end_time - start_time} at {datetime.datetime.now()}")

def main(args):
    print(f"Running in main mode with args: {args}")

if __name__ == "__main__":
    parser = TestParser()
    test_mode, main_mode, args = parser.parse_args()
    run(test_mode, main_mode, args)