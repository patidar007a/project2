def delete_employee(employees):
   

    employee_id = input("Enter the ID of the employee to delete: ")
    
    for employee in employees:
        if employee.get('id') == employee_id:
            employees.remove(employee)
            print("Employee deleted successfully!")
            return
    
   
    print("Employee with ID '{}' not found.".format(employee_id))


delete_employee(employees)
