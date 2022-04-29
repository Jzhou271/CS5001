class Gradebook:
    '''
    A Gradebook is an object that contains all the information for a
    single course. It knows the name of the course, the year, the semester,
    and all of the students in the class along with their grades.

    The Gradebook needs to store each of those pieces of information in their
    attribute. The name of the course is a string, the year is an int, the
    semester is a String containing one of three possible values "Fall",
    "Spring", "Summer", the instructor's name is a string, and the students
    and their grades are stored in a dictionary where the key is the student's
    name (str) and the value is the current number of points they have
    received on each assignment (list of int).
    '''

    def __init__(self, course_name, year, semester, instructor, students):
        '''
        Initialize a new Gradebook object.

        A ValueError is raised if the input has the wrong type of input.
        A ValueError is raised if the input year is less than 2000.
        :param course_name: a string of the course name
        :param year: the year of the course, must be an int
        :param semester: one of the following values Fall, Spring, Summer
        :param instructor: the name of the instructor, as a string
        :param students: a list of student names (strings)
        '''
        if type(course_name) is not str:
            raise ValueError("Invalid course_name provided to this Gradebook")
        if type(year) != int or year < 2000:
            raise ValueError("Invalid year provided to this Gradebook")
        if semester not in ["Fall", "Spring", "Summer"]:
            raise ValueError("Invalid semester provided to this Gradebook")
        if type(semester) is not str:
            raise ValueError("Invalid semester provided to this Gradebook")
        if type(instructor) is not str:
            raise ValueError("Invalid instructor provided to this Gradebook")
        if type(students) is not list:
            raise ValueError("Invalid students provided to this Gradebook")
        for stu in students:
            if type(stu) is not str:
                raise ValueError("Invalid students provided to this Gradebook")
        self.course_name = course_name
        self.year = year
        self.semester = semester
        self.instructor = instructor
        self.students = students
        self.grade_dictionary = self.initialize_grade_dictionary()

    def average_grade(self):
        '''
        Returns the average (arithmetic mean) number of points
        received py the students in the class.
        :return: average number of point earned
        '''
        count = 0
        for stu in self.grade_dictionary:
            count += sum(self.grade_dictionary[stu])
        return count / len(self.grade_dictionary)

    def letter_grade(self, total_points):
        '''
        Given the total points available returns a dictionary
        that has the student name along with their corresponding
        letter grade.
        The following is the grade scale
        93.00–100.00   A
        90.00–92.99    A-
        86.00–89.99    B+
        82.00–85.99   B
        77.00–81.99    B-
        73.00–76.99    C+
        69.00–72.99   C
        65.00–68.99   C-
        0.00–64.99    F

        If a grade would be out of this range a ValueError should be raised.
        If the total number of points available is less than 1 a ValueError
        should be raised.

        :param total_points: the total number of points (int) available in
        the class so far
        :return:a dictionary with a key of a student's name and a value of
        the letter grade (str)
        '''
        d = {}
        if total_points < 1:
            raise ValueError("Invalid Total Points")
        for stu in self.students:
            d[stu] = 0
            for grade in self.grade_dictionary[stu]:
                if grade < 0 or grade > 100:
                    raise ValueError("Invalid Grade")
                d[stu] += grade
        res = {}
        for stu in d:
            grade = d[stu] / total_points
            if 93 <= grade <= 100:
                res[stu] = "A"
            elif 90 <= grade:
                res[stu] = "A-"
            elif 86 <= grade:
                res[stu] = "B+"
            elif 82 <= grade:
                res[stu] = "B"
            elif 77 <= grade:
                res[stu] = "B-"
            elif 73 <= grade:
                res[stu] = "C+"
            elif 69 <= grade:
                res[stu] = "C"
            elif 65 <= grade:
                res[stu] = "C-"
            elif 0 <= grade:
                res[stu] = "F"
        return res

    # the following methods are assumed to exist, but do not need to be tested
    # you can rely on them in your tests

    def add_grade(self, assignment_grades):
        '''
        This takes a dictionary as input. The dictionary has student names as
        a key and the points for an assignment as the value.
        This methods will add the grade for each student to the dictionary in
        the class that has student as key and the value is the list of all the
        grades so far.
        So if this class attribute that contains the grades has 2 grades for
        each student, after running this method there would be 3 grades for
        each student.
        :param assignment_grades: a dictionary that has student names as keys,
        and their grade on a single assignment as the values
        '''
        for stu in assignment_grades:
            self.grade_dictionary[stu].append(assignment_grades[stu])

    def get_grades(self):
        '''
        This method returns the dictionary of student grades for this course.
        The dictionary has the student names as keys, and a list of all of
        their grades as values
        :return: The dictionary of student grades
        '''
        return self.grade_dictionary

    def initialize_grade_dictionary(self):
        '''
        This is a helper function for the constructor. It takes a list of
        students that is passed into __init__ and creates a dictionary where
        each student name is a key, and an empty list is the value.
        :return: A new dictionary with student names as keys, and an empty
        list as values
        '''
        grade_dictionary = {}
        for stu in self.students:
            grade_dictionary[stu] = []
        return grade_dictionary
