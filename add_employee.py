
def add_employee(employees_data: list, employees_ID: int):
    
    first_name = input("Enter employee's first name: ")
    last_name = input("Enter employee's last name: ")
    dob = input("Enter employee's date of birth (YYYY-MM-DD): ")
    department = input("Enter employee's department: ")
 
    while True:
        try:
            salary = float(input("Enter employee's salary: "))
            break
        except ValueError:
            print("Invalid salary input. Please enter a valid number.")
    
  
    new_employee = {
        'ID': employees_ID,
        'first_name': first_name,
        'last_name': last_name,
        'dob': dob,
        'department': department,
        'salary': salary
    }
    

    employees_data.append(new_employee)
    print("You successfully added employee")


if __name__ == "__main__":
    
    employees = []  
    employee_id_counter = 1  
    
   
    add_employee(employees, employee_id_counter)

