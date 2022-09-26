class person:
    def __init__(self,fn,ln,email):
        self.fname=fn
        self.lname=ln
        self.email=email
        
    def disp(self):
        print(self.fname,self.lname,self.email)

class customer(person):
    def __init__(self,fn,ln,email,no):
        person.__init__(self,fn,ln,email)
        self.no=no
        
    def disp(self):
        person.disp(self)
        print("customer no:",self.no)
        
class employee(person):
    def __init__(self,fn,ln,email,pan):
        person.__init__(self,fn,ln,email)
        self.pan=pan
        
    def disp(self):
        person.disp(self)
        print("employee pan:",self.pan)
        
        
def show(ob):
    if isinstance(ob,customer):
        print("customer:")
        ob.disp()
    elif isinstance(ob,employee):
        print("Employee:")
        ob.disp()
    elif isinstance(ob,person):
        print("person:")
        ob.disp()
        
def main():
    while True:
        fn,ln,email=input("Enter fname,lname,email:").split()
        print("1.customer\t2.Employee\t3.person\t4.exit")
        opt=int(input("Enter your option:"))
        if opt==1:
            no=int(input("Enter Customer number:"))
            c=customer(fn,ln,email,no)
            show(c)
        elif opt==2:
            pan=input("Enter pan number:")
            e=employee(fn,ln,email,pan)
            show(e)
        elif opt==3:
            p=person(fn,ln,email)
            show(p)
        elif opt==4:
            break
        else:
            print("Invalid input!!")
        
        choice=input("Customer (y/n)? :")
        
if __name__=='__main__':
    main()
        
        
            
            
        
        