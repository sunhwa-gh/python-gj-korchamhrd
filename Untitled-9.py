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
