import sys
import re

def hssort (innumbers):
    '''Sort numbers in a list (array): large to low'''
    '''Input is a number list'''
    '''Non-number input is not allowed'''
    if len(innumbers) == 0:
        return([])
    elif len(innumbers) == 1:
        return(innumbers)
    # Pick the first number and separate all numbers to bigger and lower groups;
    bigger = []
    lower = []
    curr = [innumbers[0]]
    # print(f"curr.{curr[0]}")
    for n in innumbers[1:]:
        if n > innumbers[0]:
            bigger.append(n)
        elif n < innumbers[0]:
            lower.append(n)
        else:
            curr.append(n)
    big_sorted = hssort(bigger)
    low_sorted = hssort(lower)
    all_sorted = big_sorted + curr + low_sorted
    return(all_sorted)

def hssum (innumbers):
    '''Sum numbers'''
    s = 0
    for n in innumbers:
        s = s + n
    return(s)

def n50_stat (innumbers):
    '''Count the total size, sequence number and N50'''
    '''Input is a number of list'''
    '''Output is a number list of (total size, sequence number, N50, N50 index)'''
    halfsum = hssum(innumbers) / 2
    sortnum = hssort(innumbers)
    v = 0
    idx = 0
    n50 = -1
    for n in sortnum:
        n50 = n
        idx = idx + 1
        v = v + n
        if v >= halfsum:
            break
    return(int(halfsum*2), len(innumbers), n50, idx)

# infn1 = 'in.fasta'
if len(sys.argv) == 1:
    print("[Error] Correct command line should be:", file= sys.stderr)
    print(f"  python3 {sys.argv[0]} in.fasta > in.fasta.N50_stat", file= sys.stderr)
    exit()
elif len(sys.argv) > 2:
    print(f"[Warn] Only the first file {sys.argv[1]} will be processed.", file= sys.stderr)

infn1 = sys.argv[1]

seqs = ''
seqlen = []
with open(infn1, 'r') as infile1:
    if infile1.mode == "r":
        # line1 = infile1.readline()
        for line1 in infile1:
            line1 = line1.strip()
            if line1.startswith(">"):
                seqs = re.sub(r'\s', '', seqs, count= 0)
                if seqs != '':
                    seqlen.append(len(seqs))
                    seqs = ''
            else:
                seqs = seqs + line1
        infile1.close()
        seqs = re.sub(r'\s', '', seqs, count= 0)
        if seqs != 0:
            seqlen.append(len(seqs))
            seqs = ''
        (ttl_bp, ttl_num, n50, n50idx) = n50_stat(seqlen)
        print(f"Assembly size  : {ttl_bp}")
        print(f"Sequence number: {ttl_num}")
        print(f"N50      : {n50}")
        print(f"N50 index: {n50idx}")

print("All finished.", file= sys.stderr)
