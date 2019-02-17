fin=open("ask4.txt")
data=fin.readlines()
fin.close()
z=0
o=1
t=2
th=3
f=4
fi=5
s=6
se=7
e=8
n=9
for line in data :
 if "plus" in line :
  if "zero" in line :
   if "one" in line :
	print (z+o)
   elif "two" in line :
	print (z+t)
   elif "three" in line :
	print (z+th)
   elif "four" in line : 
	print (z+f)
   elif "five" in line :
	print (z+fi)
   elif "six" in line :
	print (z+s)
   elif "seven" in line : 
	print (z+se)
   elif "eight" in line :
	print (z+e)
   elif "nine" in line :
	print (z+n)
  if "one" in line :
   if "two" in line :
	print (o+t)
   elif "three" in line :
	print (o+th)
   elif "four" in line :
	print (o+f)
   elif "five" in line :
	print (o+fi)
   elif "six" in line :
	print (o+s)
   elif "seven" in line :
	print (o+se)
   elif "eight" in line :
	print (o+e)
   elif "nine" in line :
	print (o+n)
  if "two" in line :
   if "three" in line :
	print (t+th)
   elif "four" in line :
	print (t+f)
   elif "five" in line :
	print (t+fi)
   elif "six" in line :
	print (t+s)
   elif "seven" in line :
	print (t+se)
   elif "eight" in line :
	print (t+e)
   elif "nine" in line :
	print (t+n)
  if "three" in line :
   if "four" in line :
	print (th+f)
   elif "five" in line :
	print (th+fi)
   elif "six" in line :
	print (th+s)
   elif "seven" in line :
	print (th+se)
   elif "eight" in line :
	print (th+e)
   elif "nine" in line :
	print (th+n)
  if "four" in line :
   if "five" in line :
	print (f+fi)
   elif "six" in line :
	print (f+s)
   elif "seven" in line :
	print (f+se)
   elif "eight" in line :
	print (f+e)
   elif "nine" in line :
	print (f+n)
  if "five" in line :
   if "six" in line :
	print (fi+s)
   elif "seven" in line :
	print (fi+se)
   elif "eight" in line :
	print (fi+e)
   elif "nine" in line :
	print (fi+n)
  if "six" in line :
   if "seven" in line: 
	print (s+se)
   elif "eight" in line :
	print (s+e)
   elif "nine" in line :
	print (s+n)
  if "seven" in line :
   if "eight" in line :
	print (se+e)
   elif "nine" in line :
	print (se+n)
  if "eight" in line :
   if "nine" in line :
	print (e+n)
  if "zero(plus(zero()))" in line :
   print (z+z)
  if "one(plus(one()))" in line :
   print (o+o)
  if "two(plus(two()))" in line :
   print (t+t)
  if "three(plus(three()))" in line :
   print (th+th)
  if "four(plus(four()))" in line :
   print (f+f)
  if "five(plus(five()))" in line :
   print (fi+fi)
  if "six(plus(six()))" in line :
   print (s+s)
  if "seven(plus(seven()))" in line :
   print (se+se)
  if "eight(plus(eight()))" in line :
   print (e+e)
  if "nine(plus(nine()))" in line :
   print (n+n)
 elif "minus" in line :
  if "zero(minus(one()))" in line :
   d=z-o
   print d
  elif "one(minus(two()))" in line :
   d=z-o
   print d
  elif "two(minus(three()))" in line :
   d=z-o
   print d
  elif "three(minus(four()))" in line :
   d=z-o
   print d
  elif "four(minus(five()))" in line :
   d=z-o
   print d
  elif "five(minus(six()))" in line :
   d=z-o
   print d
  elif "six(minus(seven()))" in line :
   d=z-o
   print d
  elif "seven(minus(eight()))" in line :
   d=z-o
   print d
  elif "eight(minus(nine()))" in line :
   d=z-o
   print d
  elif "zero(minus(two()))" in line :
   d=z-t
   print d
  elif "one(minus(three()))" in line :
   d=z-t
   print d
  elif "two(minus(four()))" in line :
   d=z-t
   print d
  elif "three(minus(five()))" in line :
   d=z-t
   print d
  elif "four(minus(six()))" in line :
   d=z-t
   print d
  elif "five(minus(seven()))" in line :
   d=z-t
   print d
  elif "six(minus(eight()))" in line :
   d=z-t
   print d
  elif "seven(minus(nine()))" in line :
   d=z-t
   print d
  elif "zero(minus(three()))" in line :
   d=z-th
   print d
  elif "one(minus(four()))" in line :
   d=z-th
   print d
  elif "two(minus(five()))" in line :
   d=z-th
   print d
  elif "three(minus(six()))" in line :
   d=z-th
   print d
  elif "four(minus(seven()))" in line :
   d=z-th
   print d
  elif "five(minus(eight()))" in line :
   d=z-th
   print d
  elif "six(minus(nine()))" in line :
   d=z-th
   print d  
  elif "zero(minus(four()))" in line :
   d=z-f
   print d
  elif "one(minus(five()))" in line :
   d=z-f
   print d
  elif "two(minus(six()))" in line :
   d=z-f
   print d
  elif "three(minus(seven()))" in line :
   d=z-f
   print d
  elif "four(minus(eight()))" in line :
   d=z-f
   print d
  elif "five(minus(nine()))" in line :
   d=z-f
   print d
  elif "zero(minus(five()))" in line :
   d=z-fi
   print d
  elif "one(minus(six()))" in line :
   d=z-fi
   print d
  elif "two(minus(seven()))" in line :
   d=z-fi
   print d
  elif "three(minus(eight()))" in line :
   d=z-fi
   print d
  elif "four(minus(nine()))" in line :
   d=z-fi
   print d
  elif "zero(minus(six()))" in line :
   d=z-s
   print d
  elif "one(minus(seven()))" in line :
   d=z-s
   print d
  elif "two(minus(eight()))" in line :
   d=z-s
   print d
  elif "three(minus(nine()))" in line :
   d=z-s
   print d
  elif "zero(minus(seven()))" in line :
   d=z-se
   print d
  elif "one(minus(eight()))" in line :
   d=z-se
   print d
  elif "two(minus(nine()))" in line :
   d=z-se
   print d
  elif "zero(minus(eight()))" in line :
   d=z-e
   print d
  elif "one(minus(nine()))" in line :
   d=z-e
   print d
  elif "zero(minus(nine()))" in line :
   d=z-n
   print d
  elif "one(minus(zero()))" in line:
   d=o-z
   print d
  elif "two(minus(one()))" in line :
   d=o-z
   print d
  elif "three(minus(two()))" in line :
   d=o-z
   print d
  elif "four(minus(three()))" in line :
   d=o-z
   print d
  elif "five(minus(four()))" in line :
   d=o-z
   print d
  elif "six(minus(five()))" in line :
   d=o-z
   print d
  elif "seven(minus(six()))" in line :
   d=o-z
   print d
  elif "eight(minus(seven()))" in line :
   d=o-z
   print d
  elif "nine(minus(eight()))" in line :
   d=o-z
   print d
  elif "two(minus(zero()))" in line :
   d=t-z
   print d
  elif "three(minus(one()))" in line :
   d=t-z
   print d
  elif "four(minus(two()))" in line :
   d=t-z
   print d
  elif "five(minus(three()))" in line :
   d=t-z
   print d
  elif "six(minus(four()))" in line :
   d=t-z
   print d
  elif "seven(minus(five()))" in line :
   d=t-z
   print d
  elif "eight(minus(six()))" in line :
   d=t-z
   print d
  elif "nine(minus(seven()))" in line :
   d=t-z
   print d
  elif "three(minus(zero()))" in line :
   d=th-z
   print d
  elif "four(minus(one()))" in line :
   d=th-z
   print d
  elif "five(minus(two()))" in line :
   d=th-z
   print d
  elif "six(minus(three()))" in line :
   d=th-z
   print d
  elif "seven(minus(four()))" in line :
   d=th-z
   print d
  elif "eight(minus(five()))" in line :
   d=th-z
   print d
  elif "nine(minus(six()))" in line :
   d=th-z
   print d
  elif "four(minus(zero()))" in line :
   d=f-z
   print d
  elif "five(minus(one()))" in line :
   d=f-z
   print d
  elif "six(minus(two()))" in line :
   d=f-z
   print d
  elif "seven(minus(three()))" in line :
   d=f-z
   print d
  elif "eight(minus(four()))" in line :
   d=f-z
   print d
  elif "nine(minus(five()))" in line :
   d=f-z
   print d
  elif "five(minus(zero()))" in line :
   d=fi-z
   print d
  elif "six(minus(one()))" in line :
   d=fi-z
   print d
  elif "seven(minus(two()))" in line :
   d=fi-z
   print d
  elif "eight(minus(three()))" in line :
   d=fi-z
   print d
  elif "nine(minus(four()))" in line :
   d=fi-z
   print d
  elif "six(minus(zero()))" in line :
   d=s-z
   print d
  elif "seven(minus(one()))" in line :
   d=s-z
   print d
  elif "eight(minus(two()))" in line :
   d=s-z
   print d
  elif "nine(minus(three()))" in line :
   d=s-z
   print d
  elif "seven(minus(zero()))" in line :
   d=se-z
   print d
  elif "eight(minus(one()))" in line :
   d=se-z
   print d
  elif "nine(minus(two()))" in line :
   d=se-z
   print d
  elif "eight(minus(zero()))" in line :
   d=e-z
   print d
  elif "nine(minus(one()))" in line :
   d=e-z
   print d
  elif "nine(minus(zero()))" in line :
   d=n-z
   print d
  elif "zero(minus(zero()))" in line :
   print ("0")
  elif "one(minus(one()))" in line :
   print ("0")
  elif "two(minus(two()))" in line :
   print ("0")
  elif "three(minus(three()))" in line :
   print ("0")  
  elif "four(minus(four()))" in line :
   print ("0")
  elif "five(minus(five()))" in line :
   print ("0")
  elif "six(minus(six()))" in line :
   print ("0")
  elif "seven(minus(seven()))" in line :
   print ("0")
  elif "eight(minus(eight()))" in line :
   print ("0")
  elif "nine(minus(nine()))" in line :
   print ("0")
 elif "times" in line :
  if "zero" in line :
   if "one" in line :
	print (z*o)
   elif "two" in line :
	print (z*t)
   elif "three" in line :
	print (z*th)
   elif "four" in line : 
	print (z*f)
   elif "five" in line :
	print (z*fi)
   elif "six" in line :
	print (z*s)
   elif "seven" in line: 
	print (z*se)
   elif "eight" in line :
	print (z*e)
   elif "nine" in line :
	print (z*n)
  if "one" in line :
   if "two" in line :
	print (o*t)
   elif "three" in line :
	print (o*th)
   elif "four" in line :
	print (o*f)
   elif "five" in line :
	print (o*fi)
   elif "six" in line :
	print (o*s)
   elif "seven" in line :
	print (o*se)
   elif "eight" in line :
	print (o*e)
   elif "nine" in line :
	print (o*n)
  if "two" in line :
   if "three" in line :
	print (t*th)
   elif "four" in line :
	print (t*f)
   elif "five" in line :
	print (t*fi)
   elif "six" in line :
	print (t*s)
   elif "seven" in line : 
	print (t*se)
   elif "eight" in line :
	print (t*e)
   elif "nine" in line :
	print (t*n)
  if "three" in line :
   if "four" in line :
	print (th*f)
   elif "five" in line :
	print (th*fi)
   elif "six" in line :
	print (th*s)
   elif "seven" in line : 
	print (th*se)
   elif "eight" in line :
	print (th*e)
   elif "nine" in line :
	print (th*n)
  if "four" in line :
   if "five" in line :
	print (f*fi)
   elif "six" in line :
	print (f*s)
   elif "seven" in line :
	print (f*se)
   elif "eight" in line :
	print (f*e)
   elif "nine" in line :
	print (f*n)
  if "five" in line :
   if "six" in line :
	print (fi*s)
   elif "seven" in line :
	print (fi*se)
   elif "eight" in line :
	print (fi*e)
   elif "nine" in line :
	print (fi*n)
  if "six" in line :
   if "seven" in line :
	print (s*se)
   elif "eight" in line :
	print (s*e)
   elif "nine" in line :
	print (s*n)
  if "seven" in line :
   if "eight" in line :
	print (se*e)
   elif "nine" in line :
	print (se*n)
  if "eight" in line :
   if "nine" in line :
	print (e*n)
  if "zero(plus(zero()))" in line :
   print (z*z)
  if "one(plus(one()))" in line :
   print (o*o)
  if "two(plus(two()))" in line :
   print (t*t)
  if "three(plus(three()))" in line :
   print (th*th)
  if "four(plus(four()))" in line :
   print (f*f)
  if "five(plus(five()))" in line :
   print (fi*fi)
  if "six(plus(six()))" in line :
   print (s*s)
  if "seven(plus(seven()))" in line :
   print (se*se)
  if "eight(plus(eight()))" in line :
   print (e*e)
  if "nine(plus(nine()))" in line :
   print (n*n)


