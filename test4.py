from dna_tool import *
###################### TEST for OPTION 4
print("\n****TEST the add_new_patient function****")
patients=[["Lucy","18",random_strand()]]
patients=add_new_patient(patients)
display(patients)
