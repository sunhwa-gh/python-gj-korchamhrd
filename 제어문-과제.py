print(5+3)
print(5-3)
print(5*3)
print(5/3)
print(5//3)
print(5%3)
print(5**3)

a = int(input("성적1: "))
b = int(input("성적2: "))
c = int(input("성적3: "))
sum = a+b+c
print("총점:", sum, "평균:", sum/3)

import math
r = int(input("반지름: "))
print("원의 넓이:", r*r*math.pi)


print("==factorial 값 구하기")
num= int(input("정수: "))
fact=1
for i in range (num, 0, -1):
    fact = fact *i
print(num, "의 factorial : ", fact)

print("==내부함수 이용한 factorial값 구하기")
import math
print(num, "의 factorial is : ", end="")
print(math.factorial(num))

# 약수 구하기
print("==약수값 구하기")
n= int(input("정수: "))
print(n, "의 약수 : ", end=" ")
for i in range (1, n+1):
    if n%i == 0:
        print(i, end=" ")


# 공약수 구하기
print()
print("==공약수 구하기")
n1= int(input("정수: "))
n2= int(input("이전 정수값보다 큰 정수: "))
for i in range(1, n1+1):
    if n1%i == 0 and n2%i == 0:
        print(i, end=" ")



# 최대대공약수 구하기기
print("==최대공약수 구하기")
n1=int(input("정수: "))
n2=int(input("이전값보다 큰 정수: "))
for i in range(n1, 0, -1):
    if n1%i ==0 and n2%i ==0:
        print(n1, "과 ", n2, "의 최대공약수는 ", i)
        break

#math모듈 이용
import math
print("math모듈 이용한 값")
print(math.gcd(n1, n2))


#소수값 판별
print("==소수값 판별하기")
chk=1
n=int(input("정수: "))
for i in range(2,n):
    if n%i == 0:
        chk=0
        break
if chk== 1:
    print(n, ": 소수임")
else:
    print(n, ": 소수아님")


print("==20번째까지의 피보나치값 구하기")
a=1
b=1
print(a, b, end=" ")
for i in range(3, 21):
    c=a+b
    print(c, end=" ")
    a=b
    b=c

print()
print("==0이 입력되기전까지의 최대값 구하기")
a= int(input("정수: "))
m = a
while a!=0:
    if a>m:
        m = a
    a = int(input("정수: "))
print("최대값: ", m)


print("==직각삼각형 모양으로 출력")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()


print("== 1부터 10까지의 약수 구하기")

for i in range(1, 11):
    print(i, "약수:", end=" ")
    for j in range(1, i+1):
         if i%j==0:
            print(j, end=" ")
    print()


print("==  100까지의 소수 구하기")
for i in range(2, 101):
    chk=1
    for j in range(2, i):
        if i%j==0:
            chk=0
            break
    if chk==1:
        print(i, end=" ")

print()
print("== 1, (1+2), .. (1+2+3..+10)의 합 구하기")
n=0
sum=0
for i in range(1,11):
    n=n+i
    sum= sum+n
print(sum)


print()
print("== 구구단 출력")
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j, end=" ")
    print()
