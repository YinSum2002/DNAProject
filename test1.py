
from dna_tool import random_strand, display

##################### TEST FOR OPTION 1
print("\n****TEST the random_strand function****")
print(random_strand())

#####################
print("\n****TEST patients data and display function****")
patient1=["Lucy","18",random_strand()]
patient2=["Tom","20",random_strand()]
patients=[patient1,patient2]
display(patients)

