########
import random

import dna_kernel
from dna_kernel import random_base # Provided to you
random.seed(5)
########

def display_menu():
    """ display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Compare all; 7-Analyze")

#today
#### To complete (all functions below)


def initialize(): #keep this at the beginning
    #generate the max strand within initialize
    patients = [['Amy', '36', ''],
                ['Bob', '28', ''],
                ['Brooke', '34', ''],
                ['Connor', '27', ''],
                ['James', '61', ''],
                ['Jenna', '44', ''],
                ['Kate', '18', ''],
                ['Pat', '26', ''],
                ['Peter', '19', ''],
                ['Tony', '55', '']]
    return patients

def display(x):
    print(x)




