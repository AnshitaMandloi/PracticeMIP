'''num=int(input("Enter a num: "))
temp = num
digits = 0
while temp > 0:
    digits += 1
    temp //= 10

temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print(f"{num} is Armstrong number")
else:
    print(f"{num} not an Armstrong number ")
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if reverse == num:
    print(f"{num} is a Palindrome number ")
else:
    print(f"{num} not a Palindrome number ")
i=1
sum=0
while i<=num:
    if(i%2!=0):
        sum+=i
    else:
        sum-=i
    i+=1
print(sum)
list=[1,2,2,4,5]
for i in list:
    print(i,end=" ")
    '''
'''
Indexing and slicing in list/tuple:
left to right index:  0   1   2   3   4   5   6   7   8   9
elements:            11  22  33  44  55  66  77  88  99  110
right to left index:-10  -9  -8  -7  -6  -5  -4  -3  -2  -1
print(myList[2:-3])
print(myList[-8:-3])
print(myList[-8:7])

'''
myList=[ 11 , 22 , 33 , 44 , 55 , 66 , 77 , 88 , 99 , 110]
print(myList[2:-3])
print(myList[-8:-3])
print(myList[6:-9:-1])
