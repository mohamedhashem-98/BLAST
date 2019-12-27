import re
##############################################
def readDataBase(filename):
    List = []
    with open(filename) as fr:
        lines = fr.readlines()
    for i in lines:
        List.append(i)
    Sequence = ""
    for i in range(len(List)):
        Sequence += List[i]
    List = Sequence.split("\n")
    Sequence = ""
    for i in List:
        Sequence += i
    return Sequence  
####################################################
def readQuery(filename , n):
    List = []
    with open(filename) as fr:
        lines = fr.readlines()
    for i in lines:
        List.append(i)
    Sequence = ""
    for i in range(len(List)):
        Sequence += List[i]
    List = Sequence.split("\n")
    Sequence = ""
    for i in List:
        Sequence += i
    cur = ""
    for i in range(0 , len(Sequence)):
        if i + n < len(Sequence):
            cnt = 0 
            for j in range(i , i + n - 1):
                if Sequence[j] == Sequence[j+1]:
                    cnt+=1
            if cnt == n - 1:
                i = i + n
            else:
                cur += Sequence[i]
        else:
            cur += Sequence[i]
    Sequence = cur
    for i in List:
        Sequence += i
    return Sequence  
##############################################
def Make_Sequences(Seq):
    Sequences = []
    for i in range(len(Seq)):
        if i + 10 < len(Seq):
            Sequences.append(Seq[i:i+11])
    return Sequences
###############################################
def Mutate(Sequence):
    dna = ['A' , 'C' , 'G' , 'T']
    Sequences = set()
    for i in range(len(Sequence)):
        x = Sequence.split()
        for j in range(4):
            x[i] = dna[j]
            cur = ""
            for z in x:
                cur += z
            Sequence.add(cur)
    return Sequences
###############################################
def Make_Mutations(Sequences):
    Muations = dict()
    for i in range(len(Sequences)):
        Muations[Sequences[i]] = Mutate(Sequences[i])
    return Muations
################################################
def CalculateScore(Seq1 , Seq2):
    score = 0
    for i in range(len(Seq1)):
        if Seq1[i] == Seq2[i]:
            score += 1
        else:
            score += -1
    return score
################################################
def Seeds(threshold , Sequences):
      seeds = []
      for key in Sequences.items():
          for j in range(len(Sequences[key])):
              if CalculateScore(key , Sequences[key][j]) >= threshold :
                  seeds.append(Sequences[key][j])
      return seeds
################################################
def Make_Hits(seeds , Seq):
    ranges = []
    for i in range(len(Seq)):
        if i + 10 < len(Seq):
            if Seq[i:i+11] in seeds:
                ranges.append([i , i+2])
    return ranges
#################################################
def extend_Sequence(lQ , rQ , lD , rD , DataBaseSeq , QuerySeq , visited , threshold):
    score = 0
    for i in range(11):
        if QuerySeq[lQ + i] == DataBaseSeq[lD + i] :
            score += 1
        else:
            score += -1
    left = 1
    right = 1
    while left == 1 or right == 1 :
        if left == 1 :
            if lQ - 1 >= 0 and lD - 1 >= 0 :
                if visited[lD - 1] == 0:
                    val = 0
                    if QuerySeq[lQ - 1] == DataBaseSeq[lD - 1] :
                        val = 1
                    else:
                        val = -1
                    if score + val >= threshold :
                        visited[lD - 1] = 1
                        score += val
                        lD-=1
                        lQ-=1
                    else:
                        left = 0
                else:
                    left = 0
            else:
                left = 0
        if right == 1 :
            if rQ + 1 < len(QuerySeq) and rD + 1 < len(DataBaseSeq) :
                if visited[rD + 1] == 0:
                    val = 0
                    if QuerySeq[rQ + 1] == DataBaseSeq[rD + 1] :
                        val = 1
                    else:
                        val = -1
                    if score +val >= threshold :
                        visited[rD + 1] = 1
                        score +=val
                        rD+=1
                        rQ+=1
                    else:
                        right = 0
                else:
                    right = 0
            else:
                right = 0       
    return [score , [lD , rD , lQ , rQ]]                
#################################################
def HSP(hits , DataBaseSeq , QuerySeq , threshold):
    Merge = [0 for i in range(len(DataBaseSeq))]
    HSP_LIST = []
    for i in range(len(QuerySeq)):
        if i + 10 < len(QuerySeq):
            for j in range(len(hits)):
                if QuerySeq[i:i+11] == DataBaseSeq[hits[j][0]:(hits[j][1]+1)] :
                   c = 0
                   for x in range(11):
                       if Merge[hits[j][0] + x] == 0 :
                           c+=1
                   if c == 11 :
                      HSP_LIST.append(extend_Sequence(i , i+10 , hits[j][0] , hits[j][1] , DataBaseSeq , QuerySeq , Merge , threshold))
    return HSP_LIST
########################################################################
def final(HSP_LIST , DataBaseSeq , QuerySequence):
    f_score = 0
    for i in range(len(HSP_LIST)):
        f_score += HSP_LIST[i][0]
        print("Score : {} .".format(HSP_LIST[i][0]))
        print("{} .".format(DataBaseSeq[HSP_LIST[i][1][0] : HSP_LIST[i][1][1]+1]))
        for j in range(HSP_LIST[i][1][0] , HSP_LIST[i][1][1]+1):
            print('|')
        print("{} .".format(QuerySequence[HSP_LIST[i][1][2] : HSP_LIST[i][1][3]+1])  )
    print("Final Score : {} .".format(f_score))
########################################################################                  
        
    