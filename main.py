#Логвинов Борис
#Львов Олег
a=['1 ученик','2 ученик','3 ученик','4 ученик','5 ученик']
b=['1 предмет','2 предмет','3 предмет']
c=[5,4,5,3,5,4,3,4,3,4,5,4,5,5,5]
p=[]
q=0
n=1
s=0
k=0
o=[]
for i in range(5):
    print((a[i]))
    for i in range(3):
        print(b[i])
        for i in range(q,n):
            print(c[i])
            q+=1
            n+=1
q=0
n=3
for i in range(q,n):
    s=s+c[i]
print('балл 1 ученика',s/3)
if s/3==5:
    p.append(a[0])
if (c[q]==4 and c[q+1]==4 and c[q+2]==4) or (c[q]==5  and c[q+1]==5 and c[q+2]==4) or (c[q]==4  and c[q+1]==5 and c[q+2]==4) or (c[q]==4  and c[q+1]==4 and c[q+2]==5) or (c[q]==5  and c[q+1]==4 and c[q+2]==5) or (c[q]==5  and c[q+1]==4 and c[q+2]==4) or (c[q]==4  and c[q+1]==5 and c[q+2]==5):
    k+=1
if c[q]<4 or c[q+1]<4 or c[q+2]<4:
    o.append(a[0])
q+=3
n+=3
s=0
for i in range(q,n):
    s+=c[i]
print('балл 2 ученика',s/3)
if s/3==5:
    p.append(a[1])
if (c[q]==4 and c[q+1]==4 and c[q+2]==4) or (c[q]==5  and c[q+1]==5 and c[q+2]==4) or (c[q]==4  and c[q+1]==5 and c[q+2]==4) or (c[q]==4  and c[q+1]==4 and c[q+2]==5) or (c[q]==5  and c[q+1]==4 and c[q+2]==5) or (c[q]==5  and c[q+1]==4 and c[q+2]==4) or (c[q]==4  and c[q+1]==5 and c[q+2]==5):
    k+=1
if c[q]<4 or c[q+1]<4 or c[q+2]<4:
    o.append(a[1])
q+=3
n+=3
s=0
for i in range(q,n):
    s+=c[i]
print('балл 3 ученика',s/3)
if s/3==5:
    p.append(a[2])
if (c[q]==4 and c[q+1]==4 and c[q+2]==4) or (c[q]==5  and c[q+1]==5 and c[q+2]==4) or (c[q]==4  and c[q+1]==5 and c[q+2]==4) or (c[q]==4  and c[q+1]==4 and c[q+2]==5) or (c[q]==5  and c[q+1]==4 and c[q+2]==5) or (c[q]==5  and c[q+1]==4 and c[q+2]==4) or (c[q]==4  and c[q+1]==5 and c[q+2]==5):
    k+=1
if c[q]<4 or c[q+1]<4 or c[q+2]<4:
    o.append(a[2])
q+=3
n+=3
s=0
for i in range(q,n):
    s+=c[i]
print('балл 4 ученика',s/3)
if s/3==5:
    p.append(a[3])
if (c[q]==4 and c[q+1]==4 and c[q+2]==4) or (c[q]==5  and c[q+1]==5 and c[q+2]==4) or (c[q]==4  and c[q+1]==5 and c[q+2]==4) or (c[q]==4  and c[q+1]==4 and c[q+2]==5) or (c[q]==5  and c[q+1]==4 and c[q+2]==5) or (c[q]==5  and c[q+1]==4 and c[q+2]==4) or (c[q]==4  and c[q+1]==5 and c[q+2]==5):
    k+=1
if c[q]<4 or c[q+1]<4 or c[q+2]<4:
    o.append(a[3])
q+=3
n+=3
s=0
for i in range(q,n):
    s+=c[i]
print('балл 5 ученика',s/3)
if s/3==5:
    p.append(a[4])
if (c[q]==4 and c[q+1]==4 and c[q+2]==4) or (c[q]==5  and c[q+1]==5 and c[q+2]==4) or (c[q]==4  and c[q+1]==5 and c[q+2]==4) or (c[q]==4  and c[q+1]==4 and c[q+2]==5) or (c[q]==5  and c[q+1]==4 and c[q+2]==5) or (c[q]==5  and c[q+1]==4 and c[q+2]==4) or (c[q]==4  and c[q+1]==5 and c[q+2]==5):
    k+=1
if c[q]<4 or c[q+1]<4 or c[q+2]<4:
    o.append(a[4])
i=0
sr1=c[i]+c[i+3]+c[i+6]+c[i+9]+c[i+12]
i+=1
sr2=c[i]+c[i+3]+c[i+6]+c[i+9]+c[i+12]
i+=1
sr3=c[i]+c[i+3]+c[i+6]+c[i+9]+c[i+12]
print('1 предмет',sr1/5)
print('2 предмет',sr2/5)
print('3 предмет',sr3/5)
print('список студентов на повышенную' ,p)
print('количество с обычной',k)
print('неуспевающие',o)