from Bio import SeqIO
# 🧬 Step 1 — Extract a small reference region
#samtools faidx /mnt/data1/db/gcp-public-data--broad-references/hg38/v0/GIABv1mask/Homo_sapiens_assembly38.GIABv1mask.fasta  chr1:100000-101000 > mini_reference.fa

# 🧬 Step 2 — Introduce a mutation
record = SeqIO.read("mini_reference.fa", "fasta")

seq = list(record.seq)

# introduce SNV at position 200 (0-based index)
seq[200] = "T" if seq[200] != "T" else "A"

record.seq = "".join(seq)

SeqIO.write(record, "mini_reference_mut.fa", "fasta")


# Step 3 — Generate paired-end FASTQ with Q30
import random

# Load mutated reference sequence
with open("mini_reference_mut.fa") as f:
    lines = f.readlines()
    seq = "".join([l.strip() for l in lines if not l.startswith(">")])

read_length = 150
num_reads = 200
insert_size = 300  # typical paired-end insert

def reverse_complement(s):
    complement = str.maketrans("ACGT", "TGCA")
    return s.translate(complement)[::-1]

with open("sample_R1.fastq", "w") as r1, open("sample_R2.fastq", "w") as r2:

    for i in range(num_reads):
        # pick fragment
        start = random.randint(0, len(seq) - insert_size)
        fragment = seq[start:start + insert_size]

        # R1 = forward read
        read1 = fragment[:read_length]

        # R2 = reverse complement of end
        read2 = reverse_complement(fragment[-read_length:])

        # constant high quality (Q30 → ASCII "?")
        quality = "?" * read_length

        # write R1
        r1.write(f"@read{i}/1\n")
        r1.write(read1 + "\n")
        r1.write("+\n")
        r1.write(quality + "\n")

        # write R2
        r2.write(f"@read{i}/2\n")
        r2.write(read2 + "\n")
        r2.write("+\n")
        r2.write(quality + "\n")
