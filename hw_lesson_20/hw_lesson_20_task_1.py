"""
Task 1

Pick your solution to one of the exercises in this module.
Design tests for this solution and write tests using unittest library.
"""
import unittest
from email_validation import ContactInfo


class EmailValidationTest(unittest.TestCase):
    wrong_sample = ["abc-@mail.com", "abc..def@mail.com",
                    ".abc@mail.com", "abc#def@mail.com",
                    "abc.def@mail.c", "abc.def@mail#archive.com",
                    "abc.def@mail", "abc.def@mail..com"]

    correct_sample = ["abc-d@mail.com", "abc.def@mail.com",
                      "abc@mail.com", "abc_def@mail.com"]

    def testValidationError(self):
        for email in self.wrong_sample:
            self.assertRaises(ValueError, ContactInfo.validate, email)

    def testValidationAccept(self):
        for email in self.correct_sample:
            self.assertEqual(email, ContactInfo.validate(email))


if __name__ == "__main__":
    unittest.main()
