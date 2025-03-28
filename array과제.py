#예제37 :  1부터 10까지 수 저장하고 출력하기기
a=[]
for i in range(1,11):
    a.append(i)
print(a)


#예제 38:  10,20,30,..,100 저장하고 거꾸로 출력하기
a=[]
for i in range(0, 10):
    a.append((i+1)*10)
print(a)

for i in range(9, -1, -1):
    print(a[i], end=" ")


#예제 39:  배열요소 거꾸로 뒤집기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, 5):
    temp = a[i]
    a[i] = a[9-i]
    a[9-i] = temp
print(a)

#==reverse함수이용해서 리스트 거꾸로 출력
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.reverse()
print(a)


#예제 40:  배열 A를 배열B에 거꾸로 저장하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in range(0,10):
    b.append(a[9-i])
print(b)


#예제 41:  배열 요소를 왼쪽으로 한 칸씩 원형으로 이동하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp = a[0]
for i in range(0,9):
    a[i]=a[i+1]
a[9]=temp
print(a)


#예제 42: 배열 최대값 구하기
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

#함수 max와 min함수 이용하기기
print("최대값: ", max(a))
print("최소값: ", min(a))


#예제 43: 에라ㅏ토스테네스의 체로 소수 구하기
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


#예제 44: 십진수를 이진수로 변환환
b=[]
n= random.randint(1,100)
print()
print(n, "의 이진수 : ", end="")
while n != 0:
    b.append(n%2)
    n = n//2

for i in range(len(b)-1, -1, -1):
    print(b[i], end=" ")


#예제 45: 배열의 2진수를 10진수로 변환하기
print()
print("다시 십진수로: ", end = "")
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


#예제 47: 이진탐색
a = [11, 18, 26, 27, 39, 57, 63, 75, 76, 80]
index=random.randint(0,9)
print("key: ", a[index])
print(a)
print("key: ", a[index])
key = a[index]
low=0
high=9
while low <= high:
    mid = (low+high)//2
    if key == a[mid]:
        print(mid+1, "번째에서 탐색성공")
        break
    elif key < a[mid]:
        high = mid-1
    else:
        low = mid+1
if low > high:
    print("탐색 실패")


#예제 48 : 선택정렬
b=[]
for i in range(0, 10):
    b.append(random.randint(1,100))
print("선택정렬: ",b)
for i in range(0, len(b)-1):
    m=i
    for j in range(i+1, len(b)):
        if b[j] < b[m]:
            m=j
    temp = b[i]
    b[i]= b[m]
    b[m]= temp
print(b)


#예제 49: 버블정렬
a=[]
for i in range(0, 10):
    a.append(random.randint(1,100))
print("버블정렬: ", a)
for i in range(0, 9):
    for j in range(0, 9-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(a)

#예제 50: 병합정렬

a = [1, 3, 5, 7]
b = [3, 4, 8, 10]
c = []
i = 0
j = 0
print("배열 a: ", a)
print("배열 b: ", b)
while i<4 and j<4:
    if a[i]<b[j]:
        c.append(a[i])
        i = i+1
    else:
        c.append(b[j])
        j = j+1
if i==4:
    while j<4:
        c.append(b[j])
        j = j+1
else:
    while i<4:
        c.append(a[i])
        i= i+1
print("병합정렬 : ", c)

