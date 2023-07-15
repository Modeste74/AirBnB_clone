#!/usr/bin/python3
"""Contains unit tests for console.py."""

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
import re
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """HBNB command interpreter Unit tests"""

    @classmethod
    def setUpClass(cls):
        # Initialize the storage object
        storage.reload()

    def setUp(self):
        # Create an instance of the console
        self.console = HBNBCommand()

    def tearDown(self):
        # Reset the storage object after each test
        storage.reload()

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("quit"))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF_command(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("EOF"))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

    def test_help_EOF_command(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("help EOF")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "Exit the hbnb program")

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

    def test_precmd_valid_command(self):
        line = "User.all()"
        result = self.console.precmd(line)
        self.assertEqual(result, "all User")

    def test_precmd_invalid_command(self):
        line = "InvalidCommand"
        result = self.console.precmd(line)
        self.assertEqual(result, line)

    def test_do_create_with_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_create_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_create_success(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            output = fake_out.getvalue().strip()
            pattern = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
            self.assertRegex(output, pattern)

    def test_do_show_with_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_show_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_show_with_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_show_with_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show BaseModel 123")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_show_success(self):
        instance = BaseModel()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"show BaseModel {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertIn(instance_id, output)

    def test_do_destroy_with_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_destroy_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_destroy_with_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_destroy_with_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy BaseModel 123")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_success(self):
        instance = BaseModel()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"destroy BaseModel {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")
            self.assertNotIn(instance_id, storage.all())

    def test_do_all_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_all_success_without_class_name(self):
        instance1 = BaseModel()
        instance1.save()
        instance2 = User()
        instance2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all")
            output = fake_out.getvalue().strip()
            self.assertIn(instance1.id, output)
            self.assertIn(instance2.id, output)

    def test_do_all_success_with_class_name(self):
        instance1 = BaseModel()
        instance1.save()
        instance2 = User()
        instance2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all BaseModel")
            output = fake_out.getvalue().strip()
            self.assertIn(instance1.id, output)
            self.assertNotIn(instance2.id, output)

    def test_do_count_with_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("count")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_count_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("count InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_update_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("update InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_update_with_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("update BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_update_with_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("update BaseModel 123")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "no instance found **")

    def test_do_update_with_attribute_name_missing(self):
        instance = BaseModel()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"update BaseModel {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

    def test_do_update_with_value_missing(self):
        instance = BaseModel()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(
                    f"update BaseModel {instance_id} attribute_name"
                    )
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    def test_do_create_base_model(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            output = fake_out.getvalue().strip()
            pattern = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
            self.assertRegex(output, pattern)

    def test_do_create_user(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create User")
            output = fake_out.getvalue().strip()
            pattern = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
            self.assertRegex(output, pattern)

    def test_do_create_place(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create Place")
            output = fake_out.getvalue().strip()
            pattern = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
            self.assertRegex(output, pattern)

    def test_do_create_city(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create City")
            output = fake_out.getvalue().strip()
            pattern = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
            self.assertRegex(output, pattern)

    def test_do_create_state(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create State")
            output = fake_out.getvalue().strip()
            pattern = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
            self.assertRegex(output, pattern)

    def test_do_create_amenity(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create Amenity")
            output = fake_out.getvalue().strip()
            pattern = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
            self.assertRegex(output, pattern)

    def test_do_create_review(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create Review")
            output = fake_out.getvalue().strip()
            pattern = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
            self.assertRegex(output, pattern)

    def test_do_create_without_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_create_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_show_base_model(self):
        instance = BaseModel()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"show BaseModel {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertIn(instance_id, output)

    def test_do_show_user(self):
        instance = User()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"show User {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertIn(instance_id, output)

    def test_do_show_place(self):
        instance = Place()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"show Place {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertIn(instance_id, output)

    def test_do_show_city(self):
        instance = City()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"show City {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertIn(instance_id, output)

    def test_do_show_state(self):
        instance = State()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"show State {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertIn(instance_id, output)

    def test_do_show_amenity(self):
        instance = Amenity()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"show Amenity {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertIn(instance_id, output)

    def test_do_show_review(self):
        instance = Review()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"show Review {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertIn(instance_id, output)

    def test_do_show_without_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_show_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_show_with_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_show_with_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show BaseModel 123")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_base_model(self):
        instance = BaseModel()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"destroy BaseModel {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")
            self.assertNotIn(instance_id, storage.all())

    def test_do_destroy_user(self):
        instance = User()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"destroy User {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")
            self.assertNotIn(instance_id, storage.all())

    def test_do_destroy_place(self):
        instance = Place()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"destroy Place {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")
            self.assertNotIn(instance_id, storage.all())

    def test_do_destroy_city(self):
        instance = City()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"destroy City {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")
            self.assertNotIn(instance_id, storage.all())

    def test_do_destroy_state(self):
        instance = State()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"destroy State {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")
            self.assertNotIn(instance_id, storage.all())

    def test_do_destroy_amenity(self):
        instance = Amenity()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"destroy Amenity {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")
            self.assertNotIn(instance_id, storage.all())

    def test_do_destroy_review(self):
        instance = Review()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"destroy Review {instance_id}")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")
            self.assertNotIn(instance_id, storage.all())

    def test_do_destroy_without_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_destroy_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_destroy_with_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_destroy_with_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy BaseModel 123")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_all_base_model(self):
        instance1 = BaseModel()
        instance1.save()
        instance2 = BaseModel()
        instance2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all BaseModel")
            output = fake_out.getvalue().strip()
            self.assertIn(instance1.id, output)
            self.assertIn(instance2.id, output)

    def test_do_all_user(self):
        instance1 = User()
        instance1.save()
        instance2 = User()
        instance2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all User")
            output = fake_out.getvalue().strip()
            self.assertIn(instance1.id, output)
            self.assertIn(instance2.id, output)

    def test_do_all_place(self):
        instance1 = Place()
        instance1.save()
        instance2 = Place()
        instance2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all Place")
            output = fake_out.getvalue().strip()
            self.assertIn(instance1.id, output)
            self.assertIn(instance2.id, output)

    def test_do_all_city(self):
        instance1 = City()
        instance1.save()
        instance2 = City()
        instance2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all City")
            output = fake_out.getvalue().strip()
            self.assertIn(instance1.id, output)
            self.assertIn(instance2.id, output)

    def test_do_all_state(self):
        instance1 = State()
        instance1.save()
        instance2 = State()
        instance2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all State")
            output = fake_out.getvalue().strip()
            self.assertIn(instance1.id, output)
            self.assertIn(instance2.id, output)

    def test_do_all_amenity(self):
        instance1 = Amenity()
        instance1.save()
        instance2 = Amenity()
        instance2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all Amenity")
            output = fake_out.getvalue().strip()
            self.assertIn(instance1.id, output)
            self.assertIn(instance2.id, output)

    def test_do_all_review(self):
        instance1 = Review()
        instance1.save()
        instance2 = Review()
        instance2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all Review")
            output = fake_out.getvalue().strip()
            self.assertIn(instance1.id, output)
            self.assertIn(instance2.id, output)

    def test_do_all_without_class_name(self):
        instance1 = BaseModel()
        instance1.save()
        instance2 = User()
        instance2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all")
            output = fake_out.getvalue().strip()
            self.assertIn(instance1.id, output)
            self.assertIn(instance2.id, output)

    def test_do_all_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_update_with_invalid_class_name(self):
        instance = BaseModel()
        instance.save()
        instance_id = instance.id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(
                    f"update InvalidClass {instance_id} name 'New Name'"
                    )
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_update_without_instance_id(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("update BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")


if __name__ == '__main__':
    unittest.main()
