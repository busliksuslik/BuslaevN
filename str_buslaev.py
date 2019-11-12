#1
S = input()
print(S[2])
print(S[len(S)-2])
print(S[0:5])
print(S[0:len(S)-2])
print(S[1:len(S):2])
print(S[2:len(S):2])
print(S[::-1])
print(S[0:len(S)-1:-2])
print(len(S))
#2
S = input()
print(S.count(' ')+1)
#3
S = input()
a = S[len(S)//2:len(S)]+S[0:len(S)//2]
print(a)
#4
S = input()
a = S[S.find(' ')+1:len(S)]+' '+S[0:S.find(' ')]
print(a)
#5
S = input()
if S.count('f') == 1:
    print(S.find('f'))
elif S.count('f') >= 2:
    print(S.find('f'))
    print(S.rfind('f'))
#5
S = input()
if S.count('f') == 1:
    print(-1)
elif S.count('f') >= 2:
    print(S.find('f',S.find('f')+1))
elif S.count('f') == 0:
    print(-2)
#7
S = input()
print(S[0:S.find('h')]+S[S.rfind('h')+1:len(S)])
#7
S = input()
print(S[0:S.find('h')]+S[S.rfind('h'):S.find('h')-1:-1]+S[S.rfind('h')+1:len(S)])
#8
S = input()
print(S.replace('1','one'))
#8
S = input()
print(S.replace('@',''))
