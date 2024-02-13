#!/usr/bin/python3
"""
Unittest for models/square

unittest classes:
    TestSquare_instantiation
    TestSquare_size
    TestSquare_x
    TestSquare_y
    TestSquare_to_dictionary
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(13), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(1), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(42)
        s2 = Square(13)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(1, 6)
        s2 = Square(4, 1)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 5, 7)
        s2 = Square(21, 5, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 11, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(16).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(16).y)


class TestSquare_size(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("inv")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(7.5)

    def test_complexsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"b": 1, "c": 3}, 2)

    def test_boolsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 4, 6)

    def test_listsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([6, 2, 5])

    def test_setsize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({10, 4, 23}, 21)

    def test_tuplesize(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((10, 5, 3), 8, 9)

    def test_negativesize(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zerosize(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    def test_Nonex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_strx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 6.5)

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Py')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, float('5.8'), 4)

    def test_nanx(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, float('nan'), 3)

    def test_negativex(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -10, 6)


class TestSquare_area(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    def test_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_changed_attributes(self):
        s = Square(2, 0, 0, 1)
        s.size = 7
        self.assertEqual(49, s.area())

    def test_area_one_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquare_stdout(unittest.TestCase):
    """
    Unittests for testing __str__ and display methods of Square class.
    """

    @staticmethod
    def capture_stdout(sq, method):
        """
        Captures and returns text printed to stdout.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_printsize(self):
        s = Square(5)
        capture = TestSquare_stdout.capture_stdout(s, "print")
        correct = "[Square] ({}) 0/0 - 5\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_methodsizex(self):
        s = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_str_methodsize_x_y(self):
        s = Square(10, 8, 22)
        correct = "[Square] ({}) 8/22 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y_id(self):
        s = Square(10, 88, 14, 9)
        self.assertEqual("[Square] (9) 88/14 - 10", str(s))

    def test_str_methodchanged_attr(self):
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_onearg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    def test_disp_size(self):
        s = Square(2, 0, 0, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_disp_sizex(self):
        s = Square(3, 1, 0, 18)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_disp_sizey(self):
        s = Square(4, 0, 1, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_dispsizex_y(self):
        s = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_disp_one_arg(self):
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""

    def test_updateargszero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args(self):
        s = Square(20, 20, 20, 20)
        s.update(89)
        self.assertEqual("[Square] (89) 20/20 - 20", str(s))

    def test_update_more_args(self):
        s = Square(50, 50, 50, 50)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_w_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.width)

    def test_update_args_h_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.height)

    def test_update_args_Noneid(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_Noneid_more(self):
        s = Square(10, 10, 10, 10)
        s.update(None, 2, 8)
        correct = "[Square] ({}) 8/10 - 2".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_getx_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 2, "invalid")

    def test_update_args_gety_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(98, 1, 2, -4)


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class."""
    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))

    def test_update_kwarg_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(s))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dict_output(self):
        s = Square(15, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 15, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 1)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
