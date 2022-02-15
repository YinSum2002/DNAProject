"""" Do not modify this file """

import random

random.seed(5) # random seed for reproducibility
MAX_STRAND=20

def random_base():
    """ returm a DNA base at random """
    bases=["A","C","G","T"]
    return random.choice(bases)
