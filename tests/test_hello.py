import unittest
import sys
import io
from python_bp_2025 import main

class TestHello(unittest.TestCase):
    def setUp(self):
        # Capture stdout to test print statements
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        # Restore stdout
        sys.stdout = sys.__stdout__

    def test_main_output(self):
        # Run the main function
        main()
        
        # Get the output
        output = self.captured_output.getvalue()
        
        # Check if the output contains the expected message
        self.assertIn("Hello, World!", output)

if __name__ == '__main__':
    unittest.main() 