L= ['a','б','в',1,2,3,4]
print(L[1:4])
print(L[0:7:3])
print(L[-4:-9:-1])
print(L[-1:-4:-1])


N = [ 3.3,4.4,5.5,6.6]
print(list(map(round,N)))

string = input("введите список чисел через пробел:")
list_string =string.split()
print(list_string)
list_number = list(map(int,list_string))
print(list_number)
print(list_number[::3])

i=0
t=len(list_number)
summ = 0
for item in list_number:
    summ+= item
    i+=1

print(summ)
print(i)

print(list_number)

a=list_number[0]
b=list_number[-1]
list_number.pop(0)
list_number.pop(-1)
new_list=[]
new_list.append(b)
i=0
for item in list_number:
    new_list.append(list_number[i])
    i+=1
new_list.append(a)
new_list.append(summ)

print(new_list)
