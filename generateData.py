import math
import numpy as np
import random
import sys


def generate_nested_sequence(length, min_seglen=5, max_seglen=10):
    """Generate low-high-low sequence, with indexes of the first/last high/middle elements"""

    # Low (1-5) vs. High (6-10)
    seq_before = [(random.randint(1,5)) for x in range(random.randint(min_seglen, max_seglen))]
    seq_during = [(random.randint(6,10)) for x in range(random.randint(min_seglen, max_seglen))]
    seq_after = [random.randint(1,5) for x in range(random.randint(min_seglen, max_seglen))]
    seq = seq_before + seq_during + seq_after

    # Pad it up to max len with 0's
    seq = seq + ([0] * (length - len(seq)))
    return [seq, len(seq_before), len(seq_before) + len(seq_during)-1]


data = generate_nested_sequence(10,
                                        3,
                                        5)

print data[0];
print data[1];
print data[2];