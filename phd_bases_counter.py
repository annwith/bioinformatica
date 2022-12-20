import os
import pandas as pd

phd_dir = 'phd_dir/'

entries = os.listdir(phd_dir)

files_info = []

for entry in entries:
    print(entry)
    entry_file = open(phd_dir+entry, 'r')
    text = entry_file.read()
    text = text.split('BEGIN_DNA')[1]
    text = text.split('END_DNA')[0]
    a = text.count('a')
    c = text.count('c')
    t = text.count('t')
    g = text.count('g')
    n = text.count('n')

    files_info += [
        {
            'name': entry,
            'a': a,
            'c': c,
            't': t,
            'g': g,
            'n': n
        }
    ]

df = pd.DataFrame(files_info)
df.to_csv('phd_bases_counter.csv', index=False)