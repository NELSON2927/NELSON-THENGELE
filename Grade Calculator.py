def input_student_grades():
    students_grades = {}
    
    while True:
        name = input("Enter the student's name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        
        
        while True:
            try:
                grade = float(input(f"Enter {name}'s grade: ").strip())
                break 
            except ValueError:
                print("Invalid grade. Please enter a numeric value.")
        
        students_grades[name] = grade
    
    return students_grades



def calculate_and_display_results(students_grades):
    if not students_grades:
        print("No student data was entered.")
        return

    
    average_grade = sum(students_grades.values()) / len(students_grades)
    
   
    highest_grade_student = max(students_grades, key=students_grades.get)
    highest_grade = students_grades[highest_grade_student]
    
    
    print("\n--- Results ---")
    print("Student Grades:")
    for student, grade in students_grades.items():
        print(f"{student}: {grade}")
    
    print(f"\nAverage grade for all students: {average_grade:.2f}")
    print(f"Student with the highest grade: {highest_grade_student} ({highest_grade})")



def main():
    print("Welcome to the Grade Calculator!")
    
 
    students_grades = input_student_grades()
    
    
    calculate_and_display_results(students_grades)



if __name__ == "__main__":
    main()