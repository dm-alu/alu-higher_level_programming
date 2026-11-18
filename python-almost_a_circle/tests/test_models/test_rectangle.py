
def tearDown(self):
        """Remove the file created by the tests."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_rectangle_two_arguments(self):
        """Check Rectangle(1, 2)."""
        rect = Rectangle(1, 2)
        self.assertEqual((rect.id, rect.width, rect.height, rect.x, rect.y),
                         (1, 1, 2, 0, 0))

    def test_rectangle_three_arguments(self):
        """Check Rectangle(1, 2, 3)."""
        rect = Rectangle(1, 2, 3)
        self.assertEqual((rect.id, rect.width, rect.height, rect.x, rect.y),
                         (1, 1, 2, 3, 0))

    def test_rectangle_four_arguments(self):
        """Check Rectangle(1, 2, 3, 4)."""
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual((rect.id, rect.width, rect.height, rect.x, rect.y),
                         (1, 1, 2, 3, 4))

    def test_rectangle_five_arguments(self):
        """Check Rectangle(1, 2, 3, 4, 5)."""
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((rect.id, rect.width, rect.height, rect.x, rect.y),
                         (5, 1, 2, 3, 4))

    def test_width_string(self):
        """Check Rectangle("1", 2)."""
        with self.assertRaises(TypeError) as cm:
            Rectangle("1", 2)
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_height_string(self):
        """Check Rectangle(1, "2")."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(1, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")

    def test_x_string(self):
        """Check Rectangle(1, 2, "3")."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(1, 2, "3")
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_y_string(self):
        """Check Rectangle(1, 2, 3, "4")."""
        with self.assertRaises(TypeError) as cm:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_width_negative(self):
        """Check Rectangle(-1, 2)."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(-1, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_height_negative(self):
        """Check Rectangle(1, -2)."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, -2)
        self.assertEqual(str(cm.exception), "height must be > 0")

    def test_width_zero(self):
        """Check Rectangle(0, 2)."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(0, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_height_zero(self):
        """Check Rectangle(1, 0)."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, 0)
        self.assertEqual(str(cm.exception), "height must be > 0")

    def test_x_negative(self):
        """Check Rectangle(1, 2, -3)."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, 2, -3)
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_y_negative(self):
        """Check Rectangle(1, 2, 3, -4)."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, 2, 3, -4)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_area_values(self):
        """Check area() with different sizes."""
        self.assertEqual(Rectangle(1, 2).area(), 2)
        self.assertEqual(Rectangle(3, 4, 5, 6).area(), 12)
        self.assertEqual(Rectangle(7, 7).area(), 49)

    def test_str_values(self):
        """Check __str__() with different values."""
        self.assertEqual(str(Rectangle(1, 2)), "[Rectangle] (1) 0/0 - 1/2")
        self.assertEqual(str(Rectangle(1, 2, 3, 4, 5)),
                         "[Rectangle] (5) 3/4 - 1/2")

    def test_display_without_x_and_y(self):
        """Check display() without x and y."""
        self.assertEqual(self.capture(Rectangle(3, 2)), "###\n###\n")

    def test_display_without_y(self):
        """Check display() without y."""
        self.assertEqual(self.capture(Rectangle(2, 2, 1)), " ##\n ##\n")

    def test_display_with_x_and_y(self):
        """Check display() with x and y."""
        self.assertEqual(self.capture(Rectangle(2, 2, 1, 1)),
                         "\n ##\n ##\n")

    def test_to_dictionary_values(self):
        """Check to_dictionary() with the five attributes."""
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.to_dictionary(),
                         {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(set(rect.to_dictionary()),
                         {"id", "width", "height", "x", "y"})

    def attributes(self, rect):
        """Return the five attributes of a rectangle in a tuple."""
        return (rect.id, rect.width, rect.height, rect.x, rect.y)

    def test_update_no_arguments(self):
        """Check update() without arguments."""
        rect = Rectangle(10, 11, 12, 13, 14)
        rect.update()
        self.assertEqual(self.attributes(rect), (14, 10, 11, 12, 13))

    def test_update_one_argument(self):
        """Check update(89)."""
        rect = Rectangle(10, 11, 12, 13, 14)
        rect.update(89)
        self.assertEqual(self.attributes(rect), (89, 10, 11, 12, 13))

    def test_update_two_arguments(self):
        """Check update(89, 1)."""
        rect = Rectangle(10, 11, 12, 13, 14)
        rect.update(89, 1)
        self.assertEqual(self.attributes(rect), (89, 1, 11, 12, 13))

    def test_update_three_arguments(self):
        """Check update(89, 1, 2)."""
        rect = Rectangle(10, 11, 12, 13, 14)
        rect.update(89, 1, 2)
        self.assertEqual(self.attributes(rect), (89, 1, 2, 12, 13))

    def test_update_four_arguments(self):
        """Check update(89, 1, 2, 3)."""
        rect = Rectangle(10, 11, 12, 13, 14)
        rect.update(89, 1, 2, 3)
        self.assertEqual(self.attributes(rect), (89, 1, 2, 3, 13))

    def test_update_five_arguments(self):
        """Check update(89, 1, 2, 3, 4)."""
        rect = Rectangle(10, 11, 12, 13, 14)
        rect.update(89, 1, 2, 3, 4)
        self.assertEqual(self.attributes(rect), (89, 1, 2, 3, 4))

    def test_update_kwargs_id(self):
        """Check update(**{'id': 89})."""
        rect = Rectangle(10, 11, 12, 13, 14)
        rect.update(**{'id': 89})
        self.assertEqual(self.attributes(rect), (89, 10, 11, 12, 13))

    def test_update_kwargs_id_width(self):
        """Check update(**{'id': 89, 'width': 1})."""
        rect = Rectangle(10, 11, 12, 13, 14)
        rect.update(**{'id': 89, 'width': 1})
        self.assertEqual(self.attributes(rect), (89, 1, 11, 12, 13))

    def test_update_kwargs_id_width_height(self):
        """Check update(**{'id': 89, 'width': 1, 'height': 2})."""
        rect = Rectangle(10, 11, 12, 13, 14)
        rect.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(self.attributes(rect), (89, 1, 2, 12, 13))

    def test_update_kwargs_four_keys(self):
        """Check update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})."""
        rect = Rectangle(10, 11, 12, 13, 14)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(self.attributes(rect), (89, 1, 2, 3, 13))

    def test_update_kwargs_five_keys(self):
        """Check update with the five keys."""
        rect = Rectangle(10, 11, 12, 13, 14)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(self.attributes(rect), (89, 1, 2, 3, 4))

    def test_create_id(self):
        """Check Rectangle.create(**{'id': 89})."""
        rect = Rectangle.create(**{'id': 89})
        self.assertIs(type(rect), Rectangle)
        self.assertEqual(rect.id, 89)

    def test_create_id_width(self):
        """Check Rectangle.create(**{'id': 89, 'width': 1})."""
        rect = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual((rect.id, rect.width), (89, 1))

    def test_create_id_width_height(self):
        """Check Rectangle.create with id, width and height."""
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual((rect.id, rect.width, rect.height), (89, 1, 2))

    def test_create_four_keys(self):
        """Check Rectangle.create with id, width, height and x."""
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(self.attributes(rect), (89, 1, 2, 3, 0))

    def test_create_five_keys(self):
        """Check Rectangle.create with the five keys."""
        rect = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(self.attributes(rect), (89, 1, 2, 3, 4))

    def test_save_to_file_none(self):
        """Check Rectangle.save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Check Rectangle.save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as a_file:
            self.assertEqual(a_file.read(), "[]")

    def test_save_to_file_one_rectangle(self):
        """Check Rectangle.save_to_file([Rectangle(1, 2)])."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as a_file:
            content = a_file.read()
        self.assertEqual(json.loads(content), [
            {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}])
        self.assertEqual(len(content), len(json.dumps(json.loads(content))))

    def test_load_from_file_does_not_exist(self):
        """Check Rectangle.load_from_file() when the file does not exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Check Rectangle.load_from_file() when the file exists."""
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4, 5), Rectangle(6, 7)])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertIs(type(loaded[0]), Rectangle)
        self.assertEqual(self.attributes(loaded[0]), (5, 1, 2, 3, 4))
        self.assertEqual(loaded[1].to_dictionary(),
                         {"id": 1, "width": 6, "height": 7, "x": 0, "y": 0})


if __name__ == "__main__":
    unittest.main()
