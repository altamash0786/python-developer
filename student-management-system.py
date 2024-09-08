#student management system application
student_data = {}


while True:
    
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Send Messages")
    print("6. Exit")

    
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        email = input("Enter student email: ")
        
        student_data[student_id] = {
            "name": name,
            "age": age if age else "N/A",
            "email": email if email else "N/A"
        }
        print(f"Student with ID {student_id} added.")

    elif choice == '2':
        
        student_id = int(input("Enter student ID to update: "))
        if student_id in student_data:
            name = input("Enter new student name (press Enter to keep current): ")
            age = input("Enter new student age (press Enter to keep current): ")
            email = input("Enter new student email (press Enter to keep current): ")
            
            if name:
                student_data[student_id]["name"] = name
            if age:
                student_data[student_id]["age"] = age
            if email:
                student_data[student_id]["email"] = email
            
            print(f"Student with ID {student_id} updated.")
        else:
            print(f"Student with ID {student_id} does not exist.")

    elif choice == '3':
        
        student_id = int(input("Enter student ID to delete: "))
        if student_id in student_data:
            del student_data[student_id]
            print(f"Student with ID {student_id} deleted.")
        else:
            print(f"Student with ID {student_id} does not exist.")

    elif choice == '4':
        
        print("\nStudent Details:")
        for student_id, details in student_data.items():
            name = details["name"]
            age = details.get("age", "N/A")
            email = details.get("email", "N/A")
            print(f"ID: {student_id}, Name: {name}, Age: {age}, Email: {email}")

    elif choice == '5':
      
        for student_id in student_data:
            print(f"Message sent to: {student_id}")

    elif choice == '6':
        
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 6.")