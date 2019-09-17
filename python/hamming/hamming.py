def distance(strand_a, strand_b):
    if strand_a.strip('CGAT') or strand_b.strip('CGAT'):
        raise ValueError("Strand has non nucleotide abbreviation")
    if not len(strand_a) == len(strand_b):
        raise ValueError("Strands don't have the same length")
    return sum(sa != sb for sa, sb in zip(strand_a, strand_b))
