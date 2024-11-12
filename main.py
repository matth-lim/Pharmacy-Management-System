# MATTHEW LIM JIAN LE

from os import system

#Initiate the main menu program
def start():
    print("\t***** Online Pharmacy Management System (OPMS) *****\n")
    print("1. Admin")
    print("2. New Customer")
    print("3. Registered Customer")
    print("4. Exit")
    #User can input their choice based on what they choose
    choice = input("Choice: ")
    #Will call certain function based on the choice
    if choice == "1":
        system('cls')
        admin_menu()
    elif choice == "2":
        system('cls')
        new_customer_menu()
    elif choice == "3":
        system('cls')
        registered_customer_menu()
    elif choice == "4":
        exit()
    else:
        #When the user type an invalid choice, call back the function
        print("Invalid choice")
        start()

#Initiate the admin login menu
def admin_menu():
    print("\t***** Admin *****\n")
    print("1. Login")
    print("2. Return to menu")
    print("3. Exit")
    #User can input their choice based on what they choose
    choice = input("Choice: ")
    #Will call certain function based on their choice
    if choice == "1":
        system('cls')
        admin_login()
    elif choice == "2":
        system('cls')
        start()
    elif choice == "3":
        exit()
    else:
        #When the user type an invalid choice, call back the function
        print("Invalid choice")
        admin_menu()

#Admin login system
def admin_login():
    admin = open("admin.txt", "r")
    access = False
    #Ask the user for username and password to login as admin
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    #Check whether the input password and username match or not
    for x in admin:
        db_username, db_password = x.split(",")
        db_password = db_password.strip()
        if username == db_username and password == db_password:
            access = True
            break
    admin.close()
    #If the password and username match, gets access to the admin menu
    if access:
        system('cls')
        admin_access()
    #If the password and username don't match, calls the admin login menu function
    else:
        input("Username or password is incorrect! Press Enter to return to menu.....")
        system('cls')
        admin_menu()

#Admin main menu after access is granted
def admin_access():
    print("\t***** Admin system menu *****\n")
    print("1. Register new admin")
    print("2. Upload Medicine detail")
    print("3. View all uploaded Medicines")
    print("4. Update Medicine information")
    print("5. Delete Medicine information")
    print("6. Search specific Medicine detail")
    print("7. View all orders of customers")
    print("8. Search order of specific customer")
    print("9. Exit")
    #Admin can input their choice based on what they choose
    choice = input("Choice: ")
    #Will call certain function based on their choice
    if choice == "1":
        system('cls')
        admin_register()
    elif choice == "2":
        system('cls')
        admin_upload()
    elif choice == "3":
        system('cls')
        admin_view_med()
    elif choice == "4":
        system('cls')
        admin_update()
    elif choice == "5":
        system('cls')
        admin_delete()
    elif choice == "6":
        system('cls')
        admin_search_med()
    elif choice == "7":
        system('cls')
        admin_view_order()
    elif choice == "8":
        system('cls')
        admin_search_order()
    elif choice == "9":
        exit()
    else:
        #When the admin type an invalid choice, call back the function
        print("Invalid choice")
        admin_access()

#Register a new admin
def admin_register():
    admin = open("admin.txt", "a")
    print("\t***** Register New Admin *****\n")
    #Input the new admin username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    #Write the new username and password in admin.txt
    admin.write(username + ", " + password + "\n")
    admin.close()
    #After completed registering press enter to go back to admin menu
    input("Admin registered successfully! Press Enter to return to admin menu.....")
    system('cls')
    admin_access()

#Upload a new medicine
def admin_upload():
    medicine = open("medicine.txt", "a")
    print("\t***** Upload Medicine Detail *****\n")
    #Input the new medicine ID, name, expiry date and price
    med_ID = input("Enter Medicine ID: ")
    med_name = input("Enter Medicine name: ")
    exp_date = input("Enter Medicine's expiry date (dd/mm/yyyy): ")
    price = input("Enter Medicine's price: ")
    #Write the new medicine information in medicine.txt
    medicine.write(med_ID + ", " + med_name + ", " + exp_date + ", " + price + "\n")
    medicine.close()
    #After completed uploading press enter to go back to admin menu
    input("Medicine uploaded successfully! Press Enter to return to admin menu.....")
    system('cls')
    admin_access()

#View all the medicines
def admin_view_med():
    medicine = open("medicine.txt", "r")
    print("| Medicine ID | Medicine name | Expiry date | Price |")
    #Loop through every single line in medicine.txt
    for x in medicine:
        ID,name,date,price = x.split(",")
        name = name.strip()
        date = date.strip()
        price = price.strip()
        #Print every single line in medicine.txt
        print(f"| {ID} | {name} | {date} | {price} |")
    medicine.close()
    #Wait for the user to press enter then go back to admin menu
    input("Press Enter to return to menu.....")
    system('cls')
    admin_access()

#Update a specific medicine
def admin_update():
    print("\t***** Update medicine detail *****\n")
    medicine = open("medicine.txt", "r")
    print("| Medicine ID | Medicine name | Expiry date | Price |")
    #Loop through every single line in medicine.txt
    for x in medicine:
        ID,name,date,price = x.split(",")
        name = name.strip()
        date = date.strip()
        price = price.strip()
        #Print every single line in medicine.txt
        print(f"| {ID} | {name} | {date} | {price} |")
    medicine.close()
    line = 0
    valid = False
    #Input the medicine ID of the medicine to update
    med_ID = input("Enter the medicine ID that you want to update: ")
    medicine = open("medicine.txt", "r")
    #Check whether the medicine exist in medicine.txt
    for x in medicine:
        entry = x.split(",")
        if entry[0] == med_ID:
            valid = True
            break
    medicine.close()
    #If medicine does not exist in medicine.txt, press enter to return to admin menu
    if not valid:
        input("Invalid medicine! Press Enter to return to menu.....")
        system('cls')
    else:
        #If the medicine exist get input of new medicine name, expiry date and price
        med_name = input("Enter the new medicine name: ")
        med_exp_date = input("Enter the new medicine expiry date: ")
        med_price = input("Enter the new medicine price: ")
        medicine = open("medicine.txt", "r")
        #Get the line number of the medicine
        for x in medicine:
            entry = x.split(",")
            if med_ID == entry[0]:
                break
            line += 1
        medicine.close()
        #Read all the lines in medicine.txt
        medicine = open("medicine.txt", "r")
        data = medicine.readlines()
        medicine.close()
        #Replace the line with the new string in medicine.txt
        data[line] = f"{med_ID}, {med_name}, {med_exp_date}, {med_price}\n"
        medicine = open("medicine.txt", "w")
        medicine.writelines(data)
        medicine.close()
        #After medicine updated, press Enter to return to admin menu
        input("Medicine updated successfully! Press Enter to return to menu.....")
        system('cls')
    admin_access()

#Delete a specific medicine
def admin_delete():
    print("\t***** Delete medicine detail *****\n")
    medicine = open("medicine.txt", "r")
    print("| Medicine ID | Medicine name | Expiry date | Price |")
    #Loop through every single line in medicine.txt
    for x in medicine:
        ID,name,date,price = x.split(",")
        name = name.strip()
        date = date.strip()
        price = price.strip()
        #Print every single line in medicine.txt
        print(f"| {ID} | {name} | {date} | {price} |")
    medicine.close()
    #Input the medicine ID to delete
    medicine_ID = input("Enter the medicine ID you want to delete: ")
    valid = False
    medicine = open("medicine.txt", "r")
    #Check whether the medicine ID exist in medicine.txt
    for x in medicine:
        entry = x.split(",")
        if entry[0] == medicine_ID:
            valid = True
            break
    medicine.close()
    if not valid:
        #If not valid press enter to return to admin menu
        input("Invalid medicine! Press Enter to return to menu.....")
        system('cls')
    else:
        #If valid search for the line of medicine to delete
        medicine = open("medicine.txt", "r")
        delete_line = ""
        for x in medicine:
            entry = x.split(",")
            if entry[0] == medicine_ID:
                delete_line = x
                break
        medicine.close()
        #Read all lines
        medicine = open("medicine.txt", "r")
        lines = medicine.readlines()
        medicine.close()
        #Rewrite everything except for the line to delete
        medicine = open("medicine.txt", "w")
        for line in lines:
            if line.strip("\n") != delete_line[:-1]:
                medicine.write(line)
        medicine.close()
        #After is medicine deleted, press Enter to return to admin menu
        input("Medicine deleted successfully! Press Enter to return to menu.....")
        system('cls')
    admin_access()

#Search for a specific medicine
def admin_search_med():
    print("\t***** Search medicine detail *****\n")
    medicine = open("medicine.txt", "r")
    #Input the medicine ID to search
    med_ID = input("Enter medicine ID: ")
    valid = False
    #Check if the medicine exist
    for x in medicine:
        entry = x.split(",")
        #If it exist print the medicine detail
        if med_ID == entry[0]:
            valid = True
            print(f"Medicine name: {entry[1]}")
            print(f"Medicine expiry date: {entry[2]}")
            print(f"Medicine price: {entry[3]}")
    medicine.close()
    #If it does not exist press enter to return to admin menu
    if not valid:
        input("Medicine not found! Press Enter to return to menu.....")
    #After viewing press enter to return to admin menu
    else:
        input("Press Enter to return to menu.....")
    system('cls')
    admin_access()
            
#View all orders of customer
def admin_view_order():
    print("\t***** View all orders of customer *****\n")
    customer = open("customer.txt", "r")
    print("| User ID | Medicines |")
    #Loop through every line in customer.txt
    for x in customer:
        medicines = []
        entry = x.split(",")
        #Loop through and print all the medicine for each customer in customer.txt
        for y in range(8, len(entry)):
            medicines.append(entry[y].strip())
        user_ID = entry[6].strip()
        print(f"| {user_ID} | {medicines} |")
    customer.close()
    #After done viewing press enter to return to admin menu
    input("Press Enter to return to menu.....")
    system('cls')
    admin_access()

#View the order of a specific customer
def admin_search_order():
    print("\t***** View orders of a specific customer *****\n")
    #Input the user ID of the customer to search his order
    user_ID = input("Enter a customer's user ID: ")
    valid = False
    orders = []
    customer = open("customer.txt", "r")
    #Check if the user ID is valid or not
    for x in customer:
        entry = x.split(",")
        db_user_ID = entry[6].strip()
        if user_ID == db_user_ID:
            #Print out every medicine the customer have if the user ID exist
            for y in range(8, len(entry)):
                orders.append(entry[y].strip())
            print(f"{user_ID} ordered: {orders}")
            valid = True
            break
    customer.close()
    #If user ID is not valid press enter to return to admin menu
    if not valid:
        input("User ID is invalid! Press Enter to return to menu.....")
        system('cls')
    #After done viewing press enter to return to admin menu
    else:
        input("Press Enter to return to menu.....")
        system('cls')
    admin_access()

#Initiate the new customer menu program
def new_customer_menu():
    print("\t***** New Customer *****\n")
    print("1. View Medicine detail")
    print("2. Registration")
    print("3. Exit")
    #User can input their choice based on what they choose
    choice = input("Choice: ")
    #Will call certain function based on the choice
    if choice == "1":
        system('cls')
        nc_view_med()
    elif choice == "2":
        system('cls')
        registration()
    elif choice == "3":
        exit()
    else:
        #When the user type an invalid choice, call back the function
        print("Invalid choice")
        new_customer_menu()

#View all medicines for new customers
def nc_view_med():
    medicine = open("medicine.txt", "r")
    print("| Medicine ID | Medicine name | Expiry date | Price |")
    #Loop through every single line in medicine.txt
    for x in medicine:
        ID,name,date,price = x.split(",")
        name = name.strip()
        date = date.strip()
        price = price.strip()
        #Print every single line in medicine.txt
        print(f"| {ID} | {name} | {date} | {price} |")
    medicine.close()
    #Wait for the user to press enter then go back to new customer menu
    input("Press Enter to return to menu.....")
    system('cls')
    new_customer_menu()

#Registration for new customers
def registration():
    customer = open("customer.txt", "r")
    #Get all exisiting user ID
    used_user_ID = []
    for x in customer:
        entry = x.split(",")
        used_user_ID.append(entry[6].strip())
    customer.close()
    print("\t***** Registration *****\n")
    #Input all the personal information
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    email = input("Enter your email: ")
    contact_num = input("Enter your contact number: ")
    gender = input("Enter your gender (M/F): ")
    date_of_birth = input("Enter your date of birth (dd/mm/yyyy): ")
    user_id = input("Enter your username: ")
    #If the user ID already exist then ask for another user ID
    while user_id in used_user_ID:
        print("User ID is used! Please try another one")
        user_id = input("Enter your username: ")
    password = input("Enter your password: ")
    rewrite_password = input("Retype password: ")
    #If the password and retype password does not match tn ask to retype the password
    while rewrite_password != password:
        print("Passwords do not match!")
        password = input("Enter your password: ")
        rewrite_password = input("Retype password: ")
    #Append the new customer into customer.txt
    customer = open("customer.txt", "a")
    customer.write(f"{name}, {address}, {email}, {contact_num}, {gender}, {date_of_birth}, {user_id}, {password}\n")
    customer.close()
    #After done registering press enter to return to menu
    input("Registered successfully! Press Enter to return to menu.....")
    system('cls')
    start()

#Initiate the registered customer program
def registered_customer_menu():
    print("\t***** Registered Customer *****\n")
    print("1. Login")
    print("2. Return to menu")
    print("3. Exit")
    #User can input their choice based on what they choose
    choice = input("Choice: ")
    #Will call certain function based on the choice
    if choice == "1":
        system('cls')
        registered_customer_login()
    elif choice == "2":
        system('cls')
        start()
    elif choice == "3":
        exit()
    else:
        #When the user type an invalid choice, call back the function
        print("Invalid choice")
        registered_customer_menu()

#Login as a customer to gain access to the customer system
def registered_customer_login():
    customer = open("customer.txt", "r")
    access = False
    #Ask the user for user ID and password
    user_ID = input("Enter your user ID: ")
    password = input("Enter your password: ")
    #Check if the password and user ID match or not
    for x in customer:
        entry = x.split(",")
        db_user_ID = entry[6].strip()
        db_password = entry[7].strip()
        if user_ID == db_user_ID and password == db_password:
            access = True
            break
    customer.close()
    #If password and user ID match then gain access to the customer system
    if access:
        system('cls')
        registered_customer_access(user_ID)
    #If the password and user ID do not match press enter to return to customer login menu
    else:
        input("Username or password is incorrect! Press Enter to return to menu.....")
        system('cls')
        registered_customer_menu()

#Registered customer main menu after the user has logged in
def registered_customer_access(user_ID):
    print("\t***** Registered Customer system menu *****\n")
    print("1. View all Medicines detail")
    print("2. Place order of medicines")
    print("3. Do payment")
    print("4. View own order")
    print("5. View personal information")
    print("6. Exit")
    #User can input their choice based on what they choose
    choice = input("Choice: ")
    #Will call certain function based on the choice
    if choice == "1":
        system('cls')
        registered_customer_view_med(user_ID)
    elif choice == "2":
        system('cls')
        registered_customer_place_order(user_ID)
    elif choice == "3":
        system('cls')
        registered_customer_payment(user_ID)
    elif choice == "4":
        system('cls')
        registered_customer_view_order(user_ID)
    elif choice == "5":
        system('cls')
        registered_customer_view_info(user_ID)
    elif choice == "6":
        exit()
    else:
        #When the user type an invalid choice, call back the function
        print("Invalid choice")
        registered_customer_access(user_ID)

#Registered customer to view all medicine
def registered_customer_view_med(user_ID):
    medicine = open("medicine.txt", "r")
    print("| Medicine ID | Medicine name | Expiry date | Price |")
    #Print every medicine in medicine.txt
    for x in medicine:
        ID,name,date,price = x.split(",")
        name = name.strip()
        date = date.strip()
        price = price.strip()
        print(f"| {ID} | {name} | {date} | {price} |")
    medicine.close()
    #After done viewing press enter to return to new customer menu
    input("Press Enter to return to menu.....")
    system('cls')
    registered_customer_access(user_ID)

#Registered customer to place order
def registered_customer_place_order(user_ID):
    print(f"\t*****Place order*****\n")
    #Input the name of the medicine to order
    medicine_name = input("Enter the medicine name to place order: ")
    access = False
    medicine = open("medicine.txt", "r")
    #Check if the medicine exist or not in medicine.txt
    for x in medicine:
        entry = x.split(",")
        medicine_name_db = entry[1].strip()
        if medicine_name_db.lower() == medicine_name.lower():
            access = True
            break
    medicine.close()
    #If it does not exist press enter to return to registered customer menu
    if not access:
        input("Invalid medicine! Press Enter to return to menu.....")
        system('cls')
    #If it exists then add the order into customer.txt
    else:
        customer = open("customer.txt", "r")
        line = 0
        #Get the line of the customer
        for x in customer:
            entry = x.split(",")
            db_user_ID = entry[6].strip()
            if user_ID == db_user_ID:
                break
            line += 1
        customer.close()
        #Read all the lines and make the new line with the new order
        customer = open("customer.txt", "r")
        data = customer.readlines()
        new_line = data[line][:-1] + ", " + medicine_name + "\n"
        data[line] = new_line
        customer.close()
        #Write the new line into customer.txt
        customer = open("customer.txt", "w")
        customer.writelines(data)
        customer.close()
        input("Thanks for ordering. Press Enter to return to menu.....")
        system('cls')
    registered_customer_access(user_ID)

#To calculate the total price for registered customer order
def cal_price_registered_customer(order_list):
    #Find the total cost of all the medicines in the list
    price = 0
    medicine = open("medicine.txt", "r")
    for x in medicine:
        entry = x.split(",")
        if entry[1].strip().lower() in order_list:
            price += float(entry[3].strip()[1:])
    medicine.close()
    return price
    
#Registered customer to make payment
def registered_customer_payment(user_ID):
    print(f"\t*****Make payment*****\n")
    have_order = True
    customer_order = []
    line = 0
    #Get the line of the customer and check if the customer have at least 1 order or not
    customer = open("customer.txt", "r")
    for x in customer:
        entry = x.split(",")
        db_user_ID = entry[6].strip()
        if user_ID == db_user_ID:
            if len(entry) == 8:
                have_order = False
            break
        line += 1
    customer.close()
    #If the customer have at least 1 order then do payment
    if have_order:
        #Get all the orders and store it in a list
        customer = open("customer.txt", "r")
        for x in customer:
            entry = x.split(",")
            db_user_ID = entry[6].strip()
            if user_ID == db_user_ID:
                for y in range(8, len(entry)):
                    customer_order.append(entry[y].strip().lower())
        customer.close()
        price = cal_price_registered_customer(customer_order)
        #Print the total price of the medicines
        print(f"Total price = ${price}")
        #Get customer credit card information
        credit_card_number = input("Enter your credit card number: ")
        card_expiry_date = input("Enter your credit card expiry date (mm/yy): ")
        CCV = input("Enter your card security number: ")
        #Remove all orders of customer
        customer = open("customer.txt", "r")
        data = customer.readlines()
        entry = data[line].split(",")
        new_line = f"{entry[0]},{entry[1]},{entry[2]},{entry[3]},{entry[4]},{entry[5]},{entry[6]},{entry[7]}\n"
        data[line] = new_line
        customer.close()
        customer = open("customer.txt", "w")
        customer.writelines(data)
        customer.close()
        input("Transaction is successful! Press Enter to return to menu.....")
        system('cls')
    #else ask the user to place order before making payment
    else:
        #Press Enter to return to registered customer menu
        input("Please place order before making payment. Press Enter to return to menu.....")
        system('cls')
    registered_customer_access(user_ID)

#registered customer to view their own order
def registered_customer_view_order(user_ID):
    print(f"\t*****{user_ID}'s orders*****\n")
    customer = open("customer.txt", "r")
    count = 1
    #Loop to the line of the customer
    for x in customer:
        entry = x.split(",")
        db_user_ID = entry[6].strip()
        if user_ID == db_user_ID:
            #Print every medicine the customer order
            for y in range(8, len(entry)):
                print(f"Medicine {count}: {entry[y]}")
                count += 1
    customer.close()
    #After done viewing press enter to return to registered customer menu
    input("Press Enter to return to menu.....")
    system('cls')
    registered_customer_access(user_ID)

#registred customer to view their own personal information
def registered_customer_view_info(user_ID):
    print(f"\t*****{user_ID}'s personal information*****\n")
    customer = open("customer.txt", "r")
    #Print out the specific customer's order
    for x in customer:
        entry = x.split(",")
        db_user_ID = entry[6].strip()
        if user_ID == db_user_ID:
            print(f"Name: {entry[0]}")
            print(f"Address: {entry[1]}")
            print(f"Email ID: {entry[2]}")
            print(f"Contact Number: {entry[3]}")
            print(f"Gender: {entry[4]}")
            print(f"Date of birth: {entry[5]}")
            print(f"User_ID: {entry[6]}")
            break
    customer.close()
    #After done viewing press enter to return to registered customer menu
    input("Press Enter to return to menu.....")
    system('cls')
    registered_customer_access(user_ID)

#Terminate the program
def exit():
    print("Program terminated successfully")

#Call start function to initiate the program
start()
