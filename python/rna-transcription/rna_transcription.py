def to_rna(dna_strand):

    dna_strand = dna_strand.upper() #just in case
    transcript = { 'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    if dna_strand.strip('GCTA'):
        raise ValueError('Found letter not assigned to nucleotide')
    else:
        return ''.join(transcript[i] for i in dna_strand)

def to_rn(dna_strand):
    from string import maketrans
    return dna_strand.translate(maketrans("GCTA", "CGAU"))