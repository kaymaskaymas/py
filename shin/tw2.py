def add(courses):
    code,cname,fname,regs = input("Enter code,coursename,faculty,no_of_regs:").split(',')
    regs=int(regs)
    if code in courses:
        print("Duplicate codes not allowed")
    else:
        courses[code]=[cname,fname,regs]
        
def dispall(courses):
    if len(courses)==0:
        print("Courses dictonary is empty")
    else:
        for code,details in courses.items():
            print(code,details[0],details[1],details[2])
            
def disp(courses):
    ccode=input("Enter the course code:")
    if ccode in courses:
        print(ccode,courses[ccode])
    else:
        print("Course is not present")
        
def highest(courses):
    if(len(courses)==0):
        print("Courses dictonary is empty")
        return 
    max = 0
    for code,details in courses.items():
        if details[2]>max:
            max = details[2]
            
    hcourses=[]
    for code,details in courses.items():
        if details[2]==max:
            hcourses.append([code,details])
            
    print("Course with highest registration:",hcourses)
        
def main():
    courses={}
    
    while True:
        opt = int(input("1.Add course\t2.Display all\t3.Disp a course\t4.highest course\t5.exit\nEnter your choice:"))
        
        if opt==1:
            add(courses)
        elif opt==2:
            dispall(courses)
        elif opt==3:
            disp(courses)
        elif opt==4:
            highest(courses)
        elif(opt==5):
            return
        else:
            print("invalid option!!")
            break

if __name__=='__main__':
    main()
        