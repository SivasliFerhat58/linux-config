import numpy as np
import unittest
import user as task_1

class TestModifyArray(unittest.TestCase):
    def test_modify_array(self):
        arr = np.array([1, 2, 3, 4, 5])
        expected_result = np.array([3, 6, 11, 18, 27])
        np.testing.assert_array_equal(task_1.modify_array(arr), expected_result)

if __name__ == '__main__':
    unittest.main()
