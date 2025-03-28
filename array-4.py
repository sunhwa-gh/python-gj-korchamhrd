import random

a = [11, 18, 26, 27, 39, 57, 63, 75, 76, 80]
index=random.randint(0,9)
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

for i in range(0, len(a)-1):
    m=i
    for j in range(i+1, len(a)):
        if a[j] < a[m]:
            m=j
    temp = a[i]
    a[i]= a[m]
    a[m]= temp
print(a)
