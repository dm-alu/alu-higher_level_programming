
def test_id_assigned_automatically(self):
        """Check that Base() assigns an id automatically."""
        self.assertEqual(Base().id, 1)

    def test_id_is_previous_plus_one(self):
        """Check that Base() takes the id of the previous one plus one."""
        first = Base()
        second = Base()
        self.assertEqual(second.id, first.id + 1)
        self.assertEqual(Base().id, second.id + 1)

    def test_id_passed_is_saved(self):
        """Check that Base(89) saves the id passed."""
        self.assertEqual(Base(89).id, 89)

    def test_id_after_given_id(self):
        """Check that a given id does not move the automatic counter."""
        first = Base()
        Base(89)
        self.assertEqual(Base().id, first.id + 1)

    def test_to_json_string_dictionary_with_id(self):
        """Check Base.to_json_string([{'id': 12}])."""
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_to_json_string_returns_a_string(self):
        """Check that to_json_string returns a str."""
        self.assertIs(type(Base.to_json_string([{'id': 12}])), str)
        self.assertIs(type(Base.to_json_string(None)), str)
        self.assertIs(type(Base.to_json_string([])), str)

    def test_from_json_string_with_id(self):
        """Check Base.from_json_string('[{ "id": 89 }]')."""
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'),
                         [{'id': 89}])

    def test_from_json_string_returns_a_list(self):
        """Check that from_json_string returns a list."""
        self.assertIs(type(Base.from_json_string('[{ "id": 89 }]')), list)
        self.assertIs(type(Base.from_json_string(None)), list)
        self.assertIs(type(Base.from_json_string("[]")), list)


if __name__ == "__main__":
    unittest.main()
