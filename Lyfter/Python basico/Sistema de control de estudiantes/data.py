import csv

def export_students(students):
    with open('students.csv', mode='w', newline='') as archive:
        writer = csv.writer(archive)
        writer.writerow([
            'Name', 
            'Section', 
            'Spanish', 
            'English', 
            'Social Studies',
            'Science'
            ])
        
        for student in students:
            writer.writerow([
                student['name'],
                student['section'],
                student['spanish'],
                student['english'],
                student['social_studies'],
                student['science']
            ])
    print("Students exported to students.csv successfully.")

students = []
try:
    with open('students.csv', mode='r') as archive:
        reader = csv.DictReader(archive)    
        for row in reader:
            student = {
                'name': row['Name'],
                'section': row['Section'],
                'spanish': float(row['Spanish']),
                'english': float(row['English']),
                'social_studies': float(row['Social Studies']),
                'science': float(row['Science'])
            }

            students.append(student)
    print("Students imported from students.csv successfully.")
except FileNotFoundError:
    print("No existing students.csv file found. Starting with an empty student list.")

