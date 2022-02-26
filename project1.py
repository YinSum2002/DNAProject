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
        if r in range(1, len(patient_list)+1):
            del patient_list[r - 1]
        else:
            print("Patient not found!")
    elif option == "4":
        patient_list = dna.add_new_patient(patient_list)
    elif option == "5":
        dna.compare_patients(patient_list)
    elif option == "6":
        dna.compare_all(patient_list)
    elif option == "7":
        print("Currently in progress")
    elif option == "":
        print("Thanks for using this tool")
        print("Come back soon!")
        break
    else:
        print("Please enter a number from 1 to 7, or hit Enter to log out.")



#print(option)



