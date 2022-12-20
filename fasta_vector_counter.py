import os

fasta_dir = 'seqs_fasta.screen'

a = 0
c = 0
t = 0
g = 0
n = 0
x = 0

fasta_file = open(fasta_dir, 'r')

for line in fasta_file.readlines():
    print(line)
    if line[0] == '>':
        continue
    else:
        a += line.count('A')
        c += line.count('C')
        t += line.count('T')
        g += line.count('G')
        n += line.count('N')
        x += line.count('X')

print("A: "+str(a))
print("C: "+str(c))
print("T: "+str(t))
print("G: "+str(g))
print("N: "+str(n))
print("X: "+str(x))

print("Porcentagem do vetor: "+str((x/(a+c+t+g+n+x))*100))