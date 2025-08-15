import unittest
from unittest.mock import patch, MagicMock
from argparse import Namespace
import datetime
from main import event_loop

class TestMain(unittest.TestCase):
    @patch('main.test_event_loop')
    @patch('main.main')
    def test_event_loop_test_mode(self, mock_main, mock_test_event_loop):
        """
        Test that event_loop calls test_event_loop in test mode
        """
        args = Namespace(limit=10)
        event_loop(test_mode=True, main_mode=False, args=args)
        
        mock_test_event_loop.assert_called_once_with(args, args.limit)
        mock_main.assert_not_called()

    @patch('main.test_event_loop')
    @patch('main.main')
    def test_event_loop_main_mode(self, mock_main, mock_test_event_loop):
        """
        Test that event_loop calls main in main mode
        """
        args = Namespace()
        event_loop(test_mode=False, main_mode=True, args=args)
        
        mock_main.assert_called_once_with(args)
        mock_test_event_loop.assert_not_called()

    @patch('main.test_event_loop')
    @patch('main.main')
    def test_event_loop_exception_handling(self, mock_main, mock_test_event_loop):
        """
        Test that event_loop handles exceptions properly
        """
        args = Namespace()
        mock_main.side_effect = Exception("Test error")
        
        with patch('builtins.print') as mock_print:
            event_loop(test_mode=False, main_mode=True, args=args)
            mock_print.assert_called_once_with("Error in Main: Test error")

    @patch('main.test_event_loop')
    @patch('main.main')
    def test_event_loop_timing(self, mock_main, mock_test_event_loop):
        """
        Test that event_loop measures and prints execution time
        """
        args = Namespace()
        mock_main.return_value = None
        
        with patch('builtins.print') as mock_print:
            event_loop(test_mode=False, main_mode=True, args=args)
            
            # Verify timing output was printed
            calls = mock_print.call_args_list
            self.assertEqual(len(calls), 2)  # Error message and timing
            timing_call = calls[1]
            self.assertTrue(timing_call[0][0].startswith("Total time:"))

if __name__ == '__main__':
    unittest.main()
