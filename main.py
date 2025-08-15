import sys
import os
import datetime
import argparse
from tests.test_parser import TestParser
from tests.test_event_loop import test_event_loop



# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

sys.dont_write_bytecode = True

def event_loop(
    test_mode: bool,
    main_mode: bool,
    args: argparse.Namespace,
) -> None:
    """
    The main event loop of the program.

    :param test_mode: Whether the event loop is in test mode.
    :param main_mode: Whether the event loop is in main mode.
    :param args: The parsed command line arguments.
    :return: None
    """
    try:
        start_time = datetime.datetime.now()
        if test_mode:
            test_event_loop(args, args.limit)
        elif main_mode:
            main(args)
    except Exception as e:
        print(f"Error in Main: {e}")    
    finally:
        end_time = datetime.datetime.now()
        print(f"Total time: {end_time - start_time} at {datetime.datetime.now()}")



if __name__ == "__main__":
    parser = TestParser()
    test_mode, main_mode, args = parser.parse_args()
    event_loop(test_mode, main_mode, args)