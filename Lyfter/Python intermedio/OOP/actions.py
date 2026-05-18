class Student:
    def __init__(self):
        self.students = []
    def ask_notes(self, subject):
        while True:
            try:
                notes = input(f"Please enter the notes for {subject} (0-100): ")
                if 0 <= int(notes) <= 100:
                    return f"The notes for {subject} are {notes}."
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                print("Invalid input. Please enter a number between 0 and 100.")
                
    def add_student(self, name):
        name = input("Please enter the student's name: ")
        if name.strip() == "":
            return "Name cannot be empty. Please enter a valid name."
        if not name.isalpha():
            return "Name must contain only letters. Please enter a valid name." 
        section = input("Please enter the student's section: ")
        if section.strip() == "":
            return "Section cannot be empty. Please enter a valid section."
        spanish_notes = self.ask_notes("Spanish")
        english_notes = self.ask_notes("English")
        social_notes = self.ask_notes("Social")
        science_notes = self.ask_notes("Science")
        
        student_info = {
            "name": name,
            "section": section,
            "spanish": spanish_notes,
            "english": english_notes,
            "social": social_notes,
            "science": science_notes
        }
        self.students.append(student_info)
        return f"Student added successfully: {name}"
    
    def view_students(self, students_list):
        if not self.students:
            return "No students to display."
        for student in self.students:
            print("-------------------------------")
            print(f"Name: {student['name']}")
            print(f"Section: {student['section']}")
            print(f"Spanish Notes: {student['spanish']}")
            print(f"English Notes: {student['english']}")
            print(f"Social Notes: {student['social']}")
            print(f"Science Notes: {student['science']}")
            print("-------------------------------")
            
        def calculate_average(self, student):
            total_notes = int(student['spanish']) + int(student['english']) + int(student['social']) + int(student['science'])
            average = total_notes / 4
            return f"The average notes for {student['name']} is {average:.2f}."
        if len(self.students) == 0:
            return "No students to calculate average."  
        def top_3_students(self):
            if len(self.students) == 0:
                return "No students to calculate top 3."
            sorted_students = sorted(self.students, key=lambda x: (int(x['spanish']) + int(x['english']) + int(x['social']) + int(x['science'])) / 4, reverse=True)
            print("Top 3 students based on average notes:")
            for i, student in enumerate(sorted_students[:3]):
                average = (int(student['spanish']) + int(student['english']) + int(student['social']) + int(student['science'])) / 4
                print(f"{i + 1}. {student['name']} - Average Notes: {average:.2f}")
                
student_manager = Student()
student_manager.ask_notes()
student_manager.add_student()
student_manager.view_students()
student_manager.top_3_students()