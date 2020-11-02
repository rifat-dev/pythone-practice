x=int(input("Enter a number : "))
count=0
for i in range(3,x):
    for j in range(2,i):
        if(i%j==0):
            count=count+1

    if(count==0):
        print(i,end=" ")
    count=0

    
      
            
            
    
            

    
    



