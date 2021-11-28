import unittest
import random
import dtw



class DTW_Tester(unittest.TestCase):

    def test_base(self):
        s1 = [1, 2, 3, 4, 5, 5, 5, 4]
        s2 = [3, 4, 5, 5, 5, 4]
        result = ([[0, 0], [1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5]], 3)
        self.assertEqual(dtw.dynamic_time_warping(s1, s2), result)

    def test_equal(self):
        s1 = [1, 2, 3, 4, 5, 5, 5, 4]
        result = ([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]], 0)
        self.assertEqual(dtw.dynamic_time_warping(s1, s1), result)
        s2 = [3, 4, 5, 5, 5, 4]
        result = ([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 0)
        self.assertEqual(dtw.dynamic_time_warping(s2, s2), result)
    
    def test_one_num(self):
        s1 = [1]
        s2 = [1]
        result = ([[0, 0]], 0)
        self.assertEqual(dtw.dynamic_time_warping(s1, s2), result)
        s1 = [1000]
        s2 = [1]
        result = ([[0, 0]], 999)
        self.assertEqual(dtw.dynamic_time_warping(s1, s2), result)
    
    def test_empty(self):
        s1 = []
        s2 = [1]
        with self.assertRaises(dtw.DTW_Exception):
            dtw.dynamic_time_warping(s1, s2)
        s1 = [1]
        s2 = []
        with self.assertRaises(dtw.DTW_Exception):
            dtw.dynamic_time_warping(s1, s2)
        s1 = []
        s2 = []
        with self.assertRaises(dtw.DTW_Exception):
            dtw.dynamic_time_warping(s1, s2)
    
    def test_random(self):
        for _ in range(100):
            size = random.randrange(3, 100)
            s1 = []
            start = random.randrange(-100, 100)
            step = random.randrange(1, 10)
            finish = start + step * size
            for i in range(start, finish, step):
                s1.append(i)
            s2 = s1.copy()
            deleted_index = random.randrange(1, size - 1)
            s2.pop(deleted_index)
            result = [[x, x if x < deleted_index and deleted_index != len(s1) - 1  else x - 1] for x in range(size)]
            self.assertEqual(dtw.dynamic_time_warping(s1, s2)[0], result)
    def test_bad(self):
        s1 = [1, 2, 3, 4, 5, 5, 5, 4]
        result = ([[7, 7]], 0)
        self.assertEqual(dtw.dynamic_time_warping(s1, s1), result)





if __name__ == "__main__":
    unittest.main()



