def happy_birthday(name,age):
    print(f"happy birthday to {name}")
    print(f"you are yooung and {age}")
    
happy_birthday("ramu",20)
happy_birthday("bamu",43)


def display_invoice(username,amount,due_date):
    print(f"hello{username}")
    print(f"your bill pf ${amount:.2f}is due:{due_date}")
display_invoice("joshwa",22,"1/2")

def add(x,y):
    
   z = x + y
   return z
def sub(x,y):
 z = x -y
 return z
def diff(x,y):
   z = x/y
   return z

print(add(4,5))
print(sub(3,4))
print(diff(3,3))


def names(k,y):
   k=k.upper()
   y=y.upper()
   return k + y
sal = names("hat","har")#yedi store garnu xa vaney var = function gar ani bala bahira
print(sal)#use garna pYIS

#working function with tuples
def b(num):
   maxnum=max(num)
   minnum=min(num)
   total=sum(num)
   return maxnum,minnum,total
num=(1,2,3,4,5,6,6,6,7)
see = b(num)
maxnum,minnum,total=b(num)
print(maxnum,"maxn")
print(minnum,"minnum")
print(total,"sum")

def c(num):
   maxnum = max(num)
   minnum = min(num)
   total = sum(num)
   return [maxnum,minnum,total]
num = [1,23434,5,5,5,66]
yes = c(num)
print("max",yes[0])
print("min",yes[1])
print("sum",yes[2])
