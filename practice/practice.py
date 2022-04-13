from contextlib import redirect_stdout
from io import StringIO
import unittest
import unittest.mock


def test():
    import test


class MockTest(unittest.TestCase):
    @unittest.mock.patch('builtins.input', lambda: 'a')
    def test_hoge(self):
        # m1 = unittest.mock.MagicMock()
        # m2 = unittest.mock.MagicMock()
        # m3 = unittest.mock.MagicMock()

        # m1.return_value = 5
        # m2.return_value = (0, 2)
        # m1.return_value = [0, 1 , 2, 3, 0]
        
        # input = m1
        # map = m2
        # list = m3
        # unittest.mock.patch('builtins.input', 'a')

        io = StringIO()
        with redirect_stdout(io):
            test()

        self.assertEqual(io.getvalue(), 'a\n')
# def print_hoge():
#     print('hoge')


# class HogeTest(unittest.TestCase):
#     @unittest.mock.patch('__main__.print')
#     def test_print(self, m):
#         print_hoge()

#         m.assert_called_with('hoge')


if __name__ == '__main__':
    unittest.main()