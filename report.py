a=['a0','a1','a2']
b=['b0','b1','b2']
c=['c0','c1','c2']
count=0
judge=False

def game(a,b,c):
    column=input('列を入力してください:')
    row=int(input('行を入力してください:'))
    if count%2 !=0:
        MorB='○'
    else:
        MorB='×'
    if column=='a':
        a[row]=MorB
    elif column=='b':
        b[row]=MorB
    else:
        c[row]=MorB
    return a,b,c

def check(a,b,c,judge):
    ca=a[0]==a[1]==a[2]
    cb=b[0]==b[1]==b[2]
    cc=c[0]==b[1]==b[2]
    c0=a[0]==b[0]==c[0]
    c1=a[1]==b[1]==c[1]
    c2=a[2]==b[2]==c[2]
    cr=a[0]==b[1]==c[2]
    cl=a[2]==b[1]==c[0]
    if ca or cb or cc or c0 or c1 or c2 or cr or cl:
        judge=True
    return judge

print('まるばつゲームスタート')
print('\n',
      '|',a[0],'|',a[1],'|',a[2],'|','\n',
      '|',b[0],'|',b[1],'|',b[2],'|','\n',
      '|',c[0],'|',c[1],'|',c[2],'|','\n',)
while judge==False and count!=9:
    game(a,b,c)
    count +=1
    print('\n',
          '|',a[0],'|',a[1],'|',a[2],'|','\n',
          '|',b[0],'|',b[1],'|',b[2],'|','\n',
          '|',c[0],'|',c[1],'|',c[2],'|','\n',)
    judge=check(a,b,c,judge)
if judge:
    if count%2 !=0:
        print('先行（×）の勝利')
    else:
        print('後攻（○）の勝利')
else:
    print('引き分け')
