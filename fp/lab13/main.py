def verif(v,n):
    '''
    compara v[i] cu v[j] si daca sunt egale returneaza fals
    :param v:
    :param n:
    :return:
    '''
    for i in range(0,n-1):
        for j in range(i+1,n):
            if v[i] == v[j]:
                return False
    return True

def verif2(v,n):
    '''
    verifica daca v[i]-v[j]==1
    :param v:
    :param n:
    :return:
    '''
   #set candidat: lista de permuntari
    #solutie candidat: o lista de permutari cu proprietatea data x=[x1,x2,..]
    for i in range(1,n):
        ok = 0
        for j in range(0,i+1):
            if v[i]-v[j] == 1 or -1*(v[i]-v[j]) == 1:
                ok = 1
        if ok == 0:
            return False
    return True

def permutari_recursiv(v,n,k):
    #functia de selectie alege permutarile cu proprietatea data
    for i in range(1,n+1):
        v[k] = i
        if k == n-1:
            if verif(v,n) == True and verif2(v,n) == True:
                print(v)
        elif k<n-1:
            permutari_recursiv(v,n,k+1)

def permutari_iterativ(v,n):
    v = [-1]
    used_values = [[] for i in range(n)]
    while len(v) > 0:
        val = 1
        ok = False
        while val <= n and not ok:
            if val not in used_values[len(v)-1]:
                v[-1] = val
                ok = True
                used_values[len(v)-1].append(val)
            val += 1
        if ok == True:
            if(len(v)) == n:
                if verif(v,n) == True and verif2(v,n) == True:
                    print(v)
            else:
                v.append(-1)
        else:
            used_values[len(v)-1] = []
            v = v[:-1]


n = int(input("scrie n: "))
v = []
k = 0

for i in range(0,n):#solutie candidat: x=[x1,x2...] permutarile
    v.append(0)

permutari_recursiv(v,n,k)
print()
permutari_iterativ(v,n)