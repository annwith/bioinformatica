import argparse
import subprocess
import time

parser = argparse.ArgumentParser(
                    prog = 'Bioinformática',
                    description = 'Automatização do processo de formação dos contigs')

parser.add_argument('-chr', '--chromat_dir', required=True)
parser.add_argument('-phd', '--phd_dir', required=True)
parser.add_argument('-vector', '--vector_sequence', required=True)
parser.add_argument('-minmatch', '--minimum_match', required=True)
parser.add_argument('-minscore', '--minimum_score', required=True)
# parser.add_argument('-out', '--output_path', required=True)

args = parser.parse_args()

# Phred reads the chromat files in "chromat_dir" and write the "phd" files to "phd_dir".
# phred -id chromat_dir -pd phd_dir
p = subprocess.call([
  "phred", 
  "-id", 
  args.chromat_dir, 
  "-pd", 
  args.phd_dir
])

# Next it makes FASTA files from the "phd" files by running the phd2fasta program.
# phd2fasta -id phd_dir -os seqs_fasta -oq seqs_fasta.screen.qual
p = subprocess.call([
  "phd2fasta", 
  "-id", 
  args.phd_dir, 
  "-os", 
  "seqs_fasta", 
  "-oq", 
  "seqs_fasta.screen.qual"
])

# Subsequently it screens out the vector in the sequences in "seqs_fasta" using cross_match:
# cross_match seqs_fasta vector.seq -minmatch 12 -minscore 20 -screen > screen.out
p = subprocess.call([
  "cross_match", 
  "seqs_fasta", 
  args.vector_sequence, 
  "-minmatch",
  args.minimum_match,
  "-minscore",
  args.minimum_score,
  "-screen"
])

# which generates the screened sequence file "seqs_fasta.screen",
# It runs phrap to perform the sequence assembly as follows:
# phrap seqs_fasta.screen -new_ace > phrap.out
p = subprocess.call([
  "phrap", 
  "seqs_fasta.screen", 
  "-new_ace"
])