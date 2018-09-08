import random
abcd=list('qwertyuiopasdfghjklzxcvbnm')
ran=random.choice(abcd)
print(abcd.index(ran),ran)
while 0==0:#can be done differently without breaks
    letter=input('qqwewqwe')
    while letter!=ran:
        if letter not in abcd:
            print('не туда')
        else:
            print('wrong by',abcd.index(ran)
                  -abcd.index(letter))
            print('не-а')
        letter=input('qqwewqwe')    
    break
print('успех')








#while input('дайте буков: ')!=ran:
#    if input not in abcd:
#        print('не туда')
#    else:
#        print(mod(abcd.index(ran)
#              -abcd.index(input())))
#    print('не-а')
#print('успех')
#to manifest difference between locations in a list
