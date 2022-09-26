import csv


def read(n):
    books=[]
    for i in range(n):
        no,title,author,price=input("Enter number,title,author and price: ").split(',')
        price=float(price)
        books.append([no,title,author,price])
    with open("book.csv",'w',newline='') as f:
        w=csv.writer(f)
        w.writerows(books)
    print("Book are:",books)
    
def authorsearch():
    a=input("Enter author to search: ")
    flag=0
    with open("book.csv") as f:
        r=csv.reader(f)
        for book in r:
            if a==book[2]:
                flag=1
                print("Book Details are: ",book[0],book[1],book[2],book[3])
        
        if flag==0:
            print("Book not found!!")
            
def titlesearch():
    a=input("Enter title to search")
    flag=0
    with open("book.csv") as f:
        r=csv.reader(f)
        for book in r:
            if a==book[1]:
                flag=1
                print("Book details are: ",book[0],book[1],book[2],book[3])
        if flag==0:
            print("Book not found")
            
def pricesearch():
    try:
        price=float(input("Enter the price to search the books under that price"))
        if price<=0:
            raise valueError("Invalid price")
        else:
            flag=0
            with open("book.csv") as f:
                w=csv.reader(f)
                for book in w:
                    if price > float(book[3]):
                        flag=1
                        print("Book details are: ",book[0],book[1],book[2],book[3])
                    if flag==0:
                        print("book not found!!")
    except valueError as e:
        print("ValueError",e,type(e))
        
def main():
    n=int(input("Enter the number of books:"))
    read(n)
    while True:
            c=int(input("1.Author search\t2.titlesearch\t3.price search\t4.exit\nEnter the option:"))
            if c==1:
                authorsearch()
            elif c==2:
                titlesearch()
            elif c==3:
                pricesearch()
            else:
                break
            
if __name__=='__main__':
    main()
            

            