a=['0','1','2','3','4','5','6','7','8']
count=0
judge=False
placelist=[]

def game(a,placelist):
    skip=True
    while skip==True:
        place=input('場所を選択してください:')
        if place not in ['0','1','2','3','4','5','6','7','8']:
            print('無効な入力値です。場所を再度入力しなおしてください。')
            skip=True
            continue
        place=int(place)
        if place in placelist:
            print('すでに使われている場所です。場所を再度入力しなおしてください。')
            skip=True
            continue
        if count%2 !=0:
            MorB='○'
        else:
            MorB='×'    
        a[place]=MorB
        placelist.append(place)
        skip=False
    return a

def check(a,judge):
    cb1=a[0]==a[1]==a[2]
    cb2=a[3]==a[4]==a[5]
    cb3=a[6]==a[7]==a[8]
    cv1=a[0]==a[3]==a[6]
    cv2=a[1]==a[4]==a[7]
    cv3=a[2]==a[5]==a[8]
    cr=a[0]==a[4]==a[8]
    cl=a[2]==a[4]==a[6]
    if cb1 or cb2 or cb3 or cv1 or cv2 or cv3 or cr or cl:
        judge=True
    return judge



print('まるばつゲームスタート')
print('\n',
      '|',a[0],'|',a[1],'|',a[2],'|','\n',
      '|',a[3],'|',a[4],'|',a[5],'|','\n',
      '|',a[6],'|',a[7],'|',a[8],'|','\n',)
while judge==False and count!=9:
    game(a,placelist)
    count +=1
    print('\n',
          '|',a[0],'|',a[1],'|',a[2],'|','\n',
          '|',a[3],'|',a[4],'|',a[5],'|','\n',
          '|',a[6],'|',a[7],'|',a[8],'|','\n',)
    judge=check(a,judge)
if judge:
    if count%2 !=0:
        print('先行（×）の勝利')
    else:
        print('後攻（○）の勝利')
else:
    print('引き分け')
