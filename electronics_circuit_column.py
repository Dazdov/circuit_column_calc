def Tres(a):
    b=0
    for i in a:
        b+=i
    return b
def Tcur(r,v):
    return v/r


def main():
    a = []
    count = 0
    NUM_OF_RESISTORS = 3
    for i in range(NUM_OF_RESISTORS):
        print("enter value for resistor",i+1)
        b = int(input())
        a.append(b)
    E = int(input("value for power "))
    print("It=",Tcur(Tres(a),E))
    print("Rt=",Tres(a))
    for i in a:
        count +=1
        print("vr",count,Tcur(Tres(a),E) * i)

main()
