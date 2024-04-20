class calc:
    def getsum(self,a,b):
        print("Sum:",a+b)
    

    def getmul(self,a,b):
        print("Mul:",a*b)


class page1(calc):
    def getsum(self, a, b):
        return super().getsum(a, b)
    
    def getmul(self, a, b):
        return super().getmul(a, b)

class page2(calc):
    def getsum(self, a, b):
        return super().getsum(a, b)
    
    def getmul(self, a, b):
        return super().getmul(a, b)
    


n1=int(input("Enter Number1:"))
n2=int(input("Enter Number2:"))
p1=page1()
p2=page2()

p1.getsum(n1,n2)
p1.getmul(n1,n2)


x=int(input("Enter Number1:"))
y=int(input("Enter Number2:"))
p2.getsum(x,y)
p2.getmul(x,y)

