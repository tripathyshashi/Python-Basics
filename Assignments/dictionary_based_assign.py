# Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ)
# depending on the operation they want to perform on the dictionary:
# A
# 1. - Add a student
# B
# 2. - Update marks
# 3. C
# - Search for a student
# 4. D
# - Display all students and marks

students = {}
while True:
    print("\nA - Add a student")
    print("B - Update CGPA ")
    print("C - Search for a student")
    print("D - Display all students and Marks")
    print("E - Exit")

    choice = input("\nEnter your choice (A/B/C/D/E) : ").upper()
    if choice == "A":
        name = input("Enter the name of student : ")
        if name in students:
            print("Student already exists.")
        else:
            cgpa = float(input("Enter the CGPA : "))
            students[name] = cgpa
            print("Student added successfully.")

    elif choice == "B":
        name = input("Enter the student name to update : ")
        if name in students:
            cgpa = float(input("Enter the new CGPA : "))
            students[name] = cgpa
            print("CGPA updated successfully.")
        else:
            print("Student not found")

    elif choice == "C":
        name = input("Enter a student name to search : ")
        if name in students:
            print(f"{name} scored {students[name]} CGPA.")
        else:
            print("Student not found.")
    elif choice == "D":
        if len(students) == 0:
            print("No student records available.")
        else:
            print("\nStudent Records")
            print("------------------------")
            for name, cgpa in students.items():
                print(f"{name} : {cgpa}")

    elif choice == "E":
        print("Program terminated.")
        break

    else:
        print("Invalid choice! Please enter A, B, C, D, or E.")
