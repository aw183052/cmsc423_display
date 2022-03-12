import sys
import os

def label_elements(bwt):
    count = dict()
    new_list = []

    for x in bwt:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    
    for i in range(len(bwt)):
        cur = bwt[i]
        new_list.append(bwt[i] + str(count[cur]))
        count[cur] -= 1
    
    return new_list

def reverse_bwt(bwt):
    if len(bwt) < 1:
        return ""
    
    left = label_elements(sorted(bwt))
    right = label_elements(bwt)
    ret = left[0][0]
    i, j = 0, 0

    for x in range(len(left)):
        i = left.index(right[j])
        ret += left[i][0]
        j = i
        
    ret = ret[:len(ret) - 1]
    return ret[::-1]

def main():
    f = open("input", "r")
    if os.path.exists("output"):
        os.remove("output")
    out = open("output", "w")
    
    bwt = f.readline().rstrip()
    bwt = [i for i in bwt]

    output = reverse_bwt(bwt)
    
    out.write(output)
    f.close()
    out.close()

if __name__ == "__main__":
    main()