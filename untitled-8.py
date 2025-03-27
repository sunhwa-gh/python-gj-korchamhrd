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


print("==0이 입력되기전까지의 최대값 구하기")
a= int(input("정수: "))
m = a
while a!=0:
    if a>m:
        m = a
    a = int(input("정수: "))
print("최대값: ", m)