def findAdd(*number):
    sum = 0
    for num in number:
        sum = sum + num
    print("Sum =",sum)

findAdd(10,20,30,40,50,60)#210
findAdd(10,100,500)#610