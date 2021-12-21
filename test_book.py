import unittest
from Book import Book

class TestBook(unittest.TestCase):
    def test_list_person_type(self):
        self.assertIs(type(Book.listPersons), list)





