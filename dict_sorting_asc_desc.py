arms={">":"<", "\\":"/", "]":"[","}":"{", ")":"(", "/":"\\"}

face = input()
arm = input()
r_arm = "".join([x if not x in arms.keys() else arms[x] for x in arm[::-1]])

print(arm, face, r_arm, sep="")



"""
I=input
f=I()
a=I()
d={'<':'>','/':'\\','[':']','{':'}','(':')'}
d|={v:k for k,v in d.items()}
I(a+f+''.join([c,d.get(c)][c in d] for c in a[::-1]))
"""