########
import random

import dna_kernel
from dna_kernel import random_base # Provided to you
########

def display_menu():
    """ display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Compare all; 7-Analyze")


#### To complete (all functions below)


#def initialize():
    #name = ["Amy", "Bob", "Brooke", "Connor", "James", "Jenna", "Kate", "Pat", "Peter", "Tony"]
    #age = ["37", "28", "34", "27", "61", "44", "18", "26", "19", "55"]
    #def random_strand():
    #for x in range(10):
        #dna_strand = random_base()

        #strand = ""
        #while len(strand) < dna_kernel.MAX_STRAND:
            #strand = strand + random_base()
        #if len(strand) == dna_kernel.MAX_STRAND:
            #patient = [name[x], age[x], strand]
        #print(patient)



def dna_strand():
    while len(strand) < dna_kernel.MAX_STRAND:
        strand = strand + random_base()
    if len(strand) == dna_kernel.MAX_STRAND:
        print(strand)

def initialize():
    patients = [['Amy', '36', dna_strand],
                ['Bob', '28', dna_strand],
                ['Brooke', '34', dna_strand],
                ['Connor', '27', dna_strand],
                ['James', '61', dna_strand],
                ['Jenna', '44', dna_strand],
                ['Kate', '18', dna_strand],
                ['Pat', '26', dna_strand],
                ['Peter', '19', dna_strand],
                ['Tony', '55', dna_strand]]
    return patients

def display():
    print("In progress...")