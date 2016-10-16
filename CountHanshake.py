while(1):
    n = input("Enter a number for count handshakes \n")
    sum=0
    for i in range(1,n):
        sum = sum+i
    print "Count of handshakes is :- ",sum
    temp=input("If You want to repeat press 1 or anything else to stop \n")
    if(temp!=1):
        break


