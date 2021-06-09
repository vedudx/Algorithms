A=[5,4,3,2,1]
B=[]
C=[]
def hanoi(height,fromPole, toPole, withPole):
    if height>=1:
        hanoi(height-1,fromPole,withPole,toPole)
        toPole.append(fromPole.pop())
        print (A,B,C)
        hanoi(height-1,withPole,toPole,fromPole)
hanoi(5,A,B,C)