########
import random

from dna_kernel import random_base # Provided to you
########

def display_menu():
    """ display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Compare all; 7-Analyze")


#### To complete (all functions below)
def initialize():
    name: list[str] = ["Amy", "Bob", "Brooke", "Connor", "James", "Jenna", "Kate", "Pat", "Peter", "Tony"]
    age: list[str] = ["37", "28", "34", "27", "61", "44", "18", "26", "19", "55"]
    dna_strand = random_base()
    for x in range(10):
        patient: list[str] = [name[x], age[x], dna_strand]
        print(patient)




#def random_strand():
    #strand=""
    #while len(strand)<20:
        #strand.append()
    #if len(strand) == MAX_STRAND:
        #print(strand)

