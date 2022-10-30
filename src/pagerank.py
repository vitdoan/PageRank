import math
import sys
import gzip
import copy

def pagerank():
    inlinks_map = {}
    outlinks_map = {}
    f = gzip.open(inputFile, 'rt')

    for line in f:
        line_arr = line.strip().split('\t')
        if line_arr[1] in inlinks_map:
            inlinks_map[line_arr[1]].append(line_arr[0])
        else:
            inlinks_map[line_arr[1]] = [line_arr[0]]
        if line_arr[0] not in inlinks_map:
            inlinks_map[line_arr[0]] = []
        if line_arr[0] in outlinks_map:
            outlinks_map[line_arr[0]].append(line_arr[1])
        else:
            outlinks_map[line_arr[0]] = [line_arr[1]]
        if line_arr[1] not in outlinks_map:
            outlinks_map[line_arr[1]] = []
    temp_count = {}

    #Inlink
    N = len(outlinks_map)
    I = {}
    for page in outlinks_map:
        I[page] = 1/N
    R = {}

    temp = 0
    for page in outlinks_map:
        R[page] = lambda_val/N
    for page in outlinks_map:
        Q = []
        for q in outlinks_map[page]:
            Q.append(q)
        if len(Q) > 0:
            for q in Q:
                R[q] = R[q] + (1 - lambda_val) * I[page] / len(Q)
        else:
            temp = temp + (1 - lambda_val) * I[page] / N
    for page in outlinks_map:
        R[page] = R[page] + temp
    while not converge(I, R):
        temp = 0
        I = copy.deepcopy(R)
        for page in outlinks_map:
            R[page] = lambda_val/N
        for page in outlinks_map:
            Q = []
            for q in outlinks_map[page]:
                Q.append(q)
            if len(Q) > 0:
                for q in Q:
                    R[q] = R[q] + (1 - lambda_val) * I[page] / len(Q)
            else:
                temp = temp + (1 - lambda_val) * I[page] / N
        for page in outlinks_map:
            R[page] = R[page] + temp

    # Write to inlinks.txt
    for elem in inlinks_map:
        temp_count[elem] = len(inlinks_map[elem])
    inlinks_count = sorted(temp_count.items(), key=lambda x: x[1], reverse=True)
    write_inlinks = open(inLinksFile, "w")
    i = 1
    for page in inlinks_count:
        if(i > 100):
            break
        write_inlinks.write(str(page[0])+'\t'+str(i)+"\t"+str(page[1])+"\n")
        i+=1
    
    # Write to pagerank.txt
    page_rank_sort = sorted(R.items(), key=lambda x: x[1], reverse=True)
    write_pagerank = open(pagerankFile, "w")
    j = 1
    for page in page_rank_sort:
        if j > 100:
            break
        write_pagerank.write(str(page[0])+'\t'+str(j)+"\t"+str(page[1])+"\n")
        j+=1

def converge(I, R):
    v_r = list(R.values())
    v_i = list(I.values())
    sum_page = 0
    for i in range(0,len(v_r)):
        sum_page += (v_r[i] - v_i[i]) ** 2
    return math.sqrt(sum_page) < tau
    

def main():
    print("Hello World!")

if __name__ == '__main__':
        # Read arguments from command line; or use sane defaults for IDE.
    argv_len = len(sys.argv)
    inputFile = sys.argv[1] if argv_len >= 2 else "links.srt.gz"
    # inputFile = sys.argv[1] if argv_len >= 2 else "../small.srt.gz"
    lambda_val = float(sys.argv[2]) if argv_len >=3 else 0.2
    tau = float(sys.argv[3]) if argv_len >=4 else 0.005
    inLinksFile = sys.argv[4] if argv_len >= 5 else "inlinks.txt"
    pagerankFile = sys.argv[5] if argv_len >= 6 else "pagerank.txt"
    k = int(sys.argv[6]) if argv_len >= 7 else 100
    pagerank()
