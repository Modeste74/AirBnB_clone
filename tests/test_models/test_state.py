#!/usr/bin/python3
"""defines unittest"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """defines test for testcase"""
    def test_instantiation(self):
        """Test that obj is created"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "")

    def test_name_attribute(self):
        """Tests the name attribute"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
        state.name = "Florida"
        self.assertEqual(state.name, "Florida")

    def test_to_dict(self):
        """test the obj to
        to dictionary for JSON
        """
        state = State()
        state.name = "Florida"
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["name"], "Florida")

    def test_from_dict(self):
        """test for creation of
        an object from dictionary
        """
        state_dict = {
                "__class__": "State",
                "name": "Florida",
                "id": "12345",
                "created_at": "2023-07-14T12:00:00.000000",
                "updated_at": "2023-07-14T13:00:00.000000"
                }
        state = State(**state_dict)
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "Florida")
        self.assertEqual(state.id, "12345")
        self.assertEqual(state.created_at.isoformat(), "2023-07-14T12:00:00")
        self.assertEqual(state.updated_at.isoformat(), "2023-07-14T13:00:00")

    def test_str(self):
        """test the string rep
        of an object"""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))


if __name__ == '__main__':
    unittest.main()
