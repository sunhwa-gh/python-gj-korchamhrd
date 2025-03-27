
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


