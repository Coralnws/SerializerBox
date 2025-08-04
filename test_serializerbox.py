# test_serializerbox.py
"""
Tests for SerializerBox module.
"""

import unittest
from serializerbox import SerializerBox

class TestSerializerBox(unittest.TestCase):
    """Test cases for SerializerBox class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SerializerBox()
        self.assertIsInstance(instance, SerializerBox)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SerializerBox()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
