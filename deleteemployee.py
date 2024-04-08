def delete_emp(employees):
   
    
    employee_id = input("Enter the ID of the employee to delete: ")
    
  
    for employee in employees:
        if employee.get('id') == employee_id:
            employees.remove(employee)
            print("successfully employee delete")
            return

    print("Employee with ID '{}' not found.".format(employee_id))


delete_emp(employees)
