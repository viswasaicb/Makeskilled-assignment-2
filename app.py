a='rader'
b='madhu'
print(type(a),type(b))

#Check palindrome
print(a==a[::-1]) #'rader'=='rader'-True #start index - 0, stop index - 4, step - -1
#It has to start from stop index to start index
print(b==b[::-1]) #'madhu'=='uhdam'-False
