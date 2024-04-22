import unittest
import tree

class Testing(unittest.TestCase):
    def setUp(self) -> None:
        nodes = [5, 4, 3, 2, 1, 6, 7, 8, 9]
        self.root = tree.Tree()
        [self.root.add(x) for x in nodes]

    def test_tree_find(self):
        res = self.root.find(8)
        self.assertIsNotNone(res)

    def test_tree_not_find(self):
        res = self.root.find(20)
        self.assertIsNone(res)

if __name__ == '__main__':
    unittest.main()