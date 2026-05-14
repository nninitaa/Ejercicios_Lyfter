from actions import (
    ask_notes,
    add_student,
    view_students,
    top_3,
    general_average,
)

import data

def show_menu():
    while True:
        print("\nMenu:")
        print("1. Ask for student notes")
        print("2. Add a student")
        print("3. View students")
        print("4. Top 3 students")
        print("5. General average")
        print("6. Export to CSV")
        print("7. Import from CSV")
        print("8. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            subject = input("Enter the subject: ")
            ask_notes(subject)
        elif choice == '2':
            add_student()
        elif choice == '3':
            view_students()
        elif choice == '4':
            top_3()
        elif choice == '5':
            general_average()
        elif choice == '6':
            data.export_csv()
        elif choice == '7':
            data.import_csv()
        elif choice == '8':
            print("Exiting the program...")
            break
        else:
            print("Invalid option, please try again.")