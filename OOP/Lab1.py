# Initializing the lists
firstnameList = []
lastnameList = []
addressList =[]
numberList = []

# Add Contact Function for the program
# use .upper() to convert the user's input as upper case letters.
def add_Contact():
    print("Enter New Contact Information")
    firstnameData = input("First Name: ").upper() 
    lastnameData = input("Last Name: ").upper()
    addressData = input("Address: ").upper()
    numberData = input("Contact Number: ").upper()

    # Setting the limit for the lists (50)
    # We use ".append" to insert the new contact to the list.
    if len(firstnameList) < 50:
        firstnameList.append(firstnameData) 
    else:
        print ("You have reached the maximum number of contacts.")
        
    if len(lastnameList) < 50:
        lastnameList.append(lastnameData)
    else:
        print ("You have reached the maximum number of contacts.")
        
    if len(addressList) < 50:
        addressList.append(addressData)
    else:
         print ("You have reached the maximum number of contacts.")
         
    if len(numberList) <50:
        numberList.append(numberData)
    # This will be the output if the limit of 50 contacts is reached.
    else:
        print ("You have reached the maximum number of contacts.")
        print (firstnameList)

# Edit Contact Function for the program
def edit_Contact():
    # Getting the user's number input to be used as index in edit_Data variable.
    edit_Data= int(input("Enter the number of the contact you want to edit: ")) 
    
    # Checking if the input is within the range of the lists.
    if edit_Data  < len(firstnameList) or edit_Data < len(lastnameList) or edit_Data < len(addressList) or edit_Data < len(numberList):
        
        # Editing the contact list based on the user's input index.
        print(firstnameList[edit_Data])
        firstnameList[edit_Data] = input("First Name: ").upper()
        
        print(lastnameList[edit_Data])
        lastnameList[edit_Data] = input("Last Name: ").upper()
        
        print(addressList[edit_Data])
        addressList[edit_Data] = input("Address: ").upper()
        
        print(numberList[edit_Data])
        numberList[edit_Data] = input("Contact Number: ").upper()
        
    else:
        print("The value you entered is out of index range. Try again.")

# Delete Contact Function for the program.
def delete_Contact():
    # Getting the user's input to be used as index in delete_Data.
    delete_Data = int(input("What index would you like to delete?: "))
    
    # Checking if the input is within the lists' range.
    if delete_Data  < len(firstnameList) or delete_Data < len(lastnameList) or delete_Data < len(addressList) or delete_Data < len(numberList):
        
        # Using ".pop" to delete the data based on the users input.
        firstnameList.pop(delete_Data)
        lastnameList.pop(delete_Data)
        addressList.pop(delete_Data)
        numberList.pop(delete_Data)
        print(f"Entry '{delete_Data}' has been successfully removed.")
        
    else:
        print("The value you entered is out of index range. Try again.")
        
# View Contact Function for the program.
def view_Contact():
    
# Calling the lists from global to be able to use it inside the for loop.
    global firstnameList, lastnameList, addressList, numberList
    
    for i,j,k,l in zip (firstnameList, lastnameList, addressList, numberList):
        print(i,j,k,l)
    
# Search Contact Function for the program.
def search_Contact():
    print("What value would you like to search?")
    print("a. First Name \nb. Last Name \nc, Address \nd Contact Number")
    
    search_Select = input(" Enter the value you would like to search:")

    # Searching based on the user's input information.
    # First name search.
    if search_Select == 'a':
        search_Data =  input("Search:").upper() #converting the user's inout to uppercase for consistency.
        
        if search_Data in firstnameList:
            index = firstnameList.index(search_Data)
            print(index, firstnameList[index], lastnameList[index],addressList[index], numberList[index])
        else:
            print(f"{search_Data} is not in the list.")

    # Last name search.
    elif search_Select == 'b':
        search_Data =  input("Search:").upper()
        
        if search_Data in lastnameList:
            index = lastnameList.index(search_Data)
            print(index, firstnameList[index], lastnameList[index],addressList[index], numberList[index])
        else:
            print(f"{search_Data} is not in the list.")
        
    # Address search.
    elif search_Select == 'c':
        search_Data =  input("Search:").upper()
        if search_Data in addressList:
            index = addressList.index(search_Data)
            print(index, firstnameList[index], lastnameList[index],addressList[index], numberList[index])
        else:
            print(f"{search_Data} is not in the list.")
            
    # Contact number search.
    elif search_Select == 'd':
        search_Data =  input("Search:").upper()
        if search_Data in numberList:
            index = numberList.index(search_Data)
            print(index, firstnameList[index], lastnameList[index],addressList[index], numberList[index])
        else:
            print(f"{search_Data} is not in the list.")
    
    else:
        print("Invalid Value. Try Again.")
        
# Main Menu function of the program
def main_Menu():
    
    # Getting the user input for the action selection
    while True:
        print("-----Adress Book-----")
        print("What would you like to do?")
        print("1. Add Contact \n2. Edit Contact \n3. Delete Contact \n4. View Contacts \n5. Search Address Book \n6. Exit")
        select = input("Choose an option:")
        if select == '1':
            add_Contact()
        elif select == '2':
            edit_Contact()
        elif select == '3':
            delete_Contact()
        elif select == '4':
            view_Contact()
        elif select == '5':
            search_Contact()
        elif select == '6':
            break
        else:
            print("Incorrect value. Try again.")
            
# Calling the main_Menu Function to launch the program
main_Menu()