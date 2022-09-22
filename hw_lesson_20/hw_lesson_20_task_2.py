"""
Task 2

Write tests for the Phonebook application, which you have implemented in module 1.
Design tests for this solution and write tests using unittest library
"""
import unittest
import telephone_book


class PhonebookFunctionalityTest(unittest.TestCase):
    def setUp(self):
        self.phonebook = "test_phonebook"

    def testSearch(self):
        for key in ['Cleveland', 'John', 'John Doe', 'Doe', '741299', 'Ohio']:
            self.assertEqual(telephone_book.search(key, self.phonebook), {'city': 'Cleveland',
                                                                          'first_name': 'John',
                                                                          'full_name': 'John Doe',
                                                                          'last_name': 'Doe',
                                                                          'phone_number': '741299',
                                                                          'state': 'Ohio'})

    def testAddContact(self):
        contact = {"first_name": "Bob",
                   "last_name": "Callagan",
                   "full_name": "Bob Callagan",
                   "phone_number": "874010",
                   "state": "Alaska",
                   "city": "Juneau"}
        telephone_book.write_new_contact("test_phonebook", contact)
        self.assertEqual(telephone_book.search("874010", self.phonebook), contact)

    def testUpdateContact(self):
        updated_contact = {"first_name": "Bob",
                           "last_name": "Callagan",
                           "full_name": "Bob Callagan",
                           "phone_number": "331109",
                           "state": "Alaska",
                           "city": "Juneau"}
        telephone_book.update_record("874010", updated_contact, "test_phonebook")
        self.assertEqual(telephone_book.search("331109", self.phonebook), updated_contact)


if __name__ == "__main__":
    unittest.main()
