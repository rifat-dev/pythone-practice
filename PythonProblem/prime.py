num=19
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num," Is not prime")
            break

    else:
        print(num," Is Prime")
else:
    print(num," Is Not Peime")
    