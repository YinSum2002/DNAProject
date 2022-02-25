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

patient_list = dna.initialize()

dna.display_menu()
while True:
    option = input("Command (Enter to exit): ")
    if option == "1":
        dna.display(patient_list)
    elif option == "2":
        dna.info(patient_list)
    elif option == "3":
        r = int(input("Who do you want to remove (enter number):"))
        if r in range(1, len(patient_list)):
            del patient_list[r - 1]
        else:
            print("Patient not found!")
    elif option == "4":
        dna.add_new_patient(patient_list)
        #print("Currently in progress")
    elif option == "5":
        dna.compare(patient_list)
        #print("Currently in progress")
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



