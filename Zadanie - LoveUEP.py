niu ="82654"
for liczba in range (1,101):
    if liczba == 50:
        print (niu, end=", ")
    elif liczba % 3 ==0 and liczba % 5 ==0:
        print ("LoveUEP", end=", ")
    elif liczba % 3 ==0:
        print ("love", end=",")
    elif liczba % 5 ==0:
        print ("UEP",end=", ")
    else:
        print (liczba, end=", ")