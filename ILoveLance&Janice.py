def solution(msg):
    kv={}
    decrypted=[]
    for i,j in zip(range(97,123),range(122,96,-1)):
        kv[chr(i)]=chr(j)
    
    for c in msg:
        if c in kv:
            c=kv[c]
        decrypted.append(c)
    return ''.join(decrypted)

print(solution("Czm blf fhv blfi mvd zxxvhh gl urmzoob glkkov Clnnzmwvi Lznywz'h vero vnkriv?"))