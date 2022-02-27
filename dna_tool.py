########
import random


from dna_kernel import random_base, MAX_STRAND # Provided to you
random.seed(5)
########

def display_menu():
    """ display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Compare all; 7-Analyze")

#today
#### To complete (all functions below)

def random_strand(): #to be impemented in initialize
    '''generates random strand of length MAX_STRAND
        adds random choice of random_base to blank strand
    '''
    strand = "" #
    for x in range(MAX_STRAND): #
        strand += random_base()
    return strand #


def initialize():
    '''creates original list
        returns as a variable
    '''
    patients = [['Amy', '37', random_strand()],
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
    '''displays variable outputted by initialize function
        uses tabs to format spacing of attributes
        uses c as ID tracker
    '''
    print(f'\t\tName\t\tage\t\tDNA-strand ({MAX_STRAND} length)') #tabs look to be different lengths?
    print("----------------------------------------------------------------")
    c=1
    for p in patients:
        print(f'{c}\t\t{p[0]}\t\t{p[1]}\t\t{p[2]}')
        c+=1

def info(patients):
    '''Takes list of patients
        returns breakdown of age groups
    '''
    a = 0 #different bins
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    asum = 0 #total age to calculate average
    for p in patients:
        z = int(p[1])
        if z < 20:
            a += 1
            asum += z
        elif z < 30:
            b += 1
            asum += z
        elif z < 40:
            c += 1
            asum += z
        elif z < 50:
            d += 1
            asum += z
        elif z < 60:
            e += 1
            asum += z
        else:
            f += 1
            asum += z
    sum = a + b + c + d + e + f #total number to calculate average
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
    print("")
    print(f'Age Mean: {asum/sum} ')

def check_strand(strand):
    '''used in add_new_patient
        returns False if length is not 20
        returns False if characters not ACGT
    '''
    if len(strand) != 20:
        return False
    for p in strand:
        if p != "A" and p != "C" and p != "G" and p != "T":
            return False
    return True #else allows add_new_patient to carry on

def add_new_patient(patients):
    '''Create list of new Name, age, strand
        adds to original list
    '''
    n = ""
    while n == "":
        n = input("Enter Name: ")
    a = ""
    while a == "":
        a = input("Enter Age: ")
    s = ""
    while s == "":
        s = input("Enter DNA Strand: ")
        if not check_strand(s):
            print("Bad input! -length must be 20")
            s = ""
    new_patient = [[n, a, s]] #new list created by inputs
    return patients + new_patient

def compare(strand1, strand2):
    '''simply compares two strings
    '''
    total_strand = ""
    for x in range(len(strand1)):
        if strand1[x] == strand2[x]:
            total_strand += strand1[x]
        else:
            total_strand += "x" #for if strands are not equal at x
    return total_strand

def check_completeness(common):
    '''scans for how similar two strands are
        used in compare_patients as new variable
    '''
    count = 0 #every time there is a commonality, add one
    for c in common:
        if c != "x":
            count += 1
    return 100 * count/len(common)


def compare_patients(patients):
    '''input two patients
        return common strand and percent similarity
    '''
    f = int(input("First patient (enter number): "))
    if f not in range(1,len(patients)+1):
        print("Patient not found!")
        return

    s = int(input("Second patient (enter number): "))
    if s not in range(1,len(patients)+1):
        print("Patient not found!")
        return

    first_strand = patients[f-1][2]
    second_strand = patients[s-1][2]
    final_strand = compare(first_strand, second_strand) #use of compare
    percent_similar = check_completeness(final_strand) #use of check_completeness
    print(f'{patients[f-1][0]} and {patients[s-1][0]} common strand is {final_strand}')
    print(f'They are similar at {percent_similar}%')

def compare_all(patients):
    '''takes list
        returns all patients greater than 33% similarity
    '''
    for i in range(len(patients)):
        for f in range(i+1, len(patients)): #nested for loop
            patient1 = patients[i]
            patient2 = patients[f]
            final_strand = compare(patient1[2], patient2[2])
            percent_similar = check_completeness(final_strand)
            if percent_similar > 33:
                print(f'{patient1[0]} vs {patient2[0]} {percent_similar}%')

def has_pattern(condition_strand, full_strand):
    t = 0
    for i in full_strand:
        if condition_strand == full_strand[t:t+len(condition_strand)]:
            return True
        t += 1
    return False

def find_pattern(patient_list, dna_strand):
    n = 0
    for p in patient_list:
        if has_pattern(dna_strand, p[2]) is True:
        #if dna_strand in p[2]:
            print(f'{p[0]}\t\t{p[1]}\t\t{p[2]}')
            n += 1
    return n

    #nested for loop with abc in dna_strand

    #if abc is in dna_strand

    #return patient info as list

    #number of patients += 1