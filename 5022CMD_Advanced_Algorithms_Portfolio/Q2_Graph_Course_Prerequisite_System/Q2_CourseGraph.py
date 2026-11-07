# Question 2: Graph - Course Prerequisite System


# Course entity class
class Course:
    def __init__(self, course_code, course_name, credit_hours, level, semester):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.level = level
        self.semester = semester

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"

    def display_details(self):
        print("\n=== COURSE DETAILS ===")
        print("Course Code:", self.course_code)
        print("Course Name:", self.course_name)
        print("Credit Hours:", self.credit_hours)
        print("Level:", self.level)
        print("Semester:", self.semester)


# Directed Graph class
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination):
        # source unlocks destination
        if source not in self.adjacency_list:
            self.add_vertex(source)

        if destination not in self.adjacency_list:
            self.add_vertex(destination)

        self.adjacency_list[source].append(destination)

    def list_incoming_adjacent_vertex(self, vertex):
        incoming_courses = []

        for source in self.adjacency_list:
            if vertex in self.adjacency_list[source]:
                incoming_courses.append(source)

        return incoming_courses

    def list_outgoing_adjacent_vertex(self, vertex):
        return self.adjacency_list[vertex]

    def display_all_courses(self):
        print("\n=== ALL COURSES ===")

        for course in self.adjacency_list:
            print(course)


def find_course(course_list, course_code):
    for course in course_list:
        if course.course_code == course_code:
            return course

    return None


def main():
    # Create Course objects
    course1 = Course("5001CMD", "Programming Principles", 20, "Core", 1)
    course2 = Course("5002CMD", "Database Systems", 20, "Core", 1)
    course3 = Course("5005CMD", "Data Structures and Algorithms", 20, "Core", 2)
    course4 = Course("5011CEM", "Big Data Programming Project", 20, "Core", 2)
    course5 = Course("5022CMD", "Advanced Algorithms", 10, "Core", 3)
    course6 = Course("5024CMD", "Artificial Intelligence", 10, "Elective", 3)
    course7 = Course("6001CMP", "Final Year Project", 30, "Core", 4)

    course_list = [
        course1,
        course2,
        course3,
        course4,
        course5,
        course6,
        course7
    ]

    # Create graph
    graph = Graph()

    # Add all courses as vertices
    for course in course_list:
        graph.add_vertex(course)

    # Add prerequisite relationships
    # A -> B means completing A unlocks B
    graph.add_edge(course1, course3)
    graph.add_edge(course2, course4)
    graph.add_edge(course3, course5)
    graph.add_edge(course3, course6)
    graph.add_edge(course5, course7)
    graph.add_edge(course4, course7)

    while True:
        print("\n=== COURSE PREREQUISITE SYSTEM ===")
        print("1. Display All Courses")
        print("2. View Course Details")
        print("3. View Prerequisite Courses")
        print("4. View Courses Unlocked")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            graph.display_all_courses()

        elif choice == "2":
            course_code = input("Enter course code: ").upper()
            course = find_course(course_list, course_code)

            if course is not None:
                course.display_details()
            else:
                print("Course not found.")

        elif choice == "3":
            course_code = input("Enter course code: ").upper()
            course = find_course(course_list, course_code)

            if course is not None:
                prerequisites = graph.list_incoming_adjacent_vertex(course)

                print(f"\n=== PREREQUISITES FOR {course.course_code} ===")

                if len(prerequisites) == 0:
                    print("No prerequisite courses.")
                else:
                    for prerequisite in prerequisites:
                        print(prerequisite)
            else:
                print("Course not found.")

        elif choice == "4":
            course_code = input("Enter course code: ").upper()
            course = find_course(course_list, course_code)

            if course is not None:
                unlocked_courses = graph.list_outgoing_adjacent_vertex(course)

                print(f"\n=== COURSES UNLOCKED BY {course.course_code} ===")

                if len(unlocked_courses) == 0:
                    print("This course does not unlock any courses.")
                else:
                    for unlocked_course in unlocked_courses:
                        print(unlocked_course)
            else:
                print("Course not found.")

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please enter 1 to 5.")


main()