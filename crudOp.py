import os

def create_record(file_name):
    # Open the file in append mode to add new records
    with open(file_name, 'a') as file:
        # Ask the user to input the data (ID, Name, Department)
        student_id = input("Enter ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        record = "{}, {}, {}".format(student_id, name, department)
        # Write the record to the file
        file.write(record + '\n')

def read_record(file_name, option):
    with open(file_name, 'r') as file: # Opens the file in read mode to read lines
        records = file.readlines()
        if option == '2.1': #Displays all the record
            for record in records:
                print(record.strip())
        elif option == '2.2': #Displays record based on ID
            search_id = input("Enter ID to search: ")
            for record in records:
                if record.startswith(search_id):
                    print(record.strip())

def update_record(file_name):
    search_id = input("Enter ID to update: ")
    with open(file_name, 'r') as file:
        lines = file.readlines()
    with open(file_name, 'w') as file:
        for line in lines:
            if line.startswith(search_id):
                student_id, name, department = line.strip().split(',')
                new_name = input(f"Enter updated Name (Press Enter to keep '{name}'): ")
                new_department = input(f"Enter updated Department (Press Enter to keep '{department}'): ")
                # Update name if new_name is provided, else keep existing name
                if new_name:
                    name = new_name.strip()
                # Update department if new_department is provided, else keep existing department
                if new_department:
                    department = new_department.strip()
                # Write the updated record to the file
                file.write(f"{student_id},{name},{department}\n")
            else:
                # Write the unchanged record to the file
                file.write(line)

def delete_record(file_name):
    # Ask user for the ID of the record to be deleted
    search_id = input("Enter ID to delete: ")
    # Open the file in read mode to read existing records
    with open(file_name, 'r') as file:
        lines = file.readlines()  # Read all lines(records) from the file
    # Open the file in write mode to rewrite records without the deleted one
    with open(file_name, 'w') as file:
        # Loop through each line(record) in the file
        for line in lines:
            # If the line does not start with the search ID, keep it in the file
            if not line.startswith(search_id):
                file.write(line)

def main():
    file_name = 'records.txt'
    while True:
        os.system('clear')
        # Display menu options to the user
        print("\nMenu:")
        print("1. Create Record")
        print("2. Read Record")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        # Ask user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            create_record(file_name)
        elif choice == '2':
            # Ask user for the read option (show all or display based on ID)
            read_option = input("2.1: Show all data\n2.2: Display data based on ID\nEnter option: ")
            read_record(file_name, read_option)
            input("Please Press Enter to continue")
        elif choice == '3':
            update_record(file_name)
        elif choice == '4':
            delete_record(file_name)
        elif choice == '5':
            # Exit the program if user chooses to exit
            print("Exiting...")
            break
        else:
            # Display error message for invalid choices
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
