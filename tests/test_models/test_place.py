#!/usr/bin/python3
"""defines test"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """define TestPlace class"""
    def test_instantiation(self):
        """test for creation of objs"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_city_id(self):
        """test the city_id
        attr"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
        place.city_id = "12345"
        self.assertEqual(place.city_id, "12345")

    def test_user_id(self):
        """test the user_id attr"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
        place.user_id = "54321"
        self.assertEqual(place.user_id, "54321")

    def test_name_attr(self):
        """tests the name attr"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
        place.name = "Apartment"
        self.assertEqual(place.name, "Apartment")

    def test_description_attr(self):
        """tests the description attr"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")
        place.description = "A beautiful apartment"
        self.assertEqual(place.description, "A beautiful apartment")

    def test_no_of_rooms(self):
        """test the no_rooms attr"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)
        place.number_rooms = 5
        self.assertEqual(place.number_rooms, 5)

    def test_no_bathrooms(self):
        """test for no of
        bathroom attr
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)
        place.number_bathrooms = 1
        self.assertEqual(place.number_bathrooms, 1)

    def test_max_guest(self):
        """test the max
        guest attr
        """
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)
        place.max_guest = 4
        self.assertEqual(place.max_guest, 4)

    def test_price_by_night(self):
        """test the price by
        night attr
        """
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
        place.price_by_night = 100
        self.assertEqual(place.price_by_night, 100)

    def test_latitude_attr(self):
        """test the latitude attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)
        place.latitude = 37.7749
        self.assertEqual(place.latitude, 37.7749)

    def test_longitude_attr(self):
        """test the longitude attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
        place.longitude = -122.4194
        self.assertEqual(place.longitude, -122.4194)

    def test_amenity_ids_attr(self):
        """test the amenity
        id attr"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])
        place.amenity_ids = ["001", "002", "003"]
        self.assertEqual(place.amenity_ids, ["001", "002", "003"])

    def test_to_dict(self):
        """Test conversion of obj
        to dictionary for JSON
        """
        place = Place()
        place.city_id = "12345"
        place.user_id = "54321"
        place.name = "Apartment"
        place.description = "A beautiful apartment"
        place.number_rooms = 5
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["001", "002", "003"]
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["city_id"], "12345")
        self.assertEqual(place_dict["user_id"], "54321")
        self.assertEqual(place_dict["name"], "Apartment")
        self.assertEqual(place_dict["description"], "A beautiful apartment")
        self.assertEqual(place_dict["number_rooms"], 5)
        self.assertEqual(place_dict["number_bathrooms"], 1)
        self.assertEqual(place_dict["max_guest"], 4)
        self.assertEqual(place_dict["price_by_night"], 100)
        self.assertEqual(place_dict["latitude"], 37.7749)
        self.assertEqual(place_dict["longitude"], -122.4194)
        self.assertEqual(place_dict["amenity_ids"], ["001", "002", "003"])

    def test_from_dict(self):
        """test of creation of
        an obj from a dict
        """
        place_dict = {
                "__class__": "Place",
                "city_id": "12345",
                "user_id": "54321",
                "name": "Apartment",
                "description": "A beautiful apartment",
                "number_rooms": 5,
                "number_bathrooms": 1,
                "max_guest": 4,
                "price_by_night": 100,
                "latitude": 37.7749,
                "longitude": -122.4194,
                "amenity_ids": ["001", "002", "003"],
                "id": "98765",
                "created_at": "2023-07-14T12:00:00.000000",
                "updated_at": "2023-07-14T13:00:00.000000"
                }
        place = Place(**place_dict)
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "12345")
        self.assertEqual(place.user_id, "54321")
        self.assertEqual(place.name, "Apartment")
        self.assertEqual(place.description, "A beautiful apartment")
        self.assertEqual(place.number_rooms, 5)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["001", "002", "003"])
        self.assertEqual(place.id, "98765")
        self.assertEqual(place.created_at.isoformat(), "2023-07-14T12:00:00")
        self.assertEqual(place.updated_at.isoformat(), "2023-07-14T13:00:00")

    def test_str(self):
        """test the string rep"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))

if __name__ == "__main__":
    unittest.main()
