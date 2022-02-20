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

def random_strand(): #to be impemented in initialize
    strand = "" #
    for x in range(dna_kernel.MAX_STRAND): #
        strand += dna_kernel.random_base()
    return strand #

def initialize():
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

def info(patients):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    for p in patients:
        z = int(p[1])
        if z < 20:
            a += 1
        elif z < 30:
            b += 1
        elif z < 40:
            c += 1
        elif z < 50:
            d += 1
        elif z < 60:
            e += 1
        else:
            f += 1
    sum = a + b + c + d + e + f
    ap = (a / sum) * 100
    bp = (b / sum) * 100
    cp = (c / sum) * 100
    dp = (d / sum) * 100
    ep = (e / sum) * 100
    fp = (f / sum) * 100
    print(f'<20 : {ap}%')
    print("20's: "f'{bp}%')
    print("30's: "f'{cp}%')
    print("40's: "f'{dp}%')
    print("50's: "f'{ep}%')
    print(f'>=60: {fp}%')


