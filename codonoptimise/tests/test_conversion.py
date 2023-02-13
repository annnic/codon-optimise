import os

import pytest

from codonoptimise.codon_opt import make_new_seq
from codonoptimise.ppa_codon_dict import ppa_CUB_10


@pytest.mark.parametrize('test_protein_seq, expected_dna_seq', [("MRT*", "ATGAGAACTTGA"),
                                                                ("MSKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTT",
 "ATGTCTAAGGGAGAGGAGCTCTTCACTGGAGTGGTGCCTATCCTCGTGGAGCT"
 "CGATGGAGATGTGAATGGACATAAGTTCTCTGTGTCTGGAGAGGGAGAGGGAG"
 "ATGCTACTTACGGAAAGCTCACTCTCAAGTTCATCTGCACTACT")])


def test_make_new_seq(test_protein_seq, expected_dna_seq):
    dna_seq = make_new_seq(test_protein_seq, ppa_CUB_10)
    assert dna_seq == expected_dna_seq
