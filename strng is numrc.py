l=str(input())
try:
  i=float(l)
except(ValueError,TypeError):
    print('no')
else:
  print('yes')
