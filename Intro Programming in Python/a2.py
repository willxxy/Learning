def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1) > len(dna2):
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for char in dna:
        if char == nucleotide:
            count+=1
    return count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if DNA sequence is valid. Valid meaning
    it contains no other characters than 'A', 'T', 'C', or 'G'.

    >>> is_valid_sequence('ATCCG')
    True
    >>> is_valid_sequence('AKTCGG')
    False

    """
    is_valid = True
    valid_sequence= 'ATCG'
    for n in dna:
        if n not in valid_sequence:
            return False
    return is_valid

def insert_sequence(dna1, dna2, ind):
    """(str, str, int) -> str

    Return the DNA sequence obtained by inserting the
    second DNA sequence into the first DNA sequence at the
    given index.

    >>>insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>>insert_sequence('ATGC', 'CG', 3)
    ATGCGC

    """
    return dna1[0:ind] + dna2 + dna1[ind:len(dna1)]


def get_complement(nucleotide):
    """(str) -> str

    Return the nucleotide's coplement.

    >>>get_complement('A')
    T
    >>>get_complement('G')
    C

    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'C':
        return 'G'

def get_complementary_sequence(dna):
    """(str) -> str

    Return the DNA sequence that is complementary to the
    given DNA sequence.

    >>>get_complementary_sequence('AT')
    'TA'
    >>>get_complementary_sequence('GC')
    'CG'

    """
    c_dna = ""
    for n in dna:
        if n == 'A':
            c_dna += 'T'
        elif n == 'T':
            c_dna += 'A'
        elif n == 'G':
            c_dna += 'C'
        elif n == 'C':
            c_dna += 'G'
    return c_dna
