import json
import urllib.request
lst='''elmiram, maryszmary, lizaku, nevmenandr, ancatmara, roctbb, akutuzov, agricolamz, lehkost, kylepjohnson, mikekestemont, demidovakatya, shwars, JelteF, timgraham, arogozhnikov, jasny, bcongdon, whyisjake, gvanrossum'''.split(', ')
def un(user):
    b={}
    token='cbcc3d314e88ce96be514a8e3d284ef1d8d7cad9'
    url = 'https://api.github.com/users/%s/repos?access_token=%s' % (user,token)
    response = urllib.request.urlopen(url)
    total = response.read().decode('utf-8')
    total= json.loads(total)
    print('Репозитории пользователя и их описания: ')
    for a in total:
        b[a['name']]=a['description']
    for a in b.keys():
        print(a,': ',b[a])
def deux(user):
        b={}
        token='cbcc3d314e88ce96be514a8e3d284ef1d8d7cad9'
        url = 'https://api.github.com/users/%s/repos?access_token=%s' % (user,token)
        response = urllib.request.urlopen(url)
        total = response.read().decode('utf-8')  
        total = json.loads(total)
        print('Список языков и соответствующих репозиториев: ')
        for c in total:
            if c['language'] not in b.keys():
                b[c['language']]=1
            else:
                b[c['language']]+=1
        for a in b:
            print('Число репозиториев, использующих ',a,': ', b[a])
def trois(lst):
    b=['',0]
    token='cbcc3d314e88ce96be514a8e3d284ef1d8d7cad9'
    for a in lst:
        user=a
        url = 'https://api.github.com/users/%s/repos?access_token=%s' % (user,token)
        response = urllib.request.urlopen(url)
        total = response.read().decode('utf-8')  
        reps = len(json.loads(total))
        if reps>b[1]:
            b[0] = a
            b[1] = reps
    return(print('Пользователь с наибольшим числом репозиториев: ',b[1]))

def quatre(lst):
    token='cbcc3d314e88ce96be514a8e3d284ef1d8d7cad9'
    b={}
    num=0
    nim=''
    for a in lst:
        user=a
        url = 'https://api.github.com/users/%s/repos?access_token=%s' % (user,token)
        response = urllib.request.urlopen(url)
        total = response.read().decode('utf-8')
        total= json.loads(total)
        for c in total:
            if c['language'] not in b.keys():
                b[c['language']]=1
            else:
                b[c['language']]+=1
    for a in b:
        if b[a] > num:
            num=b[a]
            nim=a
    return(print('Самый популярный язык: ',nim,',',num),' репозиториев')
def cinq(lst):
    token='cbcc3d314e88ce96be514a8e3d284ef1d8d7cad9'
    b=['',0]
    for a in lst:
        user=a
        url = 'https://api.github.com/users/%s/followers?access_token=%s' % (user,token)
        response = urllib.request.urlopen(url)
        total = response.read().decode('utf-8')  
        reps = len(json.loads(total))
        if reps>b[1]:
            b[0] = a
            b[1] = reps
    return(print('Больше всего фоловеров у пользователя: ',b))
def main(lst):
    inp=input('Введите имя пользователя из списка: ')
    while inp not in lst:
        inp=input('Такого пользователя нет, попробуйте еще раз: ')
    print('Вы выбрали пользователя', inp)
    un(inp)  
    deux(inp)
    trois(lst)
    quatre(lst)
    cinq(lst)
main(lst)   
#user = "ancatmara"  
#url = 'https://api.github.com/users/%s/repos' % user  

#response = urllib.request.urlopen(url)
#text = response.read().decode('utf-8')  
#data = json.loads(text) 
#print(len(data))  
#for i in data:
#    print(i)
#    break
