
    def tearDown(self):
        """Remove the file created by the tests."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def attributes(self, square):
        """Return the four attributes of a square in a tuple."""
        return (square.id, square.size, square.x, square.y)

    def test_square_one_argument(self):
        """Check Square(1)."""
        self.assertEqual(self.attributes(Square(1)), (1, 1, 0, 0))

    def test_square_two_arguments(self):
        """Check Square(1, 2)."""
        self.assertEqual(self.attributes(Square(1, 2)), (1, 1, 2, 0))

    def test_square_three_arguments(self):
        """Check Square(1, 2, 3)."""
        self.assertEqual(self.attributes(Square(1, 2, 3)), (1, 1, 2, 3))

    def test_square_four_arguments(self):
        """Check Square(1, 2, 3, 4)."""
        self.assertEqual(self.attributes(Square(1, 2, 3, 4)), (4, 1, 2, 3))

    def test_size_string(self):
        """Check Square("1")."""
        with self.assertRaises(TypeError) as cm:
            Square("1")
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_x_string(self):
        """Check Square(1, "2")."""
        with self.assertRaises(TypeError) as cm:
            Square(1, "2")
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_y_string(self):
        """Check Square(1, 2, "3")."""
        with self.assertRaises(TypeError) as cm:
            Square(1, 2, "3")
        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_size_negative(self):
        """Check Square(-1)."""
        with self.assertRaises(ValueError) as cm:
            Square(-1)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_x_negative(self):
        """Check Square(1, -2)."""
        with self.assertRaises(ValueError) as cm:
            Square(1, -2)
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_y_negative(self):
        """Check Square(1, 2, -3)."""
        with self.assertRaises(ValueError) as cm:
            Square(1, 2, -3)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_size_zero(self):
        """Check Square(0)."""
        with self.assertRaises(ValueError) as cm:
            Square(0)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_str_values(self):
        """Check __str__() with different values."""
        self.assertEqual(str(Square(1)), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(Square(1, 2, 3, 4)), "[Square] (4) 2/3 - 1")

    def test_to_dictionary_values(self):
        """Check to_dictionary() with the four attributes."""
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.to_dictionary(),
                         {"id": 4, "size": 1, "x": 2, "y": 3})
        self.assertEqual(set(square.to_dictionary()),
                         {"id", "size", "x", "y"})

    def test_update_no_arguments(self):
        """Check update() without arguments."""
        square = Square(10, 11, 12, 13)
        square.update()
        self.assertEqual(self.attributes(square), (13, 10, 11, 12))

    def test_update_one_argument(self):
        """Check update(89)."""
        square = Square(10, 11, 12, 13)
        square.update(89)
        self.assertEqual(self.attributes(square), (89, 10, 11, 12))

    def test_update_two_arguments(self):
        """Check update(89, 1)."""
        square = Square(10, 11, 12, 13)
        square.update(89, 1)
        self.assertEqual(self.attributes(square), (89, 1, 11, 12))
        self.assertEqual((square.width, square.height), (1, 1))

    def test_update_three_arguments(self):
        """Check update(89, 1, 2)."""
        square = Square(10, 11, 12, 13)
        square.update(89, 1, 2)
        self.assertEqual(self.attributes(square), (89, 1, 2, 12))

    def test_update_four_arguments(self):
        """Check update(89, 1, 2, 3)."""
        square = Square(10, 11, 12, 13)
        square.update(89, 1, 2, 3)
        self.assertEqual(self.attributes(square), (89, 1, 2, 3))

    def test_update_kwargs_id(self):
        """Check update(**{'id': 89})."""
        square = Square(10, 11, 12, 13)
        square.update(**{'id': 89})
        self.assertEqual(self.attributes(square), (89, 10, 11, 12))

    def test_update_kwargs_id_size(self):
        """Check update(**{'id': 89, 'size': 1})."""
        square = Square(10, 11, 12, 13)
        square.update(**{'id': 89, 'size': 1})
        self.assertEqual(self.attributes(square), (89, 1, 11, 12))
        self.assertEqual((square.width, square.height), (1, 1))

    def test_update_kwargs_id_size_x(self):
        """Check update(**{'id': 89, 'size': 1, 'x': 2})."""
        square = Square(10, 11, 12, 13)
        square.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(self.attributes(square), (89, 1, 2, 12))

    def test_update_kwargs_four_keys(self):
        """Check update with id, size, x and y."""
        square = Square(10, 11, 12, 13)
        square.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(self.attributes(square), (89, 1, 2, 3))

    def test_create_id(self):
        """Check Square.create(**{'id': 89})."""
        square = Square.create(**{'id': 89})
        self.assertIs(type(square), Square)
        self.assertEqual(square.id, 89)

    def test_create_id_size(self):
        """Check Square.create(**{'id': 89, 'size': 1})."""
        square = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual((square.id, square.size), (89, 1))

    def test_create_id_size_x(self):
        """Check Square.create(**{'id': 89, 'size': 1, 'x': 2})."""
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(self.attributes(square), (89, 1, 2, 0))

    def test_create_four_keys(self):
        """Check Square.create with id, size, x and y."""
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(self.attributes(square), (89, 1, 2, 3))

    def test_save_to_file_none(self):
        """Check Square.save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Check Square.save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_save_to_file_one_square(self):
        """Check Square.save_to_file([Square(1)])."""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as a_file:
            content = a_file.read()
        self.assertEqual(json.loads(content), [
            {"id": 1, "size": 1, "x": 0, "y": 0}])
        self.assertEqual(len(content), len(json.dumps(json.loads(content))))

    def test_load_from_file_does_not_exist(self):
        """Check Square.load_from_file() when the file does not exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Check Square.load_from_file() when the file exists."""
        Square.save_to_file([Square(1, 2, 3, 4), Square(6)])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertIs(type(loaded[0]), Square)
        self.assertEqual(self.attributes(loaded[0]), (4, 1, 2, 3))
        self.assertEqual(loaded[1].to_dictionary(),
                         {"id": 1, "size": 6, "x": 0, "y": 0})


if __name__ == "__main__":
    unittest.main()
