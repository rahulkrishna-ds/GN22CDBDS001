
def binary(ele, n):
  s = ''
  while ele:
    s += str(ele%2)
    ele = ele//2
  fill = n - len(s)
  return '0'*fill+s[::-1]
n = int(input())
total = 2**n
for ele in range(total):
  print(binary(ele, n))