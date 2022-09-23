"""
Task 2

Writing tests for context manager

Take your implementation of the context manager class from Task 1 and write tests for it.
Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed.
And also, write tests when your class raises errors or you have errors in the runtime context suite.
"""
import io
import unittest
from hw_lesson_21_task_1 import MyOpen


class MyOpenTest(unittest.TestCase):
    modificators = ("r", "a", "w")

    def setUp(self):
        with open("test.txt", "w") as file:
            file.write("TEST")

    def testExistingFile(self):
        with MyOpen("test.txt", "r") as file:
            sample = file.read()
        self.assertEqual("TEST", sample)

    def testNonExistingFile(self):
        self.assertRaises(FileNotFoundError, MyOpen, "non-test.txt", "r")

    def testExistingEncoding(self):
        with open("test.txt", "r", encoding="utf8") as file:
            sample = file.read()
        self.assertEqual("TEST", sample)

    def testNonExistingEncoding(self):
        with self.assertRaises(LookupError):
            with open("test.txt", "r", encoding="encoding") as file:
                sample = file.read()
            self.assertEqual("TEST", sample)

    def testAccessModificatorsErrors(self):
        with self.assertRaises(io.UnsupportedOperation):
            for modificator in self.modificators:
                with open("test.txt", modificator) as file:
                    file.read()
                    file.write("TEST")

    def testAccessModificators(self):
        for modificator in self.modificators[1:]:
            with open("test.txt", modificator) as file:
                if modificator == "a":
                    file.write("TEST")
                    testphrase = "TESTTEST"
                elif modificator == "w":
                    testphrase = "ANOTHER TEST"
                    file.write(testphrase)
            with open("test.txt", "r") as file:
                self.assertEqual(testphrase, file.read())

