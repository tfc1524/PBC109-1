consume = int ( input () )
find = 1000 - consume

a = find // 500
find = find - a * 500

b =  find  // 100
find = find - b * 100

c = find // 50
find = find - c * 50

d = find // 10
find = find - d * 10

e = find // 5
find = find - e * 5

f = find

print (a,b,c,d,e,f)
