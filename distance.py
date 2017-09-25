import operator

def hamming(str1, str2):
    while len(str1) == len(str2):
      try: 
        return sum(map(operator.ne, str1, str2))
        break
      except ValueError:
        return("Strings should be the same length! Please change your input")
        break

def jaccard(str1, str2):
    intersect_card = len(set(str1).intersection(set(str2)))
    return intersect_card / float(len(str1) + len(str2) - intersect_card)

def levenshtein(str1, str2):
    n, m = len(str1), len(str2)
    if n > m:
      str1, str2 = str2, str1
      n, m = m, n
    if n == 0:
      return m
    x = range(n+1)
    for i in range(1,m+1):
        y, x = x, [i]+[0]*n
        for j in range(1,n+1):
            ins, delete = y[j]+1, x[j-1]+1
            subst = y[j-1]
            if str1[j-1] != str2[i-1]:
                 subst = subst + 1
            x[j] = min(ins, delete, subst)
    return x[n]

