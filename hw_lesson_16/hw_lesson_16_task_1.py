"""
Task 1

School

Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute,
while salary should only be available to the teacher.
"""


class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.favourite_activities = []
        self.subjects = {}

    def __str__(self):
        return f"\n\tName/Surname: {self.name} {self.surname}\n" \
               f"\tAge: {self.age}\n" \
               f"\tGender: {self.gender}\n"

    def __call__(self):
        return f"Hi, my name is {self.name} {self.surname} and I`m {self.age} years old!"

    def set_favourite_activities(self, *activities):
        for i in activities:
            if i not in self.favourite_activities:
                self.favourite_activities.append(i)

    def remove_favourite_activities(self, *activities):
        for i in activities:
            if i in self.favourite_activities:
                self.favourite_activities.remove(i)

    def set_subjects(self, **subjects):
        for key, value in subjects.items():
            if key not in self.subjects:
                self.subjects[key] = value

    def remove_subjects(self, **subjects):
        for key in subjects.keys():
            if key in self.subjects:
                self.subjects.pop(key)


class Student(Person):
    def __init__(self, name, surname, age, gender, course, *favourite_subjects):
        super().__init__(name,
                         surname,
                         age,
                         gender)
        self.course = course
        self.favourite_subjects = favourite_subjects

    def __str__(self):
        return f"\n\tName/Surname: {self.name} {self.surname}\n" \
               f"\tAge: {self.age}\n" \
               f"\tGender: {self.gender}\n " \
               f"\tCourse: {self.course}\n " \
               f"\tSubjects: {str({key:value for key, value in self.subjects.items()})}\n"

    def learn(self, subject, hours):
        self.subjects[subject] += hours/10


class Teacher(Person):
    def __init__(self, name, surname, age, gender, salary, experience):
        super().__init__(name,
                         surname,
                         age,
                         gender)
        self.salary = salary
        self.experience = experience

    def __str__(self):
        return f"\n\tName/Surname: {self.name} {self.surname}\n" \
               f"\tAge: {self.age}\n" \
               f"\tGender: {self.gender}\n " \
               f"\tExperience: {self.experience} years\n" \
               f"\tSubjects: {str({key:value for key, value in self.subjects.items()})}\n " \
               f"\tSalary: {self.salary}\n"

    def teach(self, student, subject, hours):
        if subject in self.subjects:
            student.learn(subject, hours)


if __name__ == "__main__":
    ...
