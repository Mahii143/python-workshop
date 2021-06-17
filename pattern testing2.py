n = int(input())

val = 1

for i in range(n):
  
  for j in range(0,i+1):
    
    print(val**2, end = " ")
    val += 1

  if j == (n-1):

      break

  print()
    
