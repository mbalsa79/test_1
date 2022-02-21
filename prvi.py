a=[]
n= int (input("Unesi duzinu niza: "))
for i in range (0,n):
    element=int (input(" "))
    a.append(element)

#print(a):
def Pozitivni(a):
 br=0 
 for i in range(0, len(a)):
     if a[i]>=0:
      br=br+1
 if br==len(a):
        print(" ---------> x=1")
        exit()

Pozitivni(a)

s=0
b=[]
for i in range (0,n):
    s=s+a[i]
    elemnet2=s
    b.append(s)

print(b)
Pozitivni(b)

def Najmanji_indeks(a):
 min=b[0]
 c=0
 for i in range(1,len(a)):
   if a[i]<min:
     min=a[i]
     c=i
 return(c)

 
    
print(Najmanji_indeks(b))

x= -2*b[Najmanji_indeks(b)] + b[Najmanji_indeks(b)] +1
print("Trazeno x je --------->",x)


 
    



   


   

