'''------------------------------------------------------
                 Import Modules 
---------------------------------------------------------'''
import dna_tool as dna

'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''
print("\n==========================================")
print("DNA \"Analyzer\" and Patient Management Tool")
print("==========================================")

import dna_kernel

#print(dna_kernel.random_base())

#dna.initialize()

dna.display_menu()
while True:
    option = input("Command (Enter to exit): ")
    if option == "1":
        dna.display()
    elif option == "2":
        print("Currently in progress")
    elif option == "3":
        print("Currently in progress")
    elif option == "4":
        print("Currently in progress")
    elif option == "5":
        print("Currently in progress")
    elif option == "6":
        print("Currently in progress")
    elif option == "7":
        print("Currently in progress")
    elif option == "":
        print("Thanks for using this tool")
        print("Come back soon!")
        break
    else:
        print("Please enter a number from 1 to 7, or hit Enter to log out.")



#print(option)



