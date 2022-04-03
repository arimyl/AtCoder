n, k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

text = 'Yes'
flag_before = [1]*2
flag_now    = [0]*2

for i in range(n-1):
  flag_now[0] = 0
  flag_now[1] = 0
  if flag_before[0] == 1:
    if abs(A[i]-A[i+1]) <= k:
      flag_now[0] = 1
    if abs(A[i]-B[i+1]) <= k:
      flag_now[1] = 1
  if flag_before[1] == 1:
    if abs(B[i]-A[i+1]) <= k:
      flag_now[0] = 1
    if abs(B[i]-B[i+1]) <= k:
      flag_now[1] = 1
      
  if flag_now[0] == 0 and flag_now[1] == 0:
    text = 'No'
    break
  flag_before = flag_now[:]

print(text)