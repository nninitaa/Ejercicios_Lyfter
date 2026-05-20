class Student:
    def __init__(self, name, section, spanish, english, social, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science
        
    def average(self):
        total = sum([self.spanish, self.english, self.social, self.science])
        return total / 4

def ask_notes(subject):
        while True:
            try:
                notes = int(input(f"Enter the notes for {subject} (0-100): "))
                if 0 <= notes <= 100:
                    return notes
                print("Please enter a valid number between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
def add_student(student_list):
        name = input("Enter the student's name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        if not name.replace(" ", "").isalpha():
            print("Name must contain only letters and spaces.")
            return
        section = input("Enter the student's section: ").strip()
        if not section:
            print("Section cannot be empty.")
            return
        
        spanish = ask_notes("Spanish")
        english = ask_notes("English")
        social = ask_notes("Social")
        science = ask_notes("Science")

        new_student = Student(name, section, spanish, english, social, science)
        student_list.append(new_student)
        print(f"\nStudent {name} added successfully.")
        
def view_students(student_list):
        if not student_list:
            print("No students to display.")
            return
        
        for student in student_list:
            print("-------------------------------")
            print(f"Name: {student.name}")
            print(f"Section: {student.section}")
            print(f"Spanish: {student.spanish}")
            print(f"English: {student.english}")
            print(f"Social: {student.social}")
            print(f"Science: {student.science}")
            print(f"Average: {student.average():.2f}")
            print("-------------------------------")
            
def top_3_students(student_list):
        if not student_list:
            print("No students to evaluate.")
            return
        
        sorted_students = sorted(student_list, key=lambda s: s.average(), reverse=True)
        top_students = sorted_students[:3]
        
        print("\nTop 3 Students:")
        for student in top_students:
            print(f"{student.name} - Average: {student.average():.2f}")
            
def general_average(student_list):
        if not student_list:
            print("No students to evaluate.")
            return
        
        total_average = sum(student.average() for student in student_list) / len(student_list)
        print(f"\nGeneral Average: {total_average:.2f}")