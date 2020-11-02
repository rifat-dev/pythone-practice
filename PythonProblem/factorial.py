x=int(input("Enter a number : "))
fact=1
if x<0:
    print("Sorry, Invalid Number")

elif x==0:
    print("Factioral Is 1")
else:
    for i in range(1,x+1):
        fact=fact*i
        
    print(x," Factorial is ",fact)