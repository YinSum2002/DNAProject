########
import random


from dna_kernel import random_base # Provided to you
random.seed(5)
import dna_kernel
########

def display_menu():
    """ display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Compare all; 7-Analyze")

#today
#### To complete (all functions below)

def random_strand():
    strand = ""
    for x in range(dna_kernel.MAX_STRAND):
        strand += dna_kernel.random_base()
    return strand

def initialize(): #keep this at the beginning
    #generate the max strand within initialize

    #copy_strand = str(random_strand())
    patients = [['Amy', '36', random_strand()],
                ['Bob', '28', random_strand()],
                ['Brooke', '34', random_strand()],
                ['Connor', '27', random_strand()],
                ['James', '61', random_strand()],
                ['Jenna', '44', random_strand()],
                ['Kate', '18', random_strand()],
                ['Pat', '26', random_strand()],
                ['Peter', '19', random_strand()],
                ['Tony', '55', random_strand()]]
    return patients

def display(patients):
    print(f'\t\tName\t\tage\t\tDNA-strand ({dna_kernel.MAX_STRAND} length)') #tabs look to be different lengths?
    print("----------------------------------------------------------------")
    c=1
    for p in patients:
        print(f'{c}\t\t{p[0]}\t\t{p[1]}\t\t{p[2]}')
        c+=1




