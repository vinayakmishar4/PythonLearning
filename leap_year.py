x=int(input())

if x%4==0:
    if x%100 !=0:
        print(x,'This Leap Year')
    else :
        if x%400==0:
            print(x,'This Leap Year')
        else :
            print(x,'This not Leap Year')
else :
    print(x,'This Not Leap Year')
