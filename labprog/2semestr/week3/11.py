from collections import Counter
input = open('input.txt','r')
s = input.read()
s = s.split()
counter = Counter(sorted(s))
print(*sorted(counter.keys(), key = counter.get, reverse = True))



 
