#369
i = int(input("게임 횟수 :"))
type =input("a/b? ")
j= 1
if type=="a":
    print("while문으로")
    while i >0:
        if ((j%10%3==0) and (j%10!=0))or ((j//10!=0)and (j//10%3==0)):
            print("(박수)")
        else :
            print(j)
        i-=1
        j+=1

elif type=="b":
    print("for문으로")
    for count in range(0,i):
        if ((j%10%3==0) and (j%10!=0))or ((j//10!=0)and (j//10%3==0)):
            print("(박수)")
        else :
            print(j)
        j+=1
else :
    print("try again")
    
        
