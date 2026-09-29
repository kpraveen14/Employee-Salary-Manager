employee=[]

while True:
    print("---Employee Salary Manager---")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Update employee salary")
    print("4. Delete Employee")
    print("5. Exit")
    
    choice = int(input("Enter the choice: "))
    
    # Add Employee
    if choice ==1:
        name = input("Enter employee name: ")
        salary = int(input("Enter employee salary: "))
       
        print(f" {name} added succesfully")
        
    #View Employee    
    elif choice ==2:
        new_name = input("Enter the name of the employee: ")
        if new_name != name:
            print("No employee found")
        
            
        else:   
            print(f"Employee name : {name} and old_salary :{salary} and updated_salary: {new_salary}" )
    #Update employee salary   
    elif choice ==3:
        check_name = input("Enter the name of the employee: ")
        if check_name != name:
            print("Employee not found")
        else:
            new_salary = int(input("Enter salary: "))
            print(f"Salary updated to {new_salary}")
        
    #Delete Employee   
    elif choice ==4:
        if not employee:
            print("No employee found")
        else:
            print(f"Employee {name} delete successfully")
        
    #Exit   
    elif choice ==5:
        print("Exiting the program")
        break
    
    else:
        print("Invalid input you put")
        
    