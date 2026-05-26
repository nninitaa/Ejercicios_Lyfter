import csv
from actions import Student

def export_students(students):
    with open('students.csv', mode='w', newline='') as archive:
        writer = csv.writer(archive)
        writer.writerow([
            'Name', 
            'Section', 
            'Spanish', 
            'English', 
            'Social',
            'Science'
            ])
        
        for student in students:
            writer.writerow([
                student.name,
                student.section,
                student.spanish,
                student.english,
                student.social,
                student.science
            ])
    print("Students exported to students.csv successfully.")

def import_students(students):
    try:
        with open('students.csv', mode='r') as archive:
            reader = csv.DictReader(archive)
            for row in reader:
                student_object = Student(
                    name=row['Name'],
                    section=row['Section'],
                    spanish=int(row['Spanish']),
                    english=int(row['English']),
                    social=int(row['Social']),
                    science=int(row['Science'])
                )
                students.append(student_object)
        print("Students imported from students.csv successfully.")
    except FileNotFoundError:
        print("No students.csv file found. Please export students first.")