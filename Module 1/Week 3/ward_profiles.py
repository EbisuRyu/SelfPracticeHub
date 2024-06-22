from abc import ABC, abstractmethod


class Person(ABC):
    """ Abstract base class representing a person with common attributes and methods."""

    def __init__(self, name, yob):
        """ Initialize a new Person instance with name and year of birth.

        Args:
            name (str): The name of the person.
            yob (int): The year of birth of the person.
        """
        self._type = None  # This will be set in subclass
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        """ Abstract method to describe the person. Must be implemented by subclasses."""
        pass


class Student(Person):
    """ Represents a student, a subclass of Person."""

    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade
        self._type = 'Student'

    def describe(self):
        """ Print a description of the student including their type, name, year of birth, and grade."""
        script = f'{self._type} - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}'
        print(script)


class Teacher(Person):
    """ Represents a teacher, a subclass of Person."""

    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject
        self._type = 'Teacher'

    def describe(self):
        """ Print a description of the teacher including their type, name, year of birth, and subject taught."""
        script = f'{self._type} - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}'
        print(script)


class Doctor(Person):
    """ Represents a doctor, a subclass of Person."""

    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist
        self._type = 'Doctor'

    def describe(self):
        """ Print a description of the doctor including their type, name, year of birth, and specialization."""
        script = f'{self._type} - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}'
        print(script)


class Ward:
    """ Represents a Ward which contains a list of persons including students, teachers, and doctors."""

    def __init__(self, name):
        """ Initialize a new Ward with a name and an empty list of persons.

        Args:
            name (str): The name of the ward.
        """
        self.__ward_name = name
        self.__profiles = []

    def add_person(self, person):
        """ Add a person to the ward.

        Args:
            person (Person): The person to add to the ward.
        """
        self.__profiles.append(person)

    def describe(self):
        """ Print the name of the ward and the description of each person in the ward."""
        print(f'Ward Name: {self.__ward_name}')
        for person in self.__profiles:
            person.describe()

    def count_doctor(self):
        """ Count the number of doctors in the ward.

        Returns:
            int: Number of doctors in the ward.
        """
        doctors = [
            person for person in self.__profiles if person._type == 'Doctor']
        return len(doctors)

    def sort_age(self):
        """ Sort the persons in the ward by their year of birth in descending order."""
        self.__profiles.sort(key=lambda person: int(person._yob), reverse=True)

    def compute_average(self):
        """ Compute the average year of birth of teachers in the ward.

        Returns:
            float: Average year of birth of all teachers.
        """
        teacher_age = [int(person._yob)
                       for person in self.__profiles if person._type == 'Teacher']
        return float(sum(teacher_age) / len(teacher_age))


# Example
# 2(a)
student1 = Student(name='studentA', yob=2010, grade='7')
student1.describe()

teacher1 = Teacher(name='teacherA', yob=1969, subject='Math')
teacher1.describe()

doctor1 = Doctor(name='doctorA', yob=1945, specialist='Endocrinologists')
doctor1.describe()

# 2(b)
print()  # Print an empty line for better readability

# Create new Teacher and Doctor objects
teacher2 = Teacher(name='teacherB', yob=1995, subject='History')
doctor2 = Doctor(name='doctorB', yob=1975, specialist='Cardiologists')

# Initialize a Ward object and add people to the ward
ward1 = Ward(name='Ward1')
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

# Describe the ward and its members
ward1.describe()

# 2(c)
print(f"\nNumber of doctors: {ward1.count_doctor()}")

# 2(d)
print("\nAfter sorting the age of people in Ward1")
ward1.sort_age()
ward1.describe()

# 2(e)
average_yob_teachers = ward1.compute_average()
print(
    f"\nAverage year of birth for teachers in the ward: {average_yob_teachers:.2f}")
