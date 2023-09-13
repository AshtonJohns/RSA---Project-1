#PLACEHOLDERS FOR TESTING - REVISE
def helloWorld1():
    print("Hello world1")
def helloWorld2():
    print("Hello world2")
def helloWorld3():
    print("Hello world3")
def helloWorld4():
    print("Hello world4")
def helloWorld5():
    print("Hello world5")
def helloWorld6():
    print("Hello world6")


print("RSA keys have been generated")
#GET KEYS HERE - REVISE

dict_of_options = {1:('Please select your user type','1. A public user','2. The owner of the keys','3. Exit program'),
                   2:('As a public user what would you like to do?','1. Send an encrypted message','2. Authenticate a digital signature','3. Exit'),
                   3:('As the owner of the keys what would you like to do?', '1. Decrypt a received message','2. Digitally sign a message','3. Show the keys','4. Generating a new set of the keys','5. Exit'),}

dict_of_operations = {'2a':helloWorld1,
                      '2b':helloWorld2,
                      '3a':helloWorld3,
                      '3b':helloWorld4,
                      '3c':helloWorld5,
                      '3d':helloWorld6}

#Start with key here
key = 1

#run while loop until cont = false
cont = True

while cont: 

    # Find printable options in dict_of_options
    if key in dict_of_options:

        #will store the options, and where a choice must be made on the option
        list_of_options = []

        #get the value from the dict_of_options without parenthese [()], quote ['], or comma [,]
        options_string = str(dict_of_options.get(key))
        options_string = options_string.replace("(","")
        options_string = options_string.replace(")","")
        options_string = options_string.replace("'","")

        #add these options to the list
        list_of_options = options_string.split(", ")

        #print the options where a choice must be made
        for seperated_list_of_options in list_of_options:
            if seperated_list_of_options.startswith(".",1):
                print("\t" + seperated_list_of_options)
            else:
                print(seperated_list_of_options)
        
        #user input corresponds to options to choose from
        option = input("\nEnter your choice: ")

        #main menu (start)
        if key == 1:
            if option == '1':
                key = 2
            elif option == '2':
                key = 3
            elif option == '3':
                # exit program
                cont = False
        #public user
        elif key == 2:
            if option == '1':
                key = '2a'
            elif option == '2':
                key = '2b'
            elif option == '3':
                key = 1
        #key owner 
        elif key == 3:
            if option == '1':
                key = '3a'
            elif option == '2':
                key = '3b'
            elif option == '3':
                key = '3c'
            elif option == '4':
                key = '3d'
            elif option == '5':
                key = 1
        #invalid choice
        else:
            #reset
            print("Wrong selection, back to menu\n")
            key = 1

    # Find associated option operations in dict_of_operations
    else:
        if key == '2a' or key == '2b':
            functn = dict_of_operations[key]
            functn()
            # go back to public user menu
            key = 2
        else:
            functn = dict_of_operations[key]
            functn()
            # go back to key owner menu
            key = 3

#Finished
print("\nBye for now!")




        


