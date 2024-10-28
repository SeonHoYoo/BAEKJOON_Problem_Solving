# -*- coding: utf-8 -*-
"""11단계 시간 복잡도

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1flsUPKfrKvn8Wtpa0SuFpTDj9dX3eThq
"""

#24262

'''
MenOfPassion(A[], n) {
    i = ⌊n / 2⌋;
    return A[i]; # 코드1
}
'''

n = int(input())
print(1)
print(0)

#24263

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
}
'''

n = int(input())
print(n)
print(1)

#24264

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''

n = int(input())
print(n**2)
print(2)

#24265

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''

n = int(input())
print(int(((n-1)*(n))/2))
print(2)

#24266

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''

n = int(input())
print(n**3)
print(3)

#24267

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''

n = int(input())
print(int((n*(n-1)*(n-2))/(3*2*1)))
print(3)

#24313
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
buffer = 0

for n in range(n0,101):
  f = a1*n + a0
  g = c * n
  if f <= g and a1 <= c:
    buffer += 1
  else:
    print(0)
    break

if buffer > 0:
  print(1)

