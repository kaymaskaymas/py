max=3

def enQueue(queue):
    if(len(queue)==max):
        print("Queue overflow")
    else:
        item = int(input("Enter item to enqueue: "))
        queue.append(item)
        
def dispQueue(queue):
    if(len(queue)==0):
        print("Queue empty")
    else:
            for item in queue:
                print(item,end='\t')
                
def deQueue(queue):
    if(len(queue)==0):
        print("Queue empty")
    else:
        return queue.pop(0)
    
def qFront(queue):
    if(len(queue)==0):
        print("Queue Empty")
    else:
        return queue[0]
    
def qRear(queue):
    if(len(queue)==0):
        print("Queue is empty")
    else:
        return queue[len(queue)-1]
    
def main():
    queue=[]
    while True:
        print("\n1.Enqueue\t2.Dequeue\t3.dispqueue\t4.Qfront\t5.Qrear\t6.exit")
        ch=int(input("Enter your choice:"))
        
        if(ch==1):
            enQueue(queue)
        elif(ch==2):
            print("Dequeued item is:",deQueue(queue))
        elif(ch==3):
            dispQueue(queue)
        elif(ch==4):
            print("Queue front is:",qFront(queue))
        elif(ch==5):
            print("Queue Rear is:",qRear(queue))
        elif(ch==6):
            return
        else:
            print("Invalid choice!!")
            
if __name__=="__main__":
    main()
        
    

        
            