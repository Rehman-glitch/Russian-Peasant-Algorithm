A = int(input ("A="))
B = int(input ("B="))
D = 0
def Mod (A,B):
    while A > B:
        A = A - B
    return A
while A > 0:
    if Mod (A,2) == 1:
            C = B + D
            D = C
    A = A//2
    B = B*2
print(C)