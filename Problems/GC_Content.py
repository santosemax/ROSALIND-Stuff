from biopython import SeqIO

with open("test.txt", "r") as file:
    for record in SeqIO.parse(handle, 'fasta'):
        name = record.id
        sequence = record.seq

        print(name)
        

