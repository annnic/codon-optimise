from codonoptimise.ppa_codon_dict import ppa_CUB_10, ppa_CUB_3


def make_new_seq(protein_seq, ppa_CUB_10):
    dna_seq = ""

    for aminoacid in protein_seq:
        dna_seq = dna_seq + ppa_CUB_10[aminoacid]

    return dna_seq

# gcamp6f
protein_seq = "MGSHHHHHHGMASMTGGQQMGRDLYDDDDKDLATMVDSSRRKWNKTGHAVRAIGRLSSLENVYIKADKQKNGIKANFKIRHNIEDGGVQLAYHYQQNTPIGDGPVLLPDNHYLSVQSKLSKDPNEKRDHMVLLEFVTAAGITLGMDELYKGGTGGSMVSKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTTGKLPVPWPTLVTTLTYGVQCFSRYPDHMKQHDFFKSAMPEGYIQERTIFFKDDGNYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNLPDQLTEEQIAEFKEEFSLFDKDGDGTITTKELGTVMRSLGQNPTEAELQDMINEVDADGDGTIDFPEFLTMMARKMKYRDTEEEIREAFGVFDKDGNGYISAAELRHVMTNLGEKLTDEEVDEMIREADIDGDGQVNYEEFVQMMTAK*"

# HygR
protein_seq = "MKKPELTATSVEKFLIEKFDSVSDLMQLSEGEESRAFSFDVGGRGYVLRVNSCADGFYKDRYVYRHFASAALPIPEVLDIGEFSESLTYCISRRAQGVTLQDLPETELPAVLQPVAEAMDAIAAADLSQTSGFGPFGPQGIGQYTTWRDFICAIADPHVYHWQTVMDDTVSASVAQALDELMLWAEDCPEVRHLVHADFGSNNVLTDNGRITAVIDWSEAMFGDSQYEVANIFFWRPWLACMEQQTRYFERRHPELAGSPRLRAYMLRIGLDQLYQSLVDGNFDDAAWAQGRCDAIVRSGAGTVGRTQIARRSAAVWTDGCVEVLADSGNRRPSTRPRAKE*"
dna_seq = make_new_seq(protein_seq, ppa_CUB_3)
print(dna_seq)

with open("dna_seq.txt", "w") as f:
    f.write('> DNA sequence codon optimised for Ppa (top 10%) \n')
    f.write(dna_seq)
