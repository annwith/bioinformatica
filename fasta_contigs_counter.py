import os
import pandas as pd

fasta_dir = 'seqs_fasta.screen.contigs'

a = 0
c = 0
t = 0
g = 0
n = 0
x = 0
contig = 0

fasta_file = open(fasta_dir, 'r')

contigs_info = []

for line in fasta_file.readlines():
    print(line)
    if line[0] == '>':
        if contig > 0:
            contigs_info += [
                {
                    'contig': contig,
                    'a': a,
                    'c': c,
                    't': t,
                    'g': g,
                    'n': n,
                    'x': x
                }
            ]
            a = 0
            c = 0
            t = 0
            g = 0
            n = 0
            x = 0
        contig += 1
    else:
        a += line.count('A')
        c += line.count('C')
        t += line.count('T')
        g += line.count('G')
        n += line.count('N')
        x += line.count('X')

contigs_info += [
    {
        'contig': contig,
        'a': a,
        'c': c,
        't': t,
        'g': g,
        'n': n,
        'x': x
    }
]

df = pd.DataFrame(contigs_info)
df.to_csv('fasta_contigs_counter.csv', index=False)