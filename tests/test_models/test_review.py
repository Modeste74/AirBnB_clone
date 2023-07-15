#!/usr/bin/python3
"""defines tests"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_instantiation(self):
        """Test obj is created"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_place_id(self):
        """test place_id attr"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        review.place_id = "12345"
        self.assertEqual(review.place_id, "12345")

    def test_text_attr(self):
        """test the user_id attr"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")
        review.text = "Great place!"
        self.assertEqual(review.text, "Great place!")

    def test_user_id(self):
        """test user_id attr"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        review.user_id = "54321"
        self.assertEqual(review.user_id, "54321")

    def test_to_dict(self):
        """test conversion of
        obj attr to dict for
        JSON"""
        review = Review()
        review.place_id = "12345"
        review.user_id = "54321"
        review.text = "Great place!"
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["place_id"], "12345")
        self.assertEqual(review_dict["user_id"], "54321")
        self.assertEqual(review_dict["text"], "Great place!")

    def test_from_dict(self):
        """test creating an obj
        from a dictionary
        """
        review_dict = {
                "__class__": "Review",
                "place_id": "12345",
                "user_id": "54321",
                "text": "Great place!",
                "id": "98765",
                "created_at": "2023-07-14T12:00:00.000000",
                "updated_at": "2023-07-14T13:00:00.000000"
                }
        review = Review(**review_dict)
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, "12345")
        self.assertEqual(review.user_id, "54321")
        self.assertEqual(review.text, "Great place!")
        self.assertEqual(review.id, "98765")
        self.assertEqual(review.created_at.isoformat(), "2023-07-14T12:00:00")
        self.assertEqual(review.updated_at.isoformat(), "2023-07-14T13:00:00")

    def test_str(self):
        """test string rep of obj"""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))


if __name__ == "__main__":
    unittest.main()
