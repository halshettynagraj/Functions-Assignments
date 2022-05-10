def tringle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,1)):
      print('' ,trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
tringle(10) 
            