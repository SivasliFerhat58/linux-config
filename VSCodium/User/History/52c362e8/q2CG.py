import numpy as np

def modify_array(arr):
    return (arr ** 2) + 2

import unittest

class TestModifyArray(unittest.TestCase):

    def test_modify_array(self):
        arr = np.array([1, 2, 3, 4, 5])
        expected_result = np.array([3, 6, 11, 18, 27])
        np.testing.assert_array_equal(modify_array(arr), expected_result)

if __name__ == '__main__':
    unittest.main()
