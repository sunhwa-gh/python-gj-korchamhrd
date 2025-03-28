a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, 5):
    temp = a[i]
    a[i] = a[9-i]
    a[9-i] = temp
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.reverse()
print(a)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp = a[0]

for i in range(0,9):
    a[i]=a[i+1]
a[9]=temp

print(a)


#예제 42
import random
a=[]
for i in range(10):
    a.append(random.randint(1,100))
print(a)
m=a[0]
for i in range(1,10):
    if m < a[i]:
        m = a[i]
print("최대값: ", m)

print("Max 함수이용 최대값: ", max(a))
print("Min 함수이용 최소값: ", min(a))


#예제 43
a=[]
for i in range(1, 102):
    a.append(0)
for i in range(2, 101):
    if a[i]==0:
        for j in range(i*2, 101, i):
            a[j]=1
for i in range(2,101):
    if a[i]==0:
        print(i, end=" ")


#예제 44:
b=[]
n= random.randint(1,100)
print()
print(n, "의 이진수 : ", end="")
while n != 0:
    b.append(n%2)
    n = n//2

for i in range(len(b)-1, -1, -1):
    print(b[i], end=" ")


#예제 45:
print()
print("이진수=>십진수: ", end = "")
n=0
for i in range(0, len(b)):
    n= n + b[i]*(2**i)
print(n)

#예제 46: 선형탐색
a=[26, 27, 39, 63, 57, 75, 11, 76, 80, 18]
key = random.randint(1,100)
print(a)
cnt=0
while cnt<10:
    if key == a[cnt]:
        print(cnt+1, "번째 요소에서 ", key, "탐색성공")
        break
    cnt = cnt+1
if cnt==10:
    print(key, "탐색 실패")

#in과 index이용 key값 찾기
if key in a:
    print(key, a.index(key)+1,"번째에서 탐색성공")
else: 
    print(key, "탐색실패")

    