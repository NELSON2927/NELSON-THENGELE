class StudentDirectory:
    def __init__(self):
        
        self.students = []

    def add_student(self, name, age, grade):
        """Adds a new student to the directory."""
        student = {
            'name': name,
            'age': age,
            'grade': grade
        }
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def find_student(self, name):
        """Finds a student by name and prints their details."""
        for student in self.students:
            if student['name'].lower() == name.lower(): 
                print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
                return
        print(f"Student {name} not found.")

    def average_age(self):
        """Calculates and prints the average age of the students."""
        if not self.students:
            print("No students in the directory.")
            return
        
        total_age = sum(student['age'] for student in self.students)
        avg_age = total_age / len(self.students)
        print(f"Average age of students: {avg_age:.2f}")

    def display_menu(self):
        """Displays the menu options."""
        print("\nStudent Directory Menu:")
        print("1. Add Student")
        print("2. Find Student by Name")
        print("3. Calculate Average Age")
        print("4. Exit")

    def run(self):
        """Runs the main loop of the directory program."""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                name = input("Enter student's name: ")
                age = int(input("Enter student's age: "))
                grade = input("Enter student's grade: ")
                self.add_student(name, age, grade)
                
            elif choice == '2':
                name = input("Enter the name of the student to find: ")
                self.find_student(name)
            
            elif choice == '3':
                self.average_age()
                
            elif choice == '4':
                print("Exiting the program.")
                break
                
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    directory = StudentDirectory()
    directory.run()