listem=[]
ran=int(input("Enter the range upto which you want to add data : "))
for i in range(ran):
    item=int(input("Enter number to add in list : "))
    listem.append(item)
li=listem

#Selection sort program
def sorts(li):
    for i in range(len(li)):
        for j in range(i,len(li)):
            if li[i]>li[j]:
                #swap them
                li[i],li[j]=li[j],li[i]
                print(li)
            else:
                continue
    print("Your sorted list is=",li)

#Bubble sort algorithim
def sortb(li):
    for h in range(len(li)):
        for i in range(len(li)):
            #print("===>",li)
            for j in range(i+1,len(li)):
                #print("===>>",li)
                if li[i]>li[j]:
                    #swap them
                    li[i],li[j]=li[j],li[i]
                    print(li)
                else:
                    break
    print("Your sorted list is = ",li)

#Insertion sort program
def sorti(li,c):
    for i in range(len(li)-1):
        c=c+1
        for j in range(c,0,-1):
            if li[j-1]>li[j]:
                #swap them
                li[j-1],li[j]=li[j],li[j-1]
                print(li)
            else:
                continue
    print("here is your sorted list=",li)

#all sorting program using recursion
# selection sort using recursion
def selso(li,c):
    for i in range(c,len(li)-1):
        if li[c]>li[i+1]:
            #swap them
            li[c],li[i+1]=li[i+1],li[c]
            print(li)
        else:
            pass

    if c==(len(li)-1):
        print("here is your sorted list= ",li)
    else:
        selso(li,c+1)

#bubble sort using recursion
def bubso(li,c):
    for h in range(len(li)):
        for i in range(c,len(li)-1):
            if li[i]>li[i+1]:
            #swap them
                li[i],li[i+1]=li[i+1],li[i]
                print(li)
            else:
                continue
    if c==(len(li)-1):
        print("Your sorted list is =",li)
    else:
        bubso(li,c+1)      

#insertion sort using recursion
def insso(li,c):
    for i in range(c+1,0,-1):
        if li[i-1]>li[i]:
            #swap them
            li[i-1],li[i]=li[i],li[i-1]
            print(li)
        else:
            continue
    if c==(len(li)-2):
        print("Your sorted list is=",li)
    else:
        insso(li,c+1)

#options for sorting
def main():
    print("Enter 1 or 2 >>>")
    opt=int(input("1>Sorting 2>Sorting using recursion : "))
    if opt==1:
        optt=int(input("1>Selection sort 2>Bubble sort 3>Insertion sort : "))
        if optt==1:
            sorts(li)
            repeat()

        elif optt==2:
            sortb(li)
            repeat()

        elif optt==3:
            sorti(li)
            repeat()

        else:
            print("No such option available!")
            main()
    elif opt==2:
        optt=int(input("1>Selection sort 2>Bubble sort 3>Insertion sort : "))
        if optt==1:
            selso(li,0)
            repeat()

        elif optt==2:
            bubso(li,0)
            repeat()

        elif optt==3:
            insso(li,0)
            repeat()

        else:
            print("No such option available!")
            main()
def repeat():
    print("Do you want to check more sorting :")
    choice=input("Enter 'yes' to check or 'no' to exit : ").lower()
    if choice=='yes':
        main()
    else:
        exit()
main()