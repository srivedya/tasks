nterms= int(input("Enter the number for sequence: "))
n1 = 0
n2 = 1
count = 0
if nterms<=0:
    print("please print a positive integer")
elif nterms == 1:
    print("The sequence is as follows",nterms,":")
    print(n1)
else:
    print("the sequence is:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


