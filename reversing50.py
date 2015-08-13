expr_08 = [ 'g','o','4','a','0','#','V','(','1','0' ]
array = [ 'A','g','a','a','l','d','x','a','m','l'  ]
expr_2E = [  'r','B','3','a','d','n','$','h','+','Z' ]
array2 = [ 'd','e','x','o','=','W','2','#','9','^' ]
expr_54 = [ 'd','e','x','o','=','W','2','#','9','^' ]
array3 = [ (0) for _ in range(14) ]

st = "*$8(2%$U\"70QI$"
flag = ""

for i in range(len(st)):
    array3[i] = st[i]
for i in range(5):
    tmp = 0
    tmp ^= ord(array[0])
    tmp ^= ord(array3[i])
    array3[i] = chr(tmp)
for i in range(5, len(st)-4, 1):
    tmp = 0
    tmp ^= ord(array3[i])
    tmp ^= ord(array[i-4])
    array3[i] = chr(tmp)
for i in range(len(st)-4, len(st), 1):
    tmp = 0
    tmp ^= ord(array3[i])
    tmp ^= ord(array2[i-10])
    array3[i] = chr(tmp)

    
for i in range(len(array3)):
    flag += str(array3[i])
print flag
