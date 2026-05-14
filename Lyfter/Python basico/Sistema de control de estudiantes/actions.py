students = []

def ask_notes(subject):
    while True:
        try:
            note = float(input(f"Enter the note for {subject} (0-100): "))
            if 0 <= note <= 100:
                return note
            else:
                print("Note must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_student():
    name = input("Enter the student's name: ")
    section = input("Enter the student's section: ")
    spanish_note = ask_notes("Spanish")
    english_note = ask_notes("English")
    social_studies = ask_notes("Social Studies")
    science_note = ask_notes("Science")

    section = input("Enter the student's section: ")
    student = {
        "name": name,
        "section": section,
        "spanish": spanish_note,
        "english": english_note,
        "social_studies": social_studies,
        "science": science_note
    }
    students.append(student)
    print(f"Student {name} added successfully.")

def view_students():
    if len(students) == 0:
        print("No students to display.")
        return
    
    for student in students:
        print("-------------------------")
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish: {student['spanish']}")
        print(f"English: {student['english']}")
        print(f"Social Studies: {student['social_studies']}")
        print(f"Science: {student['science']}")
        print("-------------------------")

def general_average():
    if len(students) == 0:
        print("No students to calculate average.")
        return
    
    total_average = 0
    for student in students:
        student_average = (student['spanish'] + student['english'] + student['social_studies'] + student['science']) / 4
        total_average += student_average
    
    general_avg = total_average / len(students)
    print(f"The general average of all students is: {general_avg:.2f}")

def top_3():
    if len(students) == 0:
        print("No students to determine top 3.")
        return
    
    sorted_students = sorted(
        students,
        key=lambda x: (x['spanish'] + x['english'] + x['social_studies'] + x['science']) / 4,
        reverse=True
    )
    
    print("Top 3 students:")
    position = 1
    for i in range(min(3, len(sorted_students))):
        average = (sorted_students[i]['spanish'] + sorted_students[i]['english'] + sorted_students[i]['social_studies'] + sorted_students[i]['science']) / 4
        print(f"{position}. {sorted_students[i]['name']} with an average of {average:.2f}")
        position += 1